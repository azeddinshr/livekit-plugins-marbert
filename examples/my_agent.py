from tools import get_weather
from prompt import AGENT_INSTRUCTIONS
from livekit.plugins.marbert import MarbertTurnDetector
import logging

from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    JobProcess,
    MetricsCollectedEvent,
    RoomInputOptions,
    WorkerOptions,
    cli,
    metrics,
)
from livekit.plugins import noise_cancellation, openai, silero


load_dotenv(".env")
logger = logging.getLogger("agent")


class Assistant(Agent):
    def __init__(self):
        super().__init__(
            instructions=AGENT_INSTRUCTIONS,
            tools=[get_weather],
        )

    async def on_enter(self):
        await self.session.generate_reply(
            instructions=(
                "You are starting the conversation. "
                "The user has not spoken yet. "
                "Start with a greeting only in Saudi dialect. "
                "Say exactly: السلام عليكم! كيف أقدر أساعدك اليوم؟"
            )
        )


def prewarm(proc: JobProcess):
    """Load models (VAD + MARBERT) before accepting jobs."""
    proc.userdata["vad"] = silero.VAD.load()
    proc.userdata["marbert_detector"] = MarbertTurnDetector(
        model_name="azeddinShr/marbert-arabic-eou",
        threshold=0.5,
        device="cpu"
    )


async def entrypoint(ctx: JobContext):
    """Main LiveKit entrypoint (console or deployed)."""
    ctx.log_context_fields = {"room": ctx.room.name}

    # Get preloaded turn detector
    marbert_detector = ctx.proc.userdata["marbert_detector"]

    session = AgentSession(
        stt=openai.STT(
            model="gpt-4o-transcribe",
            language="ar"
        ),
        llm=openai.LLM(
            model="gpt-4o-mini"
        ),
        tts=openai.TTS(
            model="gpt-4o-mini-tts",
            voice="nova"
        ),
        vad=ctx.proc.userdata["vad"],
        turn_detection=marbert_detector
    )

    usage_collector = metrics.UsageCollector()

    @session.on("metrics_collected")
    def _on_metrics_collected(ev: MetricsCollectedEvent):
        metrics.log_metrics(ev.metrics)
        usage_collector.collect(ev.metrics)

    async def log_usage():
        summary = usage_collector.get_summary()
        logger.info(f"Usage: {summary}")

    ctx.add_shutdown_callback(log_usage)

    agent = Assistant()

    await session.start(
        agent=agent,
        room=ctx.room,
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    print("Connecting to LiveKit room:", ctx.room.name)
    await ctx.connect()
    print("Connected successfully.")


if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm, agent_name="eva")
    )
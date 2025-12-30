"""
Example: Saudi Arabic voice agent with MARBERT turn detection
"""
import asyncio
from livekit.plugins.marbert import MarbertTurnDetector
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    JobProcess,
    WorkerOptions,
    cli,
)
from livekit.plugins import openai, silero


def prewarm(proc: JobProcess):
    """Load models before accepting jobs (runs once at startup)."""
    # Load VAD
    proc.userdata["vad"] = silero.VAD.load()
    
    # Load MARBERT turn detector
    print("Loading MARBERT turn detector...")
    proc.userdata["marbert"] = MarbertTurnDetector(
        model_name="azeddinShr/marbert-arabic-eou",
        device="cpu"
    )
    print("✓ Models loaded and ready")


async def entrypoint(ctx: JobContext):
    """Main entrypoint for each connection."""
    await ctx.connect()
    
    # Get preloaded models from prewarm
    marbert = ctx.proc.userdata["marbert"]
    vad = ctx.proc.userdata["vad"]
    
    # Create agent session
    session = AgentSession(
        stt=openai.STT(model="gpt-4o-transcribe", language="ar"),
        llm=openai.LLM(model="gpt-4o-mini"),
        tts=openai.TTS(model="gpt-4o-mini-tts", voice="nova"),
        vad=vad,
        turn_detection=marbert  # Use MARBERT for Arabic EOU
    )
    
    # Create agent
    agent = Agent(
        instructions="أنت مساعد سعودي ذكي. تحدث باللهجة السعودية فقط."
    )
    
    # Start session
    await session.start(agent=agent, room=ctx.room)


if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
            prewarm_fnc=prewarm,  # Load models once at startup
            agent_name="saudi-assistant"
        )
    )
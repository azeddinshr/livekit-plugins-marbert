# LiveKit MARBERT Turn Detector

[![PyPI version](https://badge.fury.io/py/livekit-plugins-marbert.svg)](https://pypi.org/project/livekit-plugins-marbert/)
[![Python](https://img.shields.io/pypi/pyversions/livekit-plugins-marbert.svg)](https://pypi.org/project/livekit-plugins-marbert/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Arabic End-of-Utterance detection plugin for LiveKit Agents using fine-tuned MARBERT.

## Demo

<video controls width="100%">
  <source src="https://github.com/user-attachments/assets/84f6531d-10a8-4beb-8165-9e16e135783c" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## Installation

```bash
pip install livekit-plugins-marbert
```

Or install from source:

```bash
pip install git+https://github.com/azeddinshr/livekit-plugins-marbert.git
```

---

## Quick Start

See the complete working example in `examples/`, which includes:

* `my_agent.py` – Saudi Arabic voice agent with MARBERT turn detection
* `prompt.py` – Saudi dialect conversation instructions
* `tools.py` – Weather tool for Saudi cities
* `download_models.py` – Model preloader script

To run the example:
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install livekit-plugins-marbert livekit-plugins-openai livekit-plugins-silero python-dotenv

# Create .env file with your OpenAI API key
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# Pre-download models (recommended)
python download_models.py

# Run the agent
python my_agent.py console
```

---

## Step 3: Update examples/ structure

```text
examples/
├── my_agent.py           # Main agent with MARBERT
├── prompt.py             # Saudi Arabic instructions
├── tools.py              # Weather tools for Saudi cities
└── download_models.py    # Pre-download script
```

See `examples/basic_usage.py` for a complete working example.

---

## Features

* ✅ Fine-tuned on 125K Arabic utterances (SADA22 dataset)
* ✅ Specialized for Saudi dialect
* ✅ 77% F1 score, 30ms average CPU latency
* ✅ Drop-in replacement for LiveKit turn detector
* ✅ Compatible with LiveKit Agents 1.3.9+
* ✅ Production-ready with prewarm support

---

## Performance

| Metric            | MARBERT        | LiveKit Multilingual |
| ----------------- | -------------- | -------------------- |
| **F1 Score**      | 0.77           | 0.66*                |
| **Latency (CPU)** | 30ms           | 300ms*               |
| **Language**      | Arabic (Saudi) | 14 languages         |
| **Model Size**    | 163M params    | 500M params          |

* Comparison with community Arabic model

---

## Model Details

* **Base Model:** [UBC-NLP/MARBERT](https://huggingface.co/UBC-NLP/MARBERT) (163M parameters)
* **Fine-tuned Model:** [azeddinShr/marbert-arabic-eou](https://huggingface.co/azeddinShr/marbert-arabic-eou)
* **Training Dataset:** [azeddinShr/arabic-eou-sada22](https://huggingface.co/datasets/azeddinShr/arabic-eou-sada22)
* **Task:** Binary classification (complete vs incomplete utterance)
* **Training Data:** 125K samples from SADA22 (Saudi dialect focus)

---

## Configuration

```python
MarbertTurnDetector(
    model_name="azeddinShr/marbert-arabic-eou",  # HuggingFace model ID
    threshold=0.5,                              # EOU probability threshold
    device="cpu"                                # "cpu" or "cuda"
)
```

---

## Requirements

* Python >= 3.9
* livekit-agents >= 1.3.9
* transformers >= 4.30.0
* torch >= 2.0.0

---

## License

Apache 2.0

---

## Citation

If you use this model in your research, please cite:

```bibtex
@misc{marbert-arabic-eou,
  author = {Sahir, Azeddin},
  title = {MARBERT Arabic End-of-Utterance Detection},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/azeddinshr/livekit-plugins-marbert}
}
```

---

## Links

* [PyPI Package](https://pypi.org/project/livekit-plugins-marbert/)
* [GitHub Repository](https://github.com/azeddinshr/livekit-plugins-marbert)
* [Fine-tuned Model](https://huggingface.co/azeddinShr/marbert-arabic-eou)
* [Training Dataset](https://huggingface.co/datasets/azeddinShr/arabic-eou-sada22)
* [LiveKit Agents Documentation](https://docs.livekit.io/agents/)

"""
Download MARBERT model before running the agent
"""
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

print("Downloading MARBERT Arabic EOU model...")

model_name = "azeddinShr/marbert-arabic-eou"

try:
    print(f"Loading tokenizer from {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    print("✓ Tokenizer downloaded")
    
    print(f"Loading model from {model_name}...")
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    print("✓ Model downloaded")
    
    print(f"\nModel cached at: ~/.cache/huggingface/hub/")
    print("✓ Ready to run agent!")
    
except Exception as e:
    print(f"✗ Error: {e}")
    exit(1)
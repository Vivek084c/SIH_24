import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "microsoft/phi-2"

model = AutoModelForCausalLM.from_pretrained(model_name)
model.save_pretrained(f"cache/model/{model_name}")


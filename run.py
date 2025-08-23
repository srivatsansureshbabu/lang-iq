import torch
from transformers import MarianConfig, MarianMTModel, MarianTokenizer
import os

model_path = "/Users/srivatsansureshbabu/Desktop/LangIQ/marianmt_quantized"
state_dict_path = "/Users/srivatsansureshbabu/Desktop/LangIQ/marianmt_quantized/quantized_marianmt_state_dict.pth"

# 1️⃣ Load tokenizer
tokenizer = MarianTokenizer.from_pretrained(model_path)

# 2️⃣ Load architecture only
config = MarianConfig.from_pretrained(model_path, download=False)
model = MarianMTModel(config)

# 3️⃣ Load your saved state dict
state_dict = torch.load(state_dict_path, map_location="cpu")
# Remove 'model.' prefix if needed
state_dict = {k.replace("model.", ""): v for k, v in state_dict.items()}
model.load_state_dict(state_dict)
model.eval()

# 4️⃣ Test translation
english_text = "hello"
input_text = f">>tam<< {english_text}"  # prepend target language token
inputs = tokenizer(input_text, return_tensors="pt")

with torch.no_grad():
    translated = model.generate(**inputs)

tamil_text = tokenizer.decode(translated[0], skip_special_tokens=True)
print("Tamil:", tamil_text)

from fastapi import APIRouter
from pydantic import BaseModel
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

router = APIRouter()

# # Load Fine-Tuned Model
# MODEL_PATH = "./model/deepseek-finetuned"  # Adjust path
# BASE_MODEL = "deepseek-ai/deepseek-coder-6.7B"

# tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
# base_model = AutoModelForCausalLM.from_pretrained(BASE_MODEL, torch_dtype=torch.float16, device_map="auto")
# model = PeftModel.from_pretrained(base_model, MODEL_PATH)
# model.eval()

# Define input format
class RequestData(BaseModel):
    prompt: str
    max_length: int = 100

@router.post("/predict")
def generate_text(data: RequestData):
    input_ids = tokenizer(data.prompt, return_tensors="pt").input_ids.to(model.device)

    with torch.no_grad():
        output = model.generate(input_ids, max_length=data.max_length)

    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return {"response": response}

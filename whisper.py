import os
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

device = "cuda:0"
torch_dtype = torch.float16
model_id = "openai/whisper-large-v3"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)
pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch_dtype,
    device=device,
)

generate_kwargs = {
    "max_new_tokens": 300,
    "num_beams": 1,
    "condition_on_prev_tokens": False,
    "compression_ratio_threshold": 1.35,
    "temperature": [0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
    "logprob_threshold": -1.0,
    "no_speech_threshold": 0.6,
    "return_timestamps": True,
    "language": "japanese",
}

audio_path = "/home/guozr/下载/260125.mp3"
result = pipe(
    audio_path,
    generate_kwargs=generate_kwargs,
    chunk_length_s=30,
    stride_length_s=5,
)

text = result["text"]
print(text)

# 保存到同名 txt 文件
txt_path = os.path.splitext(audio_path)[0] + ".txt"
with open(txt_path, "w", encoding="utf-8") as f:
    f.write(text)
    print(f"已保存到: {txt_path}")

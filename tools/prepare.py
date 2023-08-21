from deepdanbooru_onnx import DeepDanbooru
import argparse
from PIL import Image
import requests
from transformers import AutoProcessor, Blip2ForConditionalGeneration
import torch
import json
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file","-i",type=str,help="URl or path")
    parser.add_argument("--output_file","-o",type=str,help="URl or path")

    args = parser.parse_args()
    model = DeepDanbooru()
    if args.input_file.startswith("http") or args.input_file.startswith("https"):
        image = Image.open(requests.get(args.input_file,stream=True).raw)
    else:
        image = Image.open(args.input_file)
    tags = ','.join(list(model(image))[:-1])

    processor = AutoProcessor.from_pretrained("Salesforce/blip2-opt-2.7b")
    model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b", torch_dtype=torch.float16,load_in_8bit=True,device_map='auto')

    inputs = processor(image, return_tensors="pt").to(model.device, torch.float16)

    generated_ids = model.generate(**inputs, max_new_tokens=30)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()
    json.dump({'id':'0001','tag':tags,'blip2_caption':generated_text},open(args.output_file,'w'))
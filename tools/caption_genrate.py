import openai
from tqdm import tqdm
try:
    import ujson as json
except:
    import json

# import multiprocessing as mp
import os
import argparse

openai.api_key = os.environ.get("OPENAI_KEY")

nums = 20000
def process_func(data):
    caption = []
    for d in tqdm(data[:5]):
        try:  
            answer = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
            {"role": "system", "content": "You are an image-text annotation assistant,\
            your task is to generate a long caption from a short caption and tag.\
            You will receive a caption and danbooru tag, and you will return a long caption,Your responses should be varied.\
            Output format:\
            Answer:you return a answer.\n"},
            {"role":"user","content":"caption:a girl with pink hair holding an ak - 47 rifle.\n\
            Tag:1girl, weapon, solo, gun, skirt, pink hair, blue eyes, holding, holding weapon, rifle, long hair, hat, sailor collar, school uniform"},
            {"role":"assistant","content":"Answer: The girl in the image has blue eyes and wears a sailor collar school uniform, holds an AK-47 rifle, wears a hat and has long pink hair.\n"},
            {"role":"user","content":f"caption:{d['blip2_caption']}\nTag:{d['tag']}.\n"}])["choices"][0]["message"]["content"]
            caption.append({"id":d['id'],'caption':answer})
        except Exception as e:
            pass
    return caption

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file","-i",type=str)
    parser.add_argument("--output_name","-o",type=str)
    args = parser.parse_args()

    data = json.load(open(args.input_file))
    result = process_func(data)
    json.dump(result,open(args.output_name,'w'))
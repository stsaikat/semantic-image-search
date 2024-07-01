from vectordb import Memory
import os
from PIL import Image
from clip_interrogator import Config, Interrogator
from tqdm import tqdm

memory = Memory(memory_file='db/db_file.vdb')
ci = Interrogator(Config(clip_model_name="ViT-L-14/openai"))

def create_db(image_collection_path):
    for file_name in tqdm(os.listdir(image_collection_path)):
        if '.png' in file_name or '.jpg' in file_name or '.jpeg' in file_name:
            image = Image.open(os.path.join(image_collection_path, file_name)).convert('RGB')
            caption = ci.interrogate(image)
            memory.save([caption],[file_name])

create_db(image_collection_path='images')
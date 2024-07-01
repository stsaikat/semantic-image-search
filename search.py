from vectordb import Memory
from PIL import Image
from clip_interrogator import Config, Interrogator

memory = Memory(memory_file='db/db_file.vdb')
ci = Interrogator(Config(clip_model_name="ViT-L-14/openai"))

def search_image(img_path, number_of_results):
    img = Image.open(img_path).convert('RGB')
    caption = ci.interrogate(img)
    results = memory.search(caption, top_n = number_of_results)

    for result in results:
        image_name = result['metadata']
        similarity = int((1 - result['distance'])*100)
        print(f'name = {image_name}, similarity = {similarity}%')

search_image(img_path='test_image.png', number_of_results=3)
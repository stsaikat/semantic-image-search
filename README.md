# Semantic aware Image search
Semantic aware image seach simple tool

## Installation
Create python virutal enviroment and install all requirements.

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Run

Create your db file
_put all your images in images folder or change the directory in the script_
Then run scripty with
```
python create_db.py
```

Search with your image
_change the image directory and put your image's directory_
Then run script with
```
python search.py
```

This script should print the names and similarity score % of the results at terminal.

## Credits
- [vectordb](https://github.com/kagisearch/vectordb) for their simple, lightweight, fully local, end-to-end solution for using embeddings-based text retrieval.
- [Clip Interrogator](https://github.com/pharmapsychotic/clip-interrogator) for their prompt engineering tool that combines OpenAI's CLIP and Salesforce's BLIP to optimize text prompts to match a given image

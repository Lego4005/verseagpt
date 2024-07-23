import os
import nltk

nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')

if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)

nltk.data.path.append(nltk_data_path)

required_packages = ['punkt', 'averaged_perceptron_tagger']

for package in required_packages:
    try:
        nltk.data.find(f'tokenizers/{package}')
    except LookupError:
        nltk.download(package, download_dir=nltk_data_path)

# Your application code here


from backend.server import app
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

from google.cloud import vision
from google.oauth2 import service_account

import os
from dotenv import load_dotenv
load_dotenv()

CREDENTIALS_PATH = os.getenv("CREDENTIALS_PATH")

credentials = service_account.Credentials.from_service_account_file(
    CREDENTIALS_PATH)

client = vision.ImageAnnotatorClient(credentials=credentials)


def ocr(image_path):
    with open(image_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    return texts[0].description

import os
import pytesseract
from PIL import Image
import openai
import re


openai.api_key = os.environ['OPENAI_API_KEY']

def extract_name_company(ocr):
    prompt = f"OCR TEXT:\n{ocr}\n\nAbove is the OCRed text for photo of someone's badge at a conference. Extract the name, company and title"
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=30,
        n=1,
        temperature=0.5
    )
    text = response.choices[0].message['content'].strip()
    return text

def ocr_images_in_notes():
    # Directory containing the images
    directory = 'notes'

    # Dictionary to store the OCR results
    ocr_results = {}

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is an image
        if filename.endswith('.png') or filename.endswith('.jpg'):
            # Open the image file
            with Image.open(os.path.join(directory, filename)) as img:
                # Perform OCR on the image
                text = pytesseract.image_to_string(img)
                # Store the OCR result in the dictionary
                ocr_results[filename] = text
                # print(f"{filename}: {ocr_results[filename]}")

    return ocr_results



# result = ocr_images_in_notes()
def replace_image_tags_with_ocr_text(ocr_result, chat_transcript):
    # Iterate over the OCR results
    for filename, ocr_text in ocr_result.items():
        # Construct the image tag
        image_tag = f"<attached: {filename}>"
        # Replace the image tag with the OCR text in the chat transcript
        chat_transcript = chat_transcript.replace(image_tag, f"[OCR: {ocr_text}]")

    return chat_transcript

ocr_results_raw = ocr_images_in_notes()
for filename, ocr_text in ocr_results_raw.items():
    ocr_results_raw[filename] = extract_name_company(ocr_text)
chat_transcript = open('./notes/_chat.txt', 'r').read()
updated_chat_transcript = replace_image_tags_with_ocr_text(ocr_results_raw, chat_transcript)


def replace_author_names(chat_transcript):
    # Define the authors
    authors = ["Harsh Gupta", "Ryan Yousefi"]

    # Iterate over the authors
    for author in authors:
        # Define the pattern to find the author's name and timestamp
        pattern = r"\[\d+/\d+/\d+, \d+:\d+:\d+ (AM|PM)\] " + author + ":"

        # Replace the author's name and timestamp with an empty string
        chat_transcript = re.sub(pattern, "", chat_transcript)

    return chat_transcript

updated_chat_transcript = replace_author_names(updated_chat_transcript)
with open('updated_chat.txt', 'w') as f:
    f.write(updated_chat_transcript)

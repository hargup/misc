import pytesseract
from PIL import ImageGrab
import sqlite3
import time
import cv2
import numpy as np
import os
import openai

# Replace 'your_api_key' with your actual GPT-3.5 API key
openai.api_key = os.environ['OPENAI_API_KEY']

# Create SQLite database and table
conn = sqlite3.connect('screenshots.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS screenshots (timestamp DATETIME, path TEXT, text TEXT, activity TEXT)''')
conn.commit()

def screenshot_and_ocr():
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_path = f'screenshots/{timestamp}.png'
    # Create screenshots directory if it doesn't exist
    if not os.path.exists('screenshots'):
        os.mkdir('screenshots')
    # Capture the screenshot
    screenshot = ImageGrab.grab()
    # Save the screenshot to disk
    screenshot.save(screenshot_path)
    print(f'Screenshot saved at {screenshot_path}')
    # Convert the screenshot to a numpy array and then to grayscale for OCR
    screenshot_np = np.array(screenshot)
    gray_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    # Perform OCR
    text = pytesseract.image_to_string(gray_screenshot)
    print(f'OCR done: {text}')

    # Send the OCRed text to GPT-3.5 Turbo
    prompt = f"Give a one-line description for what the person is doing based on the OCR of the screenshot: {text}"
    messages = [{"role": "system", "content": "You are a helpful assistant that can understand and describe activities based on OCR text from screenshots."},
                {"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=100, n=1, temperature=0.5)

    activity = response.choices[0].message['content'].strip()
    print(f'Activity: {activity}')

    # Insert the timestamp, path, text, and activity into the database
    cursor.execute("INSERT INTO screenshots (timestamp, path, text, activity) VALUES (?, ?, ?, ?)", (timestamp, screenshot_path, text, activity))
    conn.commit()

# Run the function every 30 seconds
while True:
    screenshot_and_ocr()
    time.sleep(30)

# Close the connection to the database
conn.close()
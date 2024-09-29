# Optical-Character-Recognition
# OCR and Keyword Search Application

This is a simple web application built with [Gradio](https://gradio.app/) that allows users to:
1. Upload an image file for Optical Character Recognition (OCR) processing using the EasyOCR library.
2. Extract text in both English and Hindi.
3. Search for keywords within the extracted text.
4. Highlight the matching sections of the text.

## Features
- Upload images containing text in English and Hindi.
- Perform OCR on the uploaded images to extract the text.
- Search for specific keywords within the extracted text.
- Highlight the keywords in red for easy identification.

---

## Table of Contents
1. [Requirements](#requirements)
2. [Setup](#setup)
3. [Running the App](#running-the-app)
4. [Deploying on Hugging Face Spaces](#deploying-on-hugging-face-spaces)


---

## Requirements

- **Python 3.7+**
- **Pip**

### Libraries Used
- **gradio**: For creating the web interface.
- **easyocr**: For extracting text from images.
- **opencv-python-headless**: Required for image processing by EasyOCR.
- **torch**: Required by EasyOCR for deep learning-based text recognition.

## Setup

### 1. Clone the Repository

Clone this repository to your local machine using:

```bash
git clone https://huggingface.co/spaces/Hecklar/OCRHindhiEnglish
cd 
```
## Install Dependencies 
```bash
pip install -r requirements.txt
```
## requiremnt.txt file includes
```bash
gradio
easyocr
opencv-python-headless
torch
```
## Running the App Locally
After installing the dependencies, you can run the application locally using
```bash
python app.py
```
# Deploying on Hugging Face Spaces
Steps to Deploy
1. Create a new Space on Hugging Face.
2. Select the Gradio SDK when setting up the Space.
3. Upload the app.py and requirements.txt files to the repository.
4. Once uploaded, the Hugging Face platform will automatically detect the Gradio application and install the dependencies.
5. The app will be deployed, and you will receive a URL where users can access it.

# Running the App
1. **Upload an Image**: Click on the "Upload an Image" button to select an image containing text.
2. **Extract Text**: The application will use EasyOCR to extract text from the image.
3. **Enter Keywords**: Enter keywords in the text box to search for them in the extracted text.
4. **Highlighting**: The matching keywords will be highlighted with a red background.





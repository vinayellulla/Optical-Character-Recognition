import gradio as gr
from easyocr import Reader
import re

# Initialize the EasyOCR model
reader = Reader(['en', 'hi'])  # English and Hindi

# Function to perform OCR and return extracted text
def ocr_processing(image):
    output = reader.readtext(image)
    # Extract only the text
    extracted_text = "\n".join([item[1] for item in output])
    return extracted_text

# Function to search for keywords in the extracted text and highlight them with red background
def search_text(extracted_text, keywords):
    if not keywords.strip():
        return extracted_text  # No search, just return original text
    
    # Highlighting the keywords with red background in the extracted text
    highlighted_text = re.sub(f"({keywords})", r"<mark style='background-color: red;'>\1</mark>", extracted_text, flags=re.IGNORECASE)
    return highlighted_text

# Gradio interface for the app
def gradio_app(image, keywords):
    # OCR Processing
    extracted_text = ocr_processing(image)
    
    # Search and Highlight
    highlighted_text = search_text(extracted_text, keywords)
    
    return highlighted_text

# Define the Gradio interface
interface = gr.Interface(
    fn=gradio_app,
    inputs=[
        gr.Image(type="filepath", label="Upload an Image"),  # Image upload
        gr.Textbox(lines=1, placeholder="Enter keywords to search", label="Search Keywords")  # Search keywords input
    ],
    outputs=gr.HTML(label="Extracted Text with Highlights"),  # Output as HTML for highlighting
    title="OCR and Keyword Search Application",
    description="Upload an image to extract text using OCR. Enter keywords to search within the extracted text."
)

# Launch the app
interface.launch()


# To calculate Metrices

from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def calculate_metrics(predicted_text, ground_truth_text):
    # Convert the text to lowercase and split into characters for character-level comparison
    predicted_chars = list(predicted_text.lower())
    ground_truth_chars = list(ground_truth_text.lower())
    
    # Pad the shorter list with empty spaces to make them the same length
    max_len = max(len(predicted_chars), len(ground_truth_chars))
    predicted_chars.extend([''] * (max_len - len(predicted_chars)))
    ground_truth_chars.extend([''] * (max_len - len(ground_truth_chars)))

    # Convert characters to numeric format for comparison (1 for match, 0 for no match)
    y_true = [1 if a == b else 0 for a, b in zip(ground_truth_chars, predicted_chars)]
    y_pred = [1 if a == b else 0 for a, b in zip(ground_truth_chars, predicted_chars)]

    # Calculate Accuracy
    accuracy = accuracy_score(y_true, y_pred)

    # Calculate Precision, Recall, and F1 Score
    precision = precision_score(y_true, y_pred, average='binary', zero_division=1)
    recall = recall_score(y_true, y_pred, average='binary', zero_division=1)
    f1 = f1_score(y_true, y_pred, average='binary', zero_division=1)
    
    return {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    }

# Example usage with OCR output and ground truth
predicted_text = "Iwill have to go जाना पड़ेगा"
ground_truth_text = "I will have to go जाना पड़ेगा"

# Calculate and print the metrics
metrics = calculate_metrics(predicted_text, ground_truth_text)
print(metrics)

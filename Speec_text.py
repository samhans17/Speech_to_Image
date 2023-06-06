import tkinter as tk
import speech_recognition as sr
import requests
from PIL import ImageTk, Image
import io

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Recording for 5 seconds")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=5)

    try:
        text = r.recognize_google(audio)
        print(f"Text: {text}")
        query_huggingface_api(text)
    except sr.UnknownValueError:
        print("I'm sorry, I didn't get that.")
    except sr.RequestError as e:
        print(f"Failed to convert speech to text: {e}")

def query_huggingface_api(text):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
    headers = {"Authorization": "Bearer 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"}
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content
    image_bytes = query({
    "inputs": text})
    show_image(image_bytes)

def show_image(image_bytes):
    global image_label  # Specify the global scope for the image_label variable

    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize((500, 500))
    photo = ImageTk.PhotoImage(image)
    image_label.configure(image=photo)
    image_label.image = photo

# Create the Tkinter window
window = tk.Tk()
window.title("Speech Recognition")
window.geometry("400x200")

# Create the UI components
label = tk.Label(window, text="Click the button and speak something:")
label.pack(pady=10)

button = tk.Button(window, text="Start Recording", command=recognize_speech)
button.pack(pady=10)

# Create a new window to display the image
image_window = tk.Toplevel(window)
image_window.title("Image Display")
image_window.geometry("550x550")

# A label to show the image
image_label = tk.Label(image_window)
image_label.pack()



# Run the Tkinter event loop
window.mainloop()

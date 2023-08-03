# Speech_to_Image

**Speech Recognition Application**

This application allows you to perform speech recognition and retrieve an image based on the recognized speech. To use the application, follow the instructions below.

## Prerequisites

pip install tk
pip install SpeechRecognition
pip install requests
pip install Pillow

**Make sure you have an active internet connection to access the Hugging Face API.**

## Instructions

1. Open your preferred Python IDE or text editor.
2. Copy the provided code into a new Python file.
3. Replace the placeholder API authorization token (`***********************************`) in the code with your own valid token. This token is required to access the Hugging Face model.
4. Save the file with a meaningful name, such as `speech_recognition_app.py`.
5. Open a command prompt or terminal and navigate to the directory where you saved the Python file.
6. Run the Python script using the following command:
  python location/of/the/file/speech_recognition_app.py
7. A window titled "Speech Recognition" will appear.
8. Click the "Start Recording" button. The application will start listening to your microphone input.
9. Speak something clearly and audibly into the microphone.
10. After 5 seconds of recording, the application will attempt to recognize the speech using the Google Speech Recognition engine.
11. If the speech is successfully recognized, the recognized text will be sent as input to the Hugging Face API.
12. The Hugging Face model will process the input and return an image.
13. A new window titled "Image Display" will appear, showing the retrieved image.

Make sure to replace the placeholder *********************************** with your actual Hugging Face API token.

# Speech_to_Image
**Speech Recognition Application**, This application allows you to perform speech recognition and retrieve an image based on the recognized speech. To use the application, follow the instructions below.
**Prerequisites**
Before running the code, ensure that you have the following libraries installed:
pip install tk
pip install SpeechRecognition
pip install requests
pip install Pillow

**Make sure you have an active internet connection to access the Hugging Face API.**

Instructions
Open your preferred Python IDE or text editor.
Copy the provided code into a new Python file.
Replace the placeholder API authorization token (***********************************) in the code with your own valid token. This token is required to access the Hugging Face model.

Save the file with a meaningful name, such as speech_recognition_app.py.
Open a command prompt or terminal and navigate to the directory where you saved the Python file.
Run the Python script using the following command:
python location/of/the/file/speech_recognition_app.py

A window titled "Speech Recognition" will appear.

Click the "Start Recording" button. The application will start listening to your microphone input.

Speak something clearly and audibly into the microphone.

After 5 seconds of recording, the application will attempt to recognize the speech using the Google Speech Recognition engine.

If the speech is successfully recognized, the recognized text will be sent as input to the Hugging Face API.

The Hugging Face model will process the input and return an image.

A new window titled "Image Display" will appear, showing the retrieved image.

You can repeat the process by clicking the "Start Recording" button again and speaking a new phrase.

To exit the application, close the windows or terminate the Python process in the command prompt or terminal.


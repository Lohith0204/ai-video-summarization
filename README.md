# AI Video Summarizer

## Live Demo
Try out the deployed application here:

🚀 **Streamlit App** → https://ai-video-summarization.streamlit.app/

## Overview
This project is an AI-based video summarization application that automatically generates concise summaries from video content. The system extracts audio from uploaded videos, converts speech into text using the Whisper model, and then applies Natural Language Processing (NLP) techniques to summarize the transcribed content.

The application provides a simple web interface where users can upload a video file and receive an AI-generated summary of the spoken content.

## Features
- Upload video files in `.mp4`, `.mov`, or `.avi` format  
- Automatically extract audio from video  
- Convert speech audio into text using Whisper  
- Generate concise summaries using Transformer-based NLP models  
- Clean and minimal user interface built using Streamlit  

## Tech Stack
- Python  
- Streamlit  
- OpenAI Whisper  
- Hugging Face Transformers  
- PyTorch  

## Project Structure

```text
AI-Video-Summarization/
│
├── app.py                # Streamlit UI and application logic
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
├── assets
│   └──Sample.mp4         # Sample video file  
├── gitignore.txt         # Ignore files
│
├── ai_engine/
│   ├── speech.py         # Video audio transcription logic
│   └── summarize.py      # Text summarization logic
│
└── screenshots/          # Application screenshots
    ├── home.png
    ├── upload.png
    └── result.png
```

## Screenshots

### Application Interface
![Application Interface](<screenshots/Screenshot 2025-12-22 161707.png>)

### Audio Upload
![Video Upload](<screenshots/Screenshot 2025-12-22 161739.png>)

### Transcription Output
![Summary Output](<screenshots/Screenshot 2025-12-22 161901.png>)

## How It Works
First, all the required dependencies are installed and the application is started. Once the app is running, the user is presented with a simple web interface. The user uploads a video file using the file uploader and clicks the Generate Summary button.

The system extracts the audio track from the video and processes it using the Whisper speech-to-text model. The transcribed text is then passed through a Transformer-based summarization model, which generates a concise summary of the video’s spoken content. The final summary is displayed on the screen after processing.

## Installation & Setup
1. Open your IDE (VS Code is recommended).
2. Clone or download the project files to your local system.
3. Create a virtual environment to avoid dependency conflicts:
   ```bash
   python -m venv venv
   venv\Scripts\activate
4. Install the required dependencies:
    pip install -r requirements.txt
5. Run the application:
    streamlit run app.py

## Usage
This application can be useful for students, content creators, and professionals who work with long video recordings. It helps quickly understand the core ideas of lectures, meetings, webinars, or presentations by generating a summarized version of the spoken content without watching the entire video.

## Future Improvements
Support live video stream summarization
Improve summary quality for longer videos
Add multilingual video summarization
Enhance the user interface and performance

## Learning Outcomes
Building this project helped me understand how multiple AI components—such as speech recognition and natural language processing—can be combined into a real-world application. It also taught me how to handle system constraints and dependency issues while maintaining the core objective of the project. Most importantly, the project reinforced that problem-solving and persistence are key skills when working with applied AI systems.

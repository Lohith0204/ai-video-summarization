import streamlit as st
import tempfile
import imageio_ffmpeg
import subprocess
from ai_engine.speech import transcribe_audio
from ai_engine.summarize import summarize_text

st.title("AI Video Summarizer")

uploaded_video = st.file_uploader("Upload a video file",type=["mp4", "mov", "avi"])

if uploaded_video is not None:
    st.video(uploaded_video)

    if st.button("Generate Summary"):
        with st.spinner("Processing video..."):

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
                temp_video.write(uploaded_video.read())
                video_path = temp_video.name

            audio_path = video_path.replace(".mp4", ".wav")

            ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

            subprocess.run([
                ffmpeg_path,
                "-i", video_path,
                "-ac", "1",
                "-ar", "16000",
                audio_path,
                "-y"
            ], check=True)

            text = transcribe_audio(audio_path)
            summary = summarize_text(text)

        st.success("Summary generated")
        st.subheader("Summary")
        st.write(summary)

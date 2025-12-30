import whisper
import soundfile as sf
import numpy as np

model = whisper.load_model("base")

def transcribe_audio(audio_path):
    audio, sample_rate = sf.read(audio_path)

    if len(audio.shape) > 1:
        audio = np.mean(audio, axis=1)

    audio = audio.astype(np.float32)

    if sample_rate != 16000:
        raise ValueError(
            f"Sample rate must be 16000 Hz, got {sample_rate}. "
            "Ensure audio extraction uses 16kHz."
        )

    result = model.transcribe(audio)
    return result["text"]

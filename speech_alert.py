import os
from gtts import gTTS


def speak_fault_alert(fault_type, voltage, current):
  """Generates an audio speech alert when a smart grid fault is detected."""
  try:
    # 1. Ensure the static folder exists FIRST before saving
    os.makedirs("static", exist_ok=True)

    # 2. Build the message
    message = (
        f"Warning! Smart grid fault detected. Type: {fault_type}."
        f" Voltage is {voltage} volts, and current is {current} amperes."
        " Please check the control panel immediately."
    )

    print(f"[SPEECH ALERT] Generating audio for: {message}")

    # 3. Generate speech using gTTS
    tts = gTTS(text=message, lang="en", slow=False)

    # 4. Save the audio file
    audio_path = "static/fault_alert.mp3"
    tts.save(audio_path)

    print(f"[SPEECH ALERT] Audio saved successfully to {audio_path}")
    return audio_path

  except Exception as e:
    print(f"[SPEECH ALERT ERROR]: {e}")
    return None


if __name__ == "__main__":
  # Test the function locally
  speak_fault_alert("Undervoltage", 170.0, 4.0)

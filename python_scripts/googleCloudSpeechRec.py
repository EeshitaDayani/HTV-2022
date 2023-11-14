# Imports the Google Cloud client library
from google.cloud import speech
import os
from python_scripts.var_mod import var
from python_scripts.helper import Helper
import time 

# set google api creds
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/perudayani/Downloads/steam-glass-365615-d823e4ed9dfc.json"

class SpeechRec():
    def transcribe_file(gcs_uri):
        """Transcribe the given audio file."""
        client = speech.SpeechClient()
        audio = speech.RecognitionAudio(uri=gcs_uri)

        if (var == 0):
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.FLAC.ENCODING_UNSPECIFIED,
                sample_rate_hertz=44100,
                language_code="en-US",
                audio_channel_count=2,
                enable_automatic_punctuation=True,
            )
        else:
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=48000,
                language_code="en-US",
                audio_channel_count=1,
                enable_automatic_punctuation=True,
            )

        operation = client.long_running_recognize(config=config, audio=audio)
        print("Transcribing audio file")

        time.sleep(7)

        print("Summarizing data")
        response = operation.result()

        Helper.make_resp_json(response.results)


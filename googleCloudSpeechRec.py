# Imports the Google Cloud client library
from google.cloud import speech
import json
import os
import var_mod

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/perudayani/Downloads/steam-glass-365615-d823e4ed9dfc.json"

class SpeechRec():
    def transcribe_file(gcs_uri):
        """Transcribe the given audio file."""
        client = speech.SpeechClient()
        audio = speech.RecognitionAudio(uri=gcs_uri)

        if (var_mod.var == 0):
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16.ENCODING_UNSPECIFIED,
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
        print("Waiting for operation to complete...")
        response = operation.result(timeout=90)
        make_json(response.results)

    if (var_mod.var == 0):
        gcs_uri = "gs://htv2022/audio-files/" + var_mod.rant[1]
    else:
        gcs_uri = "gs://htv2022/audio-files/" + var_mod.adver[1]


    transcribe_file(gcs_uri)


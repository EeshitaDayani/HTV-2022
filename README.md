# HTV-2022

## What it is
An NLP-based hack that helps therapy patients keep track of their mental state in between therapy sessions.

## What it does
OpenUp lets patients record audio files following an emotional/traumatic event. Based on the transcription, OpenUp analyzes the patient's state through emotion classification and sends a summarised transcription of the audio file to the therapist.

## How we built it
We used Google Cloud's speech-to-text API and Co:here's sentiment analysis and text summarization models to build our project.

## Challenges we ran into
Training the text summarization model was difficult because there was a lack of datasets focusing on mental health for text generation.

## What's next for OpenUp
Speech-to-text conversion and text summarization that works for multiple languages, and utilizing video for superior emotion analysis.

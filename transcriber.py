import assemblyai as aai

aai.settings.api_key = "4df5dcd55987438f8ed21eebfa500c45"

config = aai.TranscriptionConfig(speaker_labels=True)

transcriber = aai.Transcriber()

audio_file = ("./test.mp3")

transcript = transcriber.transcribe(audio_file, config)

if transcript.status == aai.TranscriptStatus.error:
    print("Transcription failed: ", transcript.error)
    exit(1)

print(transcript.text)

for utterance in transcript.utterances:
    print(f"Speaker {utterance.speaker}: {utterance.text}")
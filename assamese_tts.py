
import azure.cognitiveservices.speech as speechsdk
import os

from dotenv import load_dotenv

load_dotenv()
# Azure credentials
speech_key = os.getenv("SPEECH_KEY")
service_region = "eastus"

# Create Speech Config
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_config.speech_synthesis_voice_name = "as-IN-YashicaNeural"  # Assamese Female Voice

# Output file path
output_file = "assamese_tts_emotion.wav"
audio_config = speechsdk.audio.AudioOutputConfig(filename=output_file)

# SSML for Emotional Voice and Faster Speed
ssml = f"""


<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' 
       xmlns:mstts='http://www.w3.org/2001/mstts' xml:lang='as-IN'>
    <voice name='as-IN-YashicaNeural'>
        <mstts:express-as style='chat'>
            <prosody rate='17%' pitch='+6%'>
        ভাৰতএখনবিশাল,দেশ 
            </prosody>
        </mstts:express-as>
    </voice>
</speak>
"""

# Create Speech Synthesizer
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Convert SSML to speech and save
result = speech_synthesizer.speak_ssml_async(ssml).get()

# Check result
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print(f"✅ Emotional Speech saved as {output_file}")
else:
    print("❌ Speech synthesis failed.")
    cancellation_details = result.cancellation_details
    if cancellation_details:
        print("Reason:", cancellation_details.reason)
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details:", cancellation_details.error_details)

import sounddevice as sd
from scipy.io.wavfile import write
import time
import whisper
import joblib
from spotify_recommender import recommend_songs
import sys
import io

def record_audio(duration=10, sample_rate=16000):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"input_{timestamp}.wav"
    
    print("🔴 Kayıt başladı...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    write(filename, sample_rate, audio)
    print("✅ Kayıt tamamlandı:", filename)
    return filename

def transcribe_audio(filename):
    model = whisper.load_model("base")
    result = model.transcribe(filename, task="translate", language="Turkish")
    print("\n📄 İngilizce Çeviri Sonucu:")
    print(result["text"])
    return result["text"]

def predict_emotion(text):
    model = joblib.load("emotion_model.pkl")
    label_id = model.predict([text])[0]
    label_names = ["sadness", "joy", "love", "anger", "fear", "surprise"]
    label_name = label_names[label_id]
    print(f"\n💡 Tahmin edilen duygu: {label_id} - {label_name}")
    return label_id, label_name

if __name__ == "__main__":
    audio_file = record_audio()
    translated_text = transcribe_audio(audio_file)
    emotion_id, emotion_label = predict_emotion(translated_text)

    print("\n🎧 Spotify Şarkı Önerileri:")
    songs = recommend_songs(emotion_label)
    for s in songs:
        print(s)

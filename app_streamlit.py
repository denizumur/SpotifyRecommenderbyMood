import streamlit as st
import sounddevice as sd
from scipy.io.wavfile import write
import time
import whisper
import joblib
from spotify_recommender import recommend_songs
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

st.set_page_config(page_title="🎧 Ruh Haline Göre Spotify", page_icon="🎶", layout="centered")
st.markdown("<h1 style='text-align: center; color: #1DB954;'>🎧 Ruh Haline Göre Spotify</h1>", unsafe_allow_html=True)
st.markdown("## 🗣️ Mikrofonla konuş, ruh haline göre şarkı önerisi al!")

# Kayıt süresi seçimi
duration = st.slider("⏱️ Kayıt süresi (saniye)", min_value=3, max_value=15, value=5)

with st.expander("🎙️ Kayıt Animasyonu"):
    st.image("https://media.tenor.com/7QbMwdEyRLcAAAAM/mic-microphone.gif", use_column_width=True)

def record_audio_streamlit(duration=5, sample_rate=16000):
    filename = f"input_{time.strftime('%Y%m%d_%H%M%S')}.wav"
    st.info("🎙️ Kayıt başladı...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    write(filename, sample_rate, audio)
    st.success("✅ Kayıt tamamlandı!")
    return filename

def transcribe_audio(filename):
    model = whisper.load_model("base")
    result = model.transcribe(filename, task="translate", language="Turkish")
    return result["text"]

def predict_emotion(text):
    model = joblib.load("emotion_model.pkl")
    label_id = model.predict([text])[0]
    label_names = ["sadness", "joy", "love", "anger", "fear", "surprise"]
    return label_id, label_names[label_id]

if st.button("🎤 Kaydı Başlat ve Şarkı Öner"):
    file = record_audio_streamlit(duration)

    with st.spinner("🧠 İngilizce'ye çeviriliyor..."):
        text = transcribe_audio(file)
        st.write("📄 **İngilizce Çeviri:**", text)

    with st.spinner("💡 Duygu analiz ediliyor..."):
        emotion_id, emotion_label = predict_emotion(text)
        st.success(f"💬 Tahmin Edilen Duygu: `{emotion_label}`")

    with st.spinner("🎶 Spotify'dan şarkılar getiriliyor..."):
        songs = recommend_songs(emotion_label)
        st.markdown("### 🎵 Önerilen Şarkılar:")
        for s in songs:
            st.markdown(f"- {s}")

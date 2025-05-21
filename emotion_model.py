from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
print("✅  giris")
# Dataset'i yükle
dataset = load_dataset("dair-ai/emotion", split="train")
print("✅  Dataset'i yükle")

# Veri ve etiketleri ayır
texts = dataset['text']
labels = dataset['label']
print("✅  Veri ve etiketleri ayır")
# Eğitim/test ayırma
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Pipeline: TF-IDF + Naive Bayes
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)
print("✅  ipeline: TF-IDF + Naive Bayes")
# Performans kontrolü
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Modeli kaydet
joblib.dump(model, "emotion_model.pkl")
print("✅ Model kaydedildi: emotion_model.pkl")

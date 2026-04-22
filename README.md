# Kaggle Playground S3E16-🦀 Regression with a Crab Age Dataset
(Yengeç Yaşı Tahmin Uygulaması)

Bu proje, yengeçlerin fiziksel özelliklerini (ağırlık, boyut, kabuk ağırlığı vb.) kullanarak yaşlarını tahmin eden bir Makine Öğrenmesi uygulamasıdır. Model, Kaggle'daki "Crab Age Prediction" veri seti üzerinde eğitilmiştir.

## 🚀 Özellikler
- **Model:** Gradient Boosting Regressor (GBR)
- **Performans:** R² ~0.60, MAE ~1.26 yıl
- **Arayüz:** Streamlit ile interaktif web uygulaması
- **Dağıtım:** Hugging Face Spaces üzerinden canlı erişim

## 📊 Veri Analizi ve Model Süreci
- **Feature Engineering:** `Volume`, `Density`, `Shell_to_Total_Ratio` gibi biyolojik göstergeler türetilmiştir.
- **Data Preprocessing:** Aykırı değerler temizlenmiş ve hedef değişken `log1p` dönüşümü ile normalize edilmiştir.
- **Model Kayıt:** Eğitilen model `joblib` kütüphanesi ile paketlenmiştir.

## 💻 Yerel Kurulum (Local Setup)

Projeyi kendi bilgisayarınızda çalıştırmak için:

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/tugcenkrdnz/-Crab-Age-Prediction-.git

2. Kütüphaneleri Yükleyin

pip install -r requirements.txt

3. Uygulamayı çalıştırın

streamlit run app.py

# Kaggle Playground S3E16 -  🦀 Yengeç Yaşı Tahmin Uygulaması (Crab Age Prediction)

Bu proje, yengeçlerin fiziksel özelliklerini kullanarak yaşlarını tahmin eden, yüksek performanslı bir Makine Öğrenmesi uygulamasıdır. Model, Kaggle'daki "Crab Age Prediction" veri seti üzerinde Apple M4 mimarisi üzerinde optimize edilerek eğitilmiştir.

## 🚀 Özellikler
- **Model:** XGBoost Regressor (MAE Odaklı)
- **Performans:** **MAE ~1.36** (Kaggle Test Skoru)
- **Arayüz:** Streamlit ile interaktif kullanıcı deneyimi
- **Teknik:** Logaritmik hedef değişken dönüşümü (`log1p`) ve özellik mühendisliği.

## 📊 Veri Analizi ve Model Süreci
- **Genişletilmiş Özellik Mühendisliği (Feature Engineering):** Sadece ham verilerle yetinilmeyip, biyolojik anlam taşıyan 9 yeni öznitelik türetilmiştir:
    - `Volume`: Yengeç hacmi tahmini.
    - `Density`: Ağırlık/Hacim oranı.
    - `Meat_Yield`: Ayıklanmış et verimliliği oranı.
    - `Shell_Weight_Ratio`: Kabuk ağırlığının toplam ağırlığa oranı.
    - `Weight_Diff`: Kayıp ağırlık analizi.
    - `Dim_Sum`, `Shape_Index`, `Viscera_Ratio`, `Shell_to_Total`.
- **Veri Ön İşleme:** `Height == 0` gibi hatalı veriler temizlenmiş, kategorik `Sex` verisi One-Hot Encoding ile sayısallaştırılmıştır.
- **Sütun Hizalama (Feature Alignment):** Eğitim ve test aşamalarında sütun sıralamasının korunması için özel bir "Alignment" protokolü uygulanmıştır.

## 💻 Yerel Kurulum (Local Setup)

Projeyi kendi bilgisayarınızda çalıştırmak için:

1. **Depoyu klonlayın:**
   ```bash
   git clone https://github.com/tugcenkrdnz/-Crab-Age-Prediction-.git
   cd -Crab-Age-Prediction-
   ```

2. **Gerekli kütüphaneleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Uygulamayı çalıştırın:**
   ```bash
   streamlit run app.py
   ```

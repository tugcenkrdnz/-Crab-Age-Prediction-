import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 1. Sayfa Ayarları ve Başlık
st.set_page_config(page_title="Yengeç Yaşı Tahmini", page_icon="🦀")
st.title("🦀 Yengeç Yaşı Tahmini")
st.markdown("Fiziksel ölçümleri girerek yengecin yaşını tahmin edin.")

# 2. Modeli Yükleme
@st.cache_resource # Modelin her seferinde tekrar yüklenip uygulamayı yavaşlatmasını engeller
def load_model():
    return joblib.load('crab_age_xgb_model.pkl')

model = load_model()

# 3. Kullanıcı Girişleri (Sidebar/Kenar Çubuğu kullanarak ekranı ferahlatalım)
st.sidebar.header("Ölçüm Değerleri")

# Fiziksel Boyutlar
length = st.sidebar.slider("Boy (Length)", 0.0, 1.0, 0.5)
diameter = st.sidebar.slider("Çap (Diameter)", 0.0, 1.0, 0.4)
height = st.sidebar.slider("Yükseklik (Height)", 0.0, 0.5, 0.15)

# Ağırlıklar
weight = st.sidebar.number_input("Toplam Ağırlık (Weight)", 0.0, 5.0, 1.0)
shucked = st.sidebar.number_input("Ayıklanmış Ağırlık (Shucked Weight)", 0.0, 2.0, 0.5)
viscera = st.sidebar.number_input("Organ Ağırlığı (Viscera Weight)", 0.0, 1.0, 0.2)
shell = st.sidebar.number_input("Kabuk Ağırlığı (Shell Weight)", 0.0, 1.0, 0.3)

# Cinsiyet
sex = st.sidebar.selectbox("Cinsiyet", ["Erkek (M)", "Dişi (F)", "Bebek (I)"])

# 4. Tahmin Mantığı
if st.button("Yaşı Hesapla"):
    # Boş bir DataFrame oluştur (Modelin beklediği 19 sütun için)
    input_df = pd.DataFrame(0, index=[0], columns=model.feature_names_in_)
    
    # Mevcut verileri doldur
    input_df['Length'] = length
    input_df['Diameter'] = diameter
    input_df['Height'] = height
    input_df['Weight'] = weight
    input_df['Shucked Weight'] = shucked
    input_df['Viscera Weight'] = viscera
    input_df['Shell Weight'] = shell
    
    # Cinsiyet Encoding (One-Hot)
    if sex == "Erkek (M)": input_df['Sex_M'] = 1
    elif sex == "Dişi (F)": input_df['Sex_F'] = 1
    else: input_df['Sex_I'] = 1 # Bebek (I)

    # --- ÖZELLİK MÜHENDİSLİĞİ (Modelin 1.36 skoru için bunlar şart!) ---
    input_df['Volume'] = length * diameter * height
    input_df['Shell_Weight_Ratio'] = shell / (weight + 0.001)
    input_df['Meat_Yield'] = shucked / (weight + 0.001)
    input_df['Density'] = weight / (input_df['Volume'] + 0.001)
    input_df['Weight_Diff'] = weight - (shucked + viscera + shell)
    input_df['Dim_Sum'] = length + diameter + height
    input_df['Shell_to_Total'] = shell / (weight + 0.001)
    input_df['Shape_Index'] = length / (height + 0.001)
    input_df['Viscera_Ratio'] = viscera / (weight + 0.001)

    # 5. Tahmin ve Sonuç
    # Modelin beklediği sütun sırasıyla gönderiyoruz
    pred_log = model.predict(input_df)
    final_age = np.expm1(pred_log)[0]
    
    # Görsel Sonuç Paneli
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Tahmin Edilen Yaş", value=f"{final_age:.2f} Yıl")
    with col2:
        st.info(f"Hata Payı: ±1.36 Ay")

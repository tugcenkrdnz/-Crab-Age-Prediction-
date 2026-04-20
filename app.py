import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 1. Başlık ve Model Yükleme
st.title("🦀 Yengeç Yaşı Tahmini")
model = joblib.load('crab_age_model.pkl')

# 2. Kullanıcı Girişleri (En önemli 3 özellik)
shell = st.number_input("Kabuk Ağırlığı (Shell Weight)", 0.0, 1.0, 0.3)
weight = st.number_input("Toplam Ağırlık (Weight)", 0.0, 5.0, 1.0)
shucked = st.number_input("Ayıklanmış Ağırlık (Shucked Weight)", 0.0, 2.0, 0.5)

# 3. Tahmin Butonu ve Mantığı
if st.button("Tahmin Et"):
    # Modelin beklediği tüm sütunları (19 adet) 0 ile oluşturup sadece girişleri dolduruyoruz
    # Not: Modelin beklediği tam sütun listesini 'model.feature_names_in_' ile alıyoruz
    input_data = pd.DataFrame(0, index=[0], columns=model.feature_names_in_)
    input_data['Shell Weight'] = shell
    input_data['Weight'] = weight
    input_data['Shucked Weight'] = shucked
    
    # Hesaplanan özellikleri ekleyelim (Hata almamak için)
    input_data['Shell_to_Total'] = shell / (weight + 1e-9)
    
    # Tahmin (Log -> Gerçek Yaş)
    pred_log = model.predict(input_data)
    st.success(f"Tahmin Edilen Yaş: {np.expm1(pred_log)[0]:.2f}")
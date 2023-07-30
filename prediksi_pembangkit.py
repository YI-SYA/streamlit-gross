import pickle
import streamlit as st

model = pickle.load(open('prediksi_pembangkit.sav', 'rb'))

st.title('Prediksi Listrik Pembangkit')

coal_flow = st.number_input('Input Total Coal flow')
main_steam_press = st.number_input('Input Main Steam Pressure')
feedwater_flow = st.number_input('Input Total Feedwater Flow')
nilai_kalori = st.number_input('Input nilai kalori batubara')
air_flow = st.number_input('Input Total Air Flow')

predict = ''

if st.button('Estimasi Listrik'):
    predict = model.predict(
        [[coal_flow, main_steam_press, feedwater_flow, nilai_kalori, air_flow]]
    )
    st.write ('Besar listrik yang dihasilkan PLTU =', predict, 'MWH')
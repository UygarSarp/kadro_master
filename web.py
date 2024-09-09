import streamlit as st
import functions as fc

kadro = fc.dosya_ac()


def eklemec():
    yeni = st.session_state['abdu']+"\n"
    kadro.append(yeni)
    fc.dosya_yaz(kadro)


st.title("Kadro-Master")
st.subheader("Kadro-Master'a hoş geldiniz!")
st.write("Hayalinizdeki Kadroları oluşturmaya hazır mısınız?!")

for i,oyuncu in enumerate(kadro):
    buton = st.checkbox(oyuncu, key=oyuncu)
    if buton:
        kadro.pop(i)
        fc.dosya_yaz(kadro)
        del st.session_state[oyuncu]
        st.rerun()

st.text_input(label="",placeholder="Oyuncu ismini girin...",key='abdu',on_change=eklemec)
#Hacı bu eklemec in sonuna parantez koyunca neden error veriyor yav?

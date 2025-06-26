import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌐 Language Translator")

text = st.text_area("Enter text to translate")

langs = ['english', 'hindi', 'french', 'spanish', 'german', 'telugu', 'tamil']
source = st.selectbox("From Language", langs, index=0)
target = st.selectbox("To Language", langs, index=1)

if st.button("Translate"):
    if text.strip():
        translated = GoogleTranslator(source=source, target=target).translate(text)
        st.success("Translated Text:")
        st.write(translated)
    else:
        st.warning("Please enter text to translate.")

import tensorflow as tf
import tensorflow_text as tf_text
import streamlit as st

languageDetector = tf.saved_model.load('languageDetector')
EngAra = tf.saved_model.load('English_Arabic_Translator')
AraEng = tf.saved_model.load('Arabic_English_Translator')

def translate(text):
    translated_text = EngAra(text).numpy().decode()
    return translated_text

def main():
    st.title("Machine Translation API")
    text = st.text_input("Enter a sentence to translate", value="")
    if st.button("Translate"):
        language = languageDetector(text).numpy()[0].decode()
        translation = translate(text)
        
        st.success("Language:")
        st.write(language)
        
        st.success("Translation:")
        st.write(translation)

if __name__ == "__main__":
    main()
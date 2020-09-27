import warnings
warnings.filterwarnings('ignore')
import streamlit as st
from nltk.corpus import wordnet
import googletrans
from googletrans import Translator
import gtts
from playsound import playsound
import os
import pyttsx3
from pygame import mixer
from tempfile import TemporaryFile
st.set_option('deprecation.showfileUploaderEncoding', False)

def main():
    st.title("Dictionary Using NLTK")
    st.sidebar.title("Lets Check it out!!")

    choice=st.sidebar.selectbox("Choose an Option",("Meaning of The Word","Translator","About"),key="choice")

    if choice=="About":
        st.markdown("### Small Description of My Web Application...📙") 
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.write("Dictionary really helps to know the more words and at the same time we can understand the good effects of using the English words.")
        st.write(" Many people does not know how to use the words properly and they are lacking in these skills and always they will be behind other people, if we are not using them in a proper way.")
        st.write("With this web application I intend to find the meaning of the word along with its synonyms and antonyms.")
        st.write("This web application can also translate a short text or a document into the desired language the user desired along with oral recitation.")


    if choice=="Meaning of The Word":
        st.markdown("### Find the Meaning of a Word Along with its Synonyms and Antonyms.📙") 
        st.text(" ")
        st.text(" ")
        input = st.text_input("Enter The Word you want to find the meaning of:"," ")
        if input!=" ":
            try:
                syn=wordnet.synsets(input.lower())
                woi=syn[0]
                p=woi.definition()
                st.markdown("### Meaning:")
                st.write(p)

                try:
                    gre=str(syn[0].examples()[0])
                    if len(gre)!=0:
                        st.markdown("### Example..")
                        st.write(str(syn[0].examples()[0]))
                        st.text(" ")
                except:
                    pass

                syno = list()
                ant = list()
                for synset in syn:
                    for lemma in synset.lemmas():
                        syno.append(lemma.name())  
                        if lemma.antonyms():    
                            ant.append(lemma.antonyms()[0].name())

                y=set(syno)
                if len(y)!=0:
                    st.markdown("### Synonyms")
                    st.write(y)

                z=set(ant)
                if len(z)!=0:
                    st.markdown("### Antonyms")
                    st.write(z)

            except:
                st.markdown("### Sorry! We are not able to find the meaning of the word")

            
    if choice=="Translator":
        st.markdown("### Please Specify, Do You Want To Translate The Whole Document or a Single Line...")
        random=st.radio("Please Select",("Document","Couple of lines"),key="random")
        translator=Translator()

        if random=="Couple of lines":
            engine=pyttsx3.init()
            engine.setProperty('rate',100)
            st.text(" ")
            text=st.text_input("Please Enter The Sentence.."," ")
            if text!=" ":
                if st.checkbox("Clear the Output??"):
                        text=" "
            
            st.text(" ")
            a=list(googletrans.LANGUAGES.values())
            b=list(googletrans.LANGUAGES.keys())
        
            choose=st.selectbox("Please Select the Language you want to translate Your Sentence",a,key="choose")
            if text!=" ":
                dest=(b[a.index(choose)])
                result=translator.translate(text,dest=dest)
                st.text(" ")
                st.markdown("### Translated Sentence..")
                st.write(result.text) 
                try:
                    translator = Translator()
                    tts = gtts.gTTS(text=result.text,lang=dest)
                    mixer.init()
                    sf = TemporaryFile()
                    tts.write_to_fp(sf)
                    sf.seek(0)
                    mixer.music.load(sf)
                    mixer.music.play()
                except Exception:
                    pass

        if random=="Document":
            sure=''
            st.text(" ")
            st.markdown("### Please Select the Document with '.txt' extension..")
            file=st.file_uploader("Please Select the File",type=['txt','docx'])

            c=list(googletrans.LANGUAGES.values())
            v=list(googletrans.LANGUAGES.keys())

            if file:
                message=file.getvalue()
                if st.checkbox("Clear the Output??"):
                        sure="yes"

                choose=st.selectbox("Please Select the Language you want to translate Your Sentence",c,key="choose")
                if message!=" ":
                    dest=(v[c.index(choose)])
                    result=translator.translate(message,dest=dest)

                    if sure!="yes":
                        st.text(" ")
                        st.markdown("### Translated Sentence..")
                        st.write(result.text) 

                        if st.checkbox("Want to Listen the translated document.."):
                            try:
                                translator = Translator()
                                tts = gtts.gTTS(text=result.text,lang=dest)
                                mixer.init()
                                sf = TemporaryFile()
                                tts.write_to_fp(sf)
                                sf.seek(0)
                                mixer.music.load(sf)
                                mixer.music.play()
                            except Exception:
                                pass

if __name__=="__main__":
    main()
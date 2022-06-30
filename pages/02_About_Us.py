import requests
import streamlit as st
from streamlit_lottie import st_lottie


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_hello = load_lottieurl(
    "https://assets7.lottiefiles.com/packages/lf20_AMBEWz.json")
st_lottie(
    lottie_hello,
    reverse=False,
    quality="high",
    loop=True,
    height='200px',
    width=None,
    key=None,
)

st.markdown('''
###### We are a group of three (3) memebers who have done researched 
###### on the dibeties prediction using Machine Learning algorithm,
###### and have develop this website which helps us to know if we
###### are dibetic patient or not.
'''
            )

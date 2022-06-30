import streamlit as st
import requests
from streamlit_lottie import st_lottie


def main():
    st.markdown('''
    ---
    
    ''')
    st.title("What is Diabetes")
    st.markdown('''
    ---
    
    ''')
    hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_hello = load_lottieurl(
        "https://assets1.lottiefiles.com/packages/lf20_jmoaouad.json")
    st_lottie(
        lottie_hello,
        reverse=False,
        loop=True,
        height='350px',
        width=None,
        key=None,
    )
    st.markdown('''
             ###### Diabetes is noxious diseases in the world. Diabetes
             ###### caused because of obesity or high blood glucose level,
             ###### and so forth. It affects the hormone insulin, resulting
             ###### in abnormal metabolism of crabs and improves level of 
             ###### sugar in the blood. Diabetes2 occurs when body does not
             ###### make enough insulin. According to(WHO) World Health
             ###### Organization about 422 million people suffering from
             ###### diabetes particularly from low - or idle-income countries.
             ###### And this could be increased to 490 billion up to the year of 2030.
             ###### However, prevalence of diabetes is found among various Countries
             ###### like Canada, China, and India etc. Population of India is now
             ###### more than 100 million so the actual number of diabetics in
             ###### India is 40 million. Diabetes is major cause of death in the world''')


if __name__ == '__main__':
    main()

import login as auths
import streamlit as st
from streamlit_option_menu import option_menu

st.title("Diabetes Prediction")
st.subheader("Welcome Please Login or Create New Account")


bio = option_menu(menu_title=None,
                  options=['Login', 'Create New Account'],
                  icons=['house', 'flower1'],
                  default_index=0,
                  orientation="horizontal",
                  )
if bio == 'Login':
    auths.signIn()
if bio == 'Create New Account':
    auths.signUp()

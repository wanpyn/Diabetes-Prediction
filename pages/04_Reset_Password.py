import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
import pyrebase
import streamlit as st

# firebase
firebaseConfig = {
    'authDomain': "dibeties-prediction.firebaseapp.com",
    'apiKey': "AIzaSyBtFYvcXpxzwYtp1GJIzgNVF7NtHT3Kohg",
    'authDomain': "dibeties-prediction.firebaseapp.com",
    'databaseURL': "https://dibeties-prediction-default-rtdb.asia-southeast2.firebasedatabase.app",
    'projectId': "dibeties-prediction",
    'storageBucket': "dibeties-prediction.appspot.com",
    'messagingSenderId': "443974944524",
    'appId': "1:443974944524:web:0b32dbb48e520cf634eb29",
    'measurementId': "G-08VMX64HLR"
}
# initialization of firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    default_app = firebase_admin.initialize_app(cred)
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

st.header("Enter your Email to reset your password")
email = st.text_input("Email")
submit = st.button("Reset Password")
if submit:
    auth.send_password_reset_email(email)

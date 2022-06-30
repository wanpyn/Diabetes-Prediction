import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import firestore
import pyrebase
import streamlit as st
import RanDeciSVM as RF
import re
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
db = firestore.client()


def signIn():
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    log = st.checkbox('Login')
    if log:
        checks(email)
        passwordField(password)
        try:
            if (email != "" and password != ""):
                auth.sign_in_with_email_and_password(email, password)
                RF.RDS()
        except:
            error = RuntimeError("Invalid Email or Password")
            st.exception(error)       
#for signIn
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def checks(email): 
    if(email == ""):
        st.error("Email Field cannot be empty")
def passwordField(password):
    if password == "":
        st.error("Password Field cannot be empty")

#for signUp
def check(email): 
    if(re.fullmatch(regex, email)):
        pass
    elif email == "":
        st.error("Email Field cannot be empty")
    else:
        st.error("Invalid Email Format")

def usernameField(username):
    if username == "":
        st.error("Username Field cannot be empty")
    else:
        pass

def PhoneField(phoneNumber,phone):
    if phoneNumber == "":
        st.error(" PhoneNumber Field cannot be empty")
    elif phone >= 11:
        st.error("PhoneNumber must be 10 numbers")
    else:
        pass


def passField(password, passw):
    if password == "":
        st.error("Password Field cannot be empty")
    elif passw > 6:
        pass
    else:
        st.error("Password Field should be more than 6 characters")

def signUp():
    with st.form("my_form"):
        email = st.text_input("Email")
        username = st.text_input("User Name")
        phoneNumber = st.text_input("Phone Number")
        phone = len(phoneNumber)
        password = st.text_input("New password", type="password")
        passw = len(password)
        conforimPass = st.text_input(
            "Confirm Password", type="password")
        # firebase
        data = {'Email': email, 'username': username,
                'Phone Number': phoneNumber}
        suBMIt = st.form_submit_button("Create Account")
        if suBMIt:
            try:
                check(email)
                usernameField(username)
                PhoneField(phoneNumber,phone)
                passField(password, passw)
                if email != "" and username!="" and phoneNumber != "" and password != "":
                    if conforimPass == password:
                        user = auth.create_user_with_email_and_password(
                        email, password)
                        db.collection('Users').document(email).set(data)
                        # db.collection('Users').document().set(data)
                        st.success("Your Account is created successfully!!! Please Login")
                        st.balloons()
                    else:
                        st.error("Password do not maatch!!! Try Again")   
            except:
                error = RuntimeError("Email already exist")
                st.exception(error)

        
        
# Import statements
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
import streamlit as st
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import altair as alt


def RDS():
    classifier_name = st.sidebar.selectbox(
        "Select classifier", ("Random_Forest", "Decision_Tree", "SVM"))

    def add_parameter_ui(clf_name):
        # params=dict()
        if clf_name == "Random_Forest":
            st.balloons()
            df = pd.read_csv("diabetes.csv")

            # HEADINGS
            st.title('Diabetes Checkup using RANDOM FOREST')
            st.sidebar.header('Patient Data')
            st.subheader('Training Data Stats')
            st.write(df.head(10))
            st.subheader('Shape of the dataset')
            st.write(df.shape)

            # X AND Y DATA
            x = df.drop(['Outcome'], axis=1)
            y = df.iloc[:, -1]
            x_train, x_test, y_train, y_test = train_test_split(
                x, y, test_size=0.2, random_state=0)

            # FUNCTION

            def user_report():
                Pregnancies = st.sidebar.slider('Pregnancies', 0, 17, 3)
                global Glucose
                Glucose = st.sidebar.slider('Glucose', 0, 200, 120)
                global BloodPressure
                BloodPressure = st.sidebar.slider('Blood Pressure', 0, 200, 60)
                SkinThickness = st.sidebar.slider('Skin Thickness', 0, 100, 20)
                global insulin
                insulin = st.sidebar.slider('Insulin', 0, 846, 79)
                global BMI
                BMI = st.sidebar.slider('BMI', 0, 67, 20)
                DiabetesPedigreeFunction = st.sidebar.slider(
                    'Diabetes Pedigree Function', 0.0, 2.4, 0.47)
                global Age
                Age = st.sidebar.slider('Age', 21, 88, 33)

                # global Date
                # Date=st.date_input('Todays date')

                user_report_data = {
                    'Pregnancies': Pregnancies,
                    'Glucose': Glucose,
                    'BloodPressure': BloodPressure,
                    'SkinThickness': SkinThickness,
                    'insulin': insulin,
                    'BMI': BMI,
                    'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
                    'Age': Age,

                    # 'Date':Date,

                }
                report_data = pd.DataFrame(user_report_data, index=[0])
                return report_data

            # PATIENT DATA
            user_data = user_report()
            st.subheader('Patient Data')
            st.write(user_data)

            # MODEL
            rfc = RandomForestClassifier()
            rfc.fit(x_train, y_train)
            user_result = rfc.predict(user_data)

            # COLOR FUNCTION
            if user_result[0] == 0:
                color = 'blue'
            else:
                color = 'red'

            # OUTPUT
            st.subheader('Your Report: ')
            output = ''
            if user_result[0] == 0:
                output = 'You are not Diabetic'
            else:
                output = 'You are Diabetic'
            st.title(output)
            st.subheader('Accuracy: ')
            st.write(str(accuracy_score(y_test, rfc.predict(x_test))*100)+'%')

            # VISUALISATIONS
            st.title('Visualised Patient Report')

            # insulin
            st.subheader("Insulin")
            energy_source = pd.DataFrame({
                "Insulin": ["Above_Average", "Control", "Low"],
                "Insulin_Level":  [200, 70, 70],

            })

            domain = ["Above_Average", "Control", "Low"]
            range_ = ["red", "green", "yellow"]

            bar_chart = alt.Chart(energy_source).mark_bar().encode(
                x="Today:O",
                y="Insulin_Level:Q",
                color=alt.Color("Insulin", scale=alt.Scale(
                    domain=domain, range=range_))
            )
            st.altair_chart(bar_chart, use_container_width=True)

            if insulin > 140:
                st.write("Your insulin level is  very high : ", insulin)
            elif insulin <= 140 or insulin >= 60:
                st.write("Your insulin level is normal : ", insulin)
            else:
                st.write("Your insulin level is very low : ", insulin)

            # Glucose
            st.subheader("Glucose")
            energy_source = pd.DataFrame({
                "Glucose": ["Above_Average", "Control", "Low"],
                "Glucose_Level":  [200, 70, 70],
                # "Date": [Date,Date,Date]
            })

            domain = ["Above_Average", "Control", "Low"]
            range_ = ["red", "green", "yellow"]
            bar_chart = alt.Chart(energy_source).mark_bar().encode(
                x="Today:O",
                y="Glucose_Level:Q",
                color=alt.Color("Glucose", scale=alt.Scale(
                    domain=domain, range=range_))
            )

            st.altair_chart(bar_chart, use_container_width=True)
            if Glucose > 140:
                st.write("Your Glucose level is  very high : ", Glucose)
            elif Glucose <= 140 or Glucose >= 60:
                st.write("Your Glucose level is normal : ", Glucose)
            else:
                st.write("Your Glucose level is very low : ", Glucose)

    # blood_pressure

            st.subheader("BLOOD PRESSURE")
            energy_source = pd.DataFrame({
                "BloodPressure": ["Above_Average", "Control", "Low"],
                "Blood_Pressure_Level":  [7, 6, 18.5],
                # "Date": [Date,Date,Date]
            })

            domain = ["Above_Average", "Control", "Low"]
            range_ = ["red", "green", "yellow"]
            bar_chart = alt.Chart(energy_source).mark_bar().encode(
                x="Today:O",
                y="Blood_Pressure_Level:Q",
                color=alt.Color("BloodPressure", scale=alt.Scale(
                    domain=domain, range=range_))
            )

            st.altair_chart(bar_chart, use_container_width=True)
            st.write('Blood pressure categories')
            st.caption('18-39 years-----------------119/70 mm Hg')
            st.caption('40-59 years-----------------124/77 mm Hg')
            st.caption('60+ years-------------------133/69 mm Hg')

    #60+ years
            if BloodPressure > 133 and Age > 60:
                st.write(
                    "Your blood pressure level is high according to your Age : ", BloodPressure)
            elif BloodPressure <= 133 and BloodPressure >= 69 and Age > 60:
                st.write(
                    "Your blood pressure level is normal according to your Age : ", BloodPressure)
            elif BloodPressure < 69 and Age > 60:
                st.write(
                    "Your blood pressure level is low according to your Age : ", BloodPressure)

    # 18-39 years
            elif BloodPressure > 119 and Age > 18 and Age <= 39:
                st.write(
                    "Your blood pressure level is high  according to your Age : ", BloodPressure)
            elif BloodPressure <= 119 and BloodPressure > 70 and Age > 18 and Age <= 39:
                st.write(
                    "Your blood pressure level is normal according to your Age : ", BloodPressure)
            elif BloodPressure < 70 and Age > 18 and Age <= 39:
                st.write(
                    "Your blood pressure level is low according to your Age : ", BloodPressure)
    # 40-59 years
            elif BloodPressure > 124 and Age >= 40 and Age <= 59:
                st.write(
                    "Your blood pressure level is high  according to your Age : ", BloodPressure)
            elif BloodPressure <= 124 and BloodPressure >= 77 and Age >= 40 and Age <= 59:
                st.write(
                    "Your blood pressure level is normal  according to your Age : ", BloodPressure)
            elif BloodPressure < 77 and Age >= 40 and Age <= 59:
                st.write(
                    "Your blood pressure level is low  according to your Age : ", BloodPressure)

            # BMI
            st.subheader("BMI")
            energy_source = pd.DataFrame({
                "BMI": ["Above_Average", "Control", "Low"],
                "BMI_Level":  [7, 6, 18.5],
                # "Date": [Date,Date,Date]
            })

            domain = ["Above_Average", "Control", "Low"]
            range_ = ["red", "green", "yellow"]
            bar_chart = alt.Chart(energy_source).mark_bar().encode(
                x="Today:O",
                y="BMI_Level:Q",
                color=alt.Color("BMI", scale=alt.Scale(
                    domain=domain, range=range_))
            )

            st.altair_chart(bar_chart, use_container_width=True)
            st.write('BMI categories')
            st.caption('Underweight = <18.5')
            st.caption('Normal weight = 18.5–24.9')
            st.caption('Overweight = 25–29.9')

            if BMI < 18.4:
                st.write("You are underweight : ", BMI)
            elif BMI <= 24.9 and BMI >= 18.5:
                st.write("Your weight is normal : ", BMI)
            elif BMI > 26:
                st.write("You are overweight : ", BMI)
            else:
                exit()

    # _____________________________decision tree____________________________
        elif clf_name == "Decision_Tree":
            df = pd.read_csv("diabetes.csv")
            st.balloons()
            # HEADINGS
            st.title('Diabetes Checkup using DECISION TREE')
            st.sidebar.header('Patient Data')
            st.subheader('Training Data Stats')
            st.write(df.head(10))
            st.subheader('Shape of the dataset')
            st.write(df.shape)

            # X AND Y DATA
            x = df.drop(['Outcome'], axis=1)
            y = df.iloc[:, -1]
            x_train, x_test, y_train, y_test = train_test_split(
                x, y, test_size=0.2, random_state=0)

            # FUNCTION

            def user_report():
                Pregnancies = st.sidebar.slider('Pregnancies', 0, 17, 3)
                global Glucose
                Glucose = st.sidebar.slider('Glucose', 0, 200, 120)
                global BloodPressure
                BloodPressure = st.sidebar.slider('Blood Pressure', 0, 200, 60)
                SkinThickness = st.sidebar.slider('Skin Thickness', 0, 100, 20)
                global insulin
                insulin = st.sidebar.slider('Insulin', 0, 846, 79)
                global BMI
                BMI = st.sidebar.slider('BMI', 0, 67, 20)
                DiabetesPedigreeFunction = st.sidebar.slider(
                    'Diabetes Pedigree Function', 0.0, 2.4, 0.47)
                global Age
                Age = st.sidebar.slider('Age', 21, 88, 33)

                # global Date
                # Date=st.date_input('Todays date')

                user_report_data = {
                    'Pregnancies': Pregnancies,
                    'Glucose': Glucose,
                    'BloodPressure': BloodPressure,
                    'SkinThickness': SkinThickness,
                    'insulin': insulin,
                    'BMI': BMI,
                    'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
                    'Age': Age,

                    # 'Date':Date,

                }
                report_data = pd.DataFrame(user_report_data, index=[0])
                return report_data

            # PATIENT DATA
            user_data = user_report()
            st.subheader('Patient Data')
            st.write(user_data)

            # MODEL
            dtree = DecisionTreeClassifier()
            dtree.fit(x_train, y_train)
            user_result = dtree.predict(user_data)

            # COLOR FUNCTION
            if user_result[0] == 0:
                color = 'blue'
            else:
                color = 'red'

            # OUTPUT
            st.subheader('Your Report: ')
            output = ''
            if user_result[0] == 0:
                output = 'You are not Diabetic'
            else:
                output = 'You are Diabetic'
            st.title(output)
            st.subheader('Accuracy: ')
            st.write(str(accuracy_score(y_test, dtree.predict(x_test))*100)+'%')

            # VISUALISATIONS
            st.title('Visualised Patient Report')

            # insulin
            st.subheader("Insulin")
            energy_source = pd.DataFrame({
                "Insulin": ["Above_Average", "Control", "Low"],
                "Insulin_Level":  [200, 70, 70],

            })

            domain = ["Above_Average", "Control", "Low"]
            range_ = ["red", "green", "yellow"]

            bar_chart = alt.Chart(energy_source).mark_bar().encode(
                x="Today:O",
                y="Insulin_Level:Q",
                color=alt.Color("Insulin", scale=alt.Scale(
                    domain=domain, range=range_))
            )
            st.altair_chart(bar_chart, use_container_width=True)

            if insulin > 140:
                st.write("Your insulin level is  very high : ", insulin)
            elif insulin <= 140 or insulin >= 60:
                st.write("Your insulin level is normal : ", insulin)
            else:
                st.write("Your insulin level is very low : ", insulin)

            # Glucose
            st.subheader("Glucose")
            energy_source = pd.DataFrame({
                "Glucose": ["Above_Average", "Control", "Low"],
                "Glucose_Level":  [200, 70, 70],
                # "Date": [Date,Date,Date]
            })

            domain = ["Above_Average", "Control", "Low"]
            range_ = ["red", "green", "yellow", ]
            bar_chart = alt.Chart(energy_source).mark_bar().encode(
                x="Today:O",
                y="Glucose_Level:Q",
                color=alt.Color("Glucose", scale=alt.Scale(
                    domain=domain, range=range_))
            )

            st.altair_chart(bar_chart, use_container_width=True)
            if Glucose > 140:
                st.write("Your Glucose level is  very high : ", Glucose)
            elif Glucose <= 140 or Glucose >= 60:
                st.write("Your Glucose level is normal : ", Glucose)
            else:
                st.write("Your Glucose level is very low : ", Glucose)

    # blood_pressure

            st.subheader("BLOOD PRESSURE")
            energy_source = pd.DataFrame({
                "BloodPressure": ["Above_Average", "Control", "Low"],
                "Blood_Pressure_Level":  [7, 6, 18.5],
                # "Date": [Date,Date,Date]
            })

            domain = ["Above_Average", "Control", "Low"]
            range_ = ["red", "green", "yellow"]
            bar_chart = alt.Chart(energy_source).mark_bar().encode(
                x="Today:O",
                y="Blood_Pressure_Level:Q",
                color=alt.Color("BloodPressure", scale=alt.Scale(
                    domain=domain, range=range_))
            )

            st.altair_chart(bar_chart, use_container_width=True)
            st.write('Blood pressure categories')
            st.caption('18-39 years--------------------119/70 mm Hg')
            st.caption('40-59 years--------------------124/77 mm Hg')
            st.caption('60+ years----------------------133/69 mm Hg')

    #60+ years
            if BloodPressure > 133 and Age > 60:
                st.write(
                    "Your blood pressure level is high according to your Age : ", BloodPressure)
            elif BloodPressure <= 133 and BloodPressure >= 69 and Age > 60:
                st.write(
                    "Your blood pressure level is normal according to your Age : ", BloodPressure)
            elif BloodPressure < 69 and Age > 60:
                st.write(
                    "Your blood pressure level is low according to your Age : ", BloodPressure)

    # 18-39 years
            elif BloodPressure > 119 and Age > 18 and Age <= 39:
                st.write(
                    "Your blood pressure level is high  according to your Age : ", BloodPressure)
            elif BloodPressure <= 119 and BloodPressure > 70 and Age > 18 and Age <= 39:
                st.write(
                    "Your blood pressure level is normal according to your Age : ", BloodPressure)
            elif BloodPressure < 70 and Age > 18 and Age <= 39:
                st.write(
                    "Your blood pressure level is low according to your Age : ", BloodPressure)
    # 40-59 years
            elif BloodPressure > 124 and Age >= 40 and Age <= 59:
                st.write(
                    "Your blood pressure level is high  according to your Age : ", BloodPressure)
            elif BloodPressure <= 124 and BloodPressure >= 77 and Age >= 40 and Age <= 59:
                st.write(
                    "Your blood pressure level is normal  according to your Age : ", BloodPressure)
            elif BloodPressure < 77 and Age >= 40 and Age <= 59:
                st.write(
                    "Your blood pressure level is low  according to your Age : ", BloodPressure)

            # BMI
            st.subheader("BMI")
            energy_source = pd.DataFrame({
                "BMI": ["Above_Average", "Control", "Low"],
                "BMI_Level":  [7, 6, 18.5],
                # "Date": [Date,Date,Date]
            })

            domain = ["Above_Average", "Control", "Low"]
            range_ = ["red", "green", "yellow"]
            bar_chart = alt.Chart(energy_source).mark_bar().encode(
                x="Today:O",
                y="BMI_Level:Q",
                color=alt.Color("BMI", scale=alt.Scale(
                    domain=domain, range=range_))
            )

            st.altair_chart(bar_chart, use_container_width=True)
            st.write('BMI categories')
            st.caption('Underweight = <18.5')
            st.caption('Normal weight = 18.5–24.9')
            st.caption('Overweight = 25–29.9')

            if BMI < 18.4:
                st.write("You are underweight : ", BMI)
            elif BMI <= 24.9 and BMI >= 18.5:
                st.write("Your weight is normal : ", BMI)
            elif BMI > 26:
                st.write("You are overweight : ", BMI)

        # params=dict()
        elif clf_name == "SVM":
            st.balloons()
            df = pd.read_csv("diabetes.csv")

            # HEADINGS
            st.title('Diabetes Checkup using RANDOM FOREST')
            st.sidebar.header('Patient Data')
            st.subheader('Training Data Stats')
            st.write(df.head(10))
            st.subheader('Shape of the dataset')
            st.write(df.shape)

            # X AND Y DATA
            x = df.drop(['Outcome'], axis=1)
            y = df.iloc[:, -1]
            x_train, x_test, y_train, y_test = train_test_split(
                x, y, test_size=0.2, random_state=0)

            # FUNCTION

            def user_report():
                Pregnancies = st.sidebar.slider('Pregnancies', 0, 17, 3)
                global Glucose
                Glucose = st.sidebar.slider('Glucose', 0, 200, 120)
                global BloodPressure
                BloodPressure = st.sidebar.slider('Blood Pressure', 0, 200, 60)
                SkinThickness = st.sidebar.slider('Skin Thickness', 0, 100, 20)
                global insulin
                insulin = st.sidebar.slider('Insulin', 0, 846, 79)
                global BMI
                BMI = st.sidebar.slider('BMI', 0, 67, 20)
                DiabetesPedigreeFunction = st.sidebar.slider(
                    'Diabetes Pedigree Function', 0.0, 2.4, 0.47)
                global Age
                Age = st.sidebar.slider('Age', 21, 88, 33)

                # global Date
                # Date=st.date_input('Todays date')

                user_report_data = {
                    'Pregnancies': Pregnancies,
                    'Glucose': Glucose,
                    'BloodPressure': BloodPressure,
                    'SkinThickness': SkinThickness,
                    'insulin': insulin,
                    'BMI': BMI,
                    'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
                    'Age': Age,

                    # 'Date':Date,

                }
                report_data = pd.DataFrame(user_report_data, index=[0])
                return report_data

            # PATIENT DATA
            user_data = user_report()
            st.subheader('Patient Data')
            st.write(user_data)

            # MODEL
            svc = SVC()
            svc.fit(x_train, y_train)
            user_result = svc.predict(user_data)

            # COLOR FUNCTION
            if user_result[0] == 0:
                color = 'blue'
            else:
                color = 'red'

            # OUTPUT
            st.subheader('Your Report: ')
            output = ''
            if user_result[0] == 0:
                output = 'You are not Diabetic'
            else:
                output = 'You are Diabetic'
            st.title(output)

            # #Type1 or Type2
            # if insulin>18:
            #   st.write("You have Type 2 Diabetes")
            # else:
            #   st.write("You have Type 1 Diabetes")
            st.subheader('Accuracy: ')
            st.write(str(accuracy_score(y_test, svc.predict(x_test))*100)+'%')

            # VISUALISATIONS
            st.title('Visualised Patient Report')

            # insulin
            st.subheader("Insulin")
            energy_source = pd.DataFrame({
                "Insulin": ["Above_Average", "Control", "Low"],
                "Insulin_Level":  [200, 70, 70],

            })

            domain = ["Above_Average", "Control", "Low"]
            range_ = ["red", "green", "yellow"]

            bar_chart = alt.Chart(energy_source).mark_bar().encode(
                x="Today:O",
                y="Insulin_Level:Q",
                color=alt.Color("Insulin", scale=alt.Scale(
                    domain=domain, range=range_))
            )
            st.altair_chart(bar_chart, use_container_width=True)

            if insulin > 140:
                st.write("Your insulin level is  very high : ", insulin)
            elif insulin <= 140 or insulin >= 60:
                st.write("Your insulin level is normal : ", insulin)
            else:
                st.write("Your insulin level is very low : ", insulin)

            # Glucose
            st.subheader("Glucose")
            energy_source = pd.DataFrame({
                "Glucose": ["Above_Average", "Control", "Low"],
                "Glucose_Level":  [200, 70, 70],
                # "Date": [Date,Date,Date]
            })

            domain = ["Above_Average", "Control", "Low"]
            range_ = ["red", "green", "yellow"]
            bar_chart = alt.Chart(energy_source).mark_bar().encode(
                x="Today:O",
                y="Glucose_Level:Q",
                color=alt.Color("Glucose", scale=alt.Scale(
                    domain=domain, range=range_))
            )

            st.altair_chart(bar_chart, use_container_width=True)
            if Glucose > 140:
                st.write("Your Glucose level is  very high : ", Glucose)
            elif Glucose <= 140 or Glucose >= 60:
                st.write("Your Glucose level is normal : ", Glucose)
            else:
                st.write("Your Glucose level is very low : ", Glucose)

    # blood_pressure

            st.subheader("BLOOD PRESSURE")
            energy_source = pd.DataFrame({
                "BloodPressure": ["Above_Average", "Control", "Low"],
                "Blood_Pressure_Level":  [7, 6, 18.5],
                # "Date": [Date,Date,Date]
            })

            domain = ["Above_Average", "Control", "Low"]
            range_ = ["red", "green", "yellow"]
            bar_chart = alt.Chart(energy_source).mark_bar().encode(
                x="Today:O",
                y="Blood_Pressure_Level:Q",
                color=alt.Color("BloodPressure", scale=alt.Scale(
                    domain=domain, range=range_))
            )

            st.altair_chart(bar_chart, use_container_width=True)
            st.write('Blood pressure categories')
            st.caption('18-39 years-----------------119/70 mm Hg')
            st.caption('40-59 years-----------------124/77 mm Hg')
            st.caption('60+ years-------------------133/69 mm Hg')

    #60+ years
            if BloodPressure > 133 and Age > 60:
                st.write(
                    "Your blood pressure level is high according to your Age : ", BloodPressure)
            elif BloodPressure <= 133 and BloodPressure >= 69 and Age > 60:
                st.write(
                    "Your blood pressure level is normal according to your Age : ", BloodPressure)
            elif BloodPressure < 69 and Age > 60:
                st.write(
                    "Your blood pressure level is low according to your Age : ", BloodPressure)

    # 18-39 years
            elif BloodPressure > 119 and Age > 18 and Age <= 39:
                st.write(
                    "Your blood pressure level is high  according to your Age : ", BloodPressure)
            elif BloodPressure <= 119 and BloodPressure > 70 and Age > 18 and Age <= 39:
                st.write(
                    "Your blood pressure level is normal according to your Age : ", BloodPressure)
            elif BloodPressure < 70 and Age > 18 and Age <= 39:
                st.write(
                    "Your blood pressure level is low according to your Age : ", BloodPressure)
    # 40-59 years
            elif BloodPressure > 124 and Age >= 40 and Age <= 59:
                st.write(
                    "Your blood pressure level is high  according to your Age : ", BloodPressure)
            elif BloodPressure <= 124 and BloodPressure >= 77 and Age >= 40 and Age <= 59:
                st.write(
                    "Your blood pressure level is normal  according to your Age : ", BloodPressure)
            elif BloodPressure < 77 and Age >= 40 and Age <= 59:
                st.write(
                    "Your blood pressure level is low  according to your Age : ", BloodPressure)

            # BMI
            st.subheader("BMI")
            energy_source = pd.DataFrame({
                "BMI": ["Above_Average", "Control", "Low"],
                "BMI_Level":  [7, 6, 18.5],
                # "Date": [Date,Date,Date]
            })

            domain = ["Above_Average", "Control", "Low"]
            range_ = ["red", "green", "yellow"]
            bar_chart = alt.Chart(energy_source).mark_bar().encode(
                x="Today:O",
                y="BMI_Level:Q",
                color=alt.Color("BMI", scale=alt.Scale(
                    domain=domain, range=range_))
            )

            st.altair_chart(bar_chart, use_container_width=True)
            st.write('BMI categories')
            st.caption('Underweight = <18.5')
            st.caption('Normal weight = 18.5–24.9')
            st.caption('Overweight = 25–29.9')

            if BMI < 18.4:
                st.write("You are underweight : ", BMI)
            elif BMI <= 24.9 and BMI >= 18.5:
                st.write("Your weight is normal : ", BMI)
            elif BMI > 26:
                st.write("You are overweight : ", BMI)
            else:
                exit()

    add_parameter_ui(classifier_name)

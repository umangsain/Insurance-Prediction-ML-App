import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
import streamlit as st
# this stremlit is for web based application project

# Web Page Code
st.title("HEALTH INSURANCE PREDICTION")
img_url = "https://www.google.com/imgres?q=health%20insurance&imgurl=https%3A%2F%2Fwww.fundsindia.com%2Fblog%2Fwp-content%2Fuploads%2F2014%2F07%2Fhealth_insurance.jpg&imgrefurl=https%3A%2F%2Ffundsindia.com%2Fblog%2Fpersonal-finance%2Fseven-secrets-to-choose-the-best-health-insurance-plan%2F5649&docid=eMxRwHovuGfqRM&tbnid=UXgBZd1nRWTJHM&vet=12ahUKEwicrcWdgvCWAxUuRmwGHU3RGjsQnPAOegUI3wEQAA..i&w=550&h=465&hcb=2&ved=2ahUKEwicrcWdgvCWAxUuRmwGHU3RGjsQnPAOegUI3wEQAA"
st.img(img_url)

# Load Data and ML MODEL PART 
url = "https://raw.githubusercontent.com/ankitmisk/UIT-data/refs/heads/main/Insurance.csv"
df = pd.read_csv(url)
df.drop("Customer_ID", axis = 1, inplace=True)
df['Previous_Insurance'] = df['Previous_Insurance'].map({'Yes':1, 'No':0})
df['Insurance_Bought'] = df['Insurance_Bought'].map({'Yes':1, 'No':0})
X = df.iloc[:,:-1]
y = df.iloc[:,-1]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3)
model = LogisticRegression()
model.fit(X_train, y_train)

# show data sample
st.write(df.head())
# Create Side bar for user input form
st.sidebar.title("Fill Customer Details")
st.sidebar.image(img_url)

for index, col_name in enumerate(X.columns):
  min_v = X[col_name].min()
  max_v = X[col_name].max()
  if col_name != "Previous_Insurance":
    value = st.sidebar.slider(f"Select value for {col_name}",
                              min_value = min_y,
                              max_value = max_y)
  else:
    value = st.sidebar.number_input(f"Select value for {col_name} (0:No, 1: yes): ")

all_ans.append(value)

ud = {j:all_ans[i] for i,j in enumerate(X.columns)}
user_df = pd.DataFrame(ud, index = [1])
st.write(user_df)

#============================Prediction================

if st.button("Click to Predict: "):
    with st.spinner("Predicting.."):
        import time
        time.sleep(2)

    final_ans = model.predict([all_ans])[0]

    if final_ans == 0:
        st.info("❌Customer will not Buy the Insurance❌")
    else:
        st.success("✅Customer will buy the Insurance✅") 

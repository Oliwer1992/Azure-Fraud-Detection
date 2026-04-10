import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="🏦",
    layout="centered"
)



@st.cache_resource
def load_model():
    return joblib.load("Fraud-LGBMClassifier.pkl")

model = load_model()

st.title("Fraud Prediction")
st.caption("Fill in the customer details below to assess their fraud risk.")


st.subheader("")
transaction_mapping = {0: "CASH_OUT", 1: "TRANSFER"}
type_val = st.selectbox("Type of transaction",
                      options=[0,1],
                       format_func = lambda x: transaction_mapping[x])
step = st.number_input('Step (hour of month)', min_value=1, max_value=744, value=1)
destTransactionCount = st.number_input("Number of past transactions with the recipient", min_value=0, value=0)


amount = st.number_input('Amount of transaction', min_value=0.0, value=1000.0)
odlbalanceOrg = st.number_input("Sender Balance (Before)", min_value=0.0, value=1000.0)
newbalanceOrig = st.number_input("Sender Balance (After)", min_value=0.0, value=1000.0)
oldbalanceDest = st.number_input("Receiver Balance (Before)", min_value=0.0, value=1000.0)
newbalanceDest = st.number_input("Receiver Balance (After)", min_value=0.0, value=1000.0)





st.divider()
if st.button("Check transaction"):
    errorBalanceOrig = (odlbalanceOrg  - amount ) - newbalanceOrig
    errorBalanceDest = (oldbalanceDest  + amount) - newbalanceDest
    hour_of_day = step % 24 
    day_of_week = (step // 24) % 7
    accountDrained = 1 if (newbalanceOrig == 0) and amount > 0 else 0
    isHighAmount = 1 if amount > 954997.47 else 0

    
    data = {
        'type': type_val,
        'amount': amount,
        'odlbalanceOrg': odlbalanceOrg,
        'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest,
        'newbalanceDest': newbalanceDest,
        'errorBalanceOrig': errorBalanceOrig,
        'errorBalanceDest': errorBalanceDest,
        'hour_of_day': hour_of_day,
        'day_of_week': day_of_week,
        'accountDrained': accountDrained,
        'isHighAmount': isHighAmount,
        'destTransactionCount': destTransactionCount
    }

    df = pd.DataFrame([data])
    wynik = model.predict(df)
    proba = model.predict_proba(df)[0][1]
    if wynik[0] == 1:
        st.error(f"⚠️ High fraud risk — The transaction is Fraud (Probability: {proba:.0%})")
    else:
        st.success(f"✅ Low fraud risk — The transaction if not Fraud. (Probability: {proba:.0%})")
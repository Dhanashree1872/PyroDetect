import streamlit as st
import pickle
import numpy as np
model = pickle.load(open('model.pkl','rb'))

def predict_forest(oxygen,humidity,temperature):
    input=np.array([[oxygen,humidity,temperature]]).astype(np.float64)
    prediction=model.predict_proba(input)
    pred = '{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)

def main():

    html_temp0 = """
    <style>
    [data-testid="stAppViewContainer"] {
    # background: linear-gradient(115deg, #233329, #63d471);
    background-image: url("https://wallpapers.com/images/hd/dark-forest-background-ihw0yduemotnqh35.jpg");
    background-size: cover;
    }
    [data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
    }
    .stTextInput > label {
    font-size:150%;
    font-weight:bold;
    color:white;
    border: 2px;
    border-radius: 3px;
    }
    [data-baseweb="base-input"]{
    background-color: #b6a594;
    border: 2px;
    border-radius: 10px;
    
    input[class]{
    font-weight: bold;
    font-size:110%;
    color: black;
    }
    </style>
"""

    st.markdown(html_temp0, unsafe_allow_html=True)
    # st.title("Hello")

    html_temp2 = """
    <div style="padding:8px">
    <h1 style="color:#FFDAB9;text-align:center;height:100px;letter-spacing:3px;font-weight:500;">PYRODETECT</h1>
    </div>
    """
    st.markdown(html_temp2, unsafe_allow_html=True)

    oxygen = st.text_input("Oxygen")
    humidity = st.text_input("Humidity")
    temperature = st.text_input("Temperature")

    safe_html="""  
      <div style="padding:10px">
       <h2 style="color:#F4D03F;text-align:center;"> Your forest is safe</h2>
       </div>
    """
    danger_html="""  
      <div style="padding:10px">
       <h2 style="color:#FF0000;text-align:center;"> Your forest is in danger!</h2>
       </div>
    """

    if st.button("Predict",type="primary"):
        output=predict_forest(oxygen,humidity,temperature)
        st.success('The probability of fire taking place is {}'.format(output))

        if output > 0.5:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()

# python -m streamlit run app.py
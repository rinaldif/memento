import streamlit as st
import pandas as pd
import datetime

st.set_page_config(
    page_title="dieversary",
    page_icon="🌍",
    layout="wide",
    #initial_sidebar_state="expanded",
    #menu_items={
    #    'Get Help': 'https://www.extremelycoolapp.com/help',
    #    'Report a bug': "https://www.extremelycoolapp.com/bug",
    #    'About': "# This is a header. This is an *extremely* cool app!"
    #}
)

st.header("dieversary")

with st.sidebar: 
    with st.form(key='data_entry', border=False):
        usr_name = st.text_input('Your Name', placeholder="Enter your name")
        usr_dob = st.date_input('Your Date of Birth', 
                                min_value=datetime.date(1900, 1, 1), 
                                max_value=datetime.date.today()
                                )
        st.form_submit_button('Calculate')

current_date = datetime.date.today()

days_since_birth = current_date - usr_dob

st.markdown(f'Hello {usr_name if usr_name else 'there'}, you were born on {usr_dob} and you\'ve been travelling for {days_since_birth.days} days.')

st.markdown(f"Your 10000 dieversary will be on the {usr_dob+datetime.timedelta(days=10000)}")
st.markdown(f"Your 11111 dieversary will be on the {usr_dob+datetime.timedelta(days=11111)}")
st.markdown(f"Your 12345 dieversary will be on the {usr_dob+datetime.timedelta(days=12345)}")
st.markdown(f"Your 31415 dieversary will be on the {usr_dob+datetime.timedelta(days=31415)}")



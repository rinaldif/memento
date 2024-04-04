import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.express as px


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

tab1, tab2 = st.tabs(["Intro", "Memento Mori"])

with tab1: 
    current_date = datetime.date.today()

    days_since_birth = current_date - usr_dob

    st.markdown(f'Hello {usr_name if usr_name else 'there'}, you were born on {usr_dob} and you\'ve been travelling for {days_since_birth.days} days.')

    st.markdown(f"Your 10000 dieversary will be on the {usr_dob+datetime.timedelta(days=10000)}")
    st.markdown(f"Your 11111 dieversary will be on the {usr_dob+datetime.timedelta(days=11111)}")
    st.markdown(f"Your 12345 dieversary will be on the {usr_dob+datetime.timedelta(days=12345)}")
    st.markdown(f"Your 31415 dieversary will be on the {usr_dob+datetime.timedelta(days=31415)}")


with tab2: 
    ###### Memento Mori Life Calendar

    # data definition for calendar

    dob = datetime.date(1988, 9, 25)
    today = datetime.date.today()
    #days = (today - dob).days
    weeks = (today - usr_dob).days/7
    #years = (today - dob).days/365

    weeks_max = 80*52
    weeks_rem = weeks_max - round(weeks)

    weeks_cal = np.vstack((np.ones((round(weeks),1)), 
                        np.zeros((weeks_rem,1)) ))
                        
    df_cal = pd.DataFrame(data=weeks_cal.reshape(-1,52), 
                        index=range(1,81), 
                        columns=[str(wk) for wk in range(1,53)])

    # plot
    cell_size = 15
    row_title_width = 50
    width = cell_size*len(df_cal.columns) + row_title_width
    height = cell_size*len(df_cal.index)

    fig = px.imshow(df_cal, width=width, height=height, color_continuous_scale=['lightgrey', 'darkgrey'])
    fig.update(layout_coloraxis_showscale=False)   # to remove the colorscale
    fig.update_layout(showlegend=False)

    for i in range(len(df_cal.columns)):
        fig.add_shape(type="line", x0=0.5 + i, y0=0.5, x1=0.5 + i, y1=len(df_cal.index) + 0.5, line=dict(color="white", width=1))

    for i in range(len(df_cal.index)):
        fig.add_shape(type="line", x0=0.5, y0=0.5 + i, x1=len(df_cal.columns) + 0.5, y1=0.5 + i, line=dict(color="white", width=1))

    st.plotly_chart(fig, use_container_width=True, config = {'displayModeBar': False})

    #fig.show()




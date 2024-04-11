import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.express as px
import math


st.set_page_config(
    page_title="dieversary",
    page_icon="🚀",
    layout="wide",
    #initial_sidebar_state="expanded",
    #menu_items={
    #    'Get Help': 'https://www.extremelycoolapp.com/help',
    #    'Report a bug': "https://www.extremelycoolapp.com/bug",
    #    'About': "# This is a header. This is an *extremely* cool app!"
    #}
)

earth_speed_kmh = 1332000
ant_cm = 0.2
earth_diameter_cm = 1274200000
def magnitude(n): 
    return math.floor(math.log10(n))

st.header("dieversary")

with st.sidebar: 
    with st.form(key='data_entry', border=False):
        usr_name = st.text_input('Your Name', placeholder="Enter your name")
        usr_dob = st.date_input('Your Date of Birth', 
                                min_value=datetime.date(1900, 1, 1), 
                                max_value=datetime.date.today()
                                )
        st.form_submit_button('Calculate')

tab1, tab2, tab3 = st.tabs(["Your Journey", "Your Dieversary", "Memento Mori"])

### Your Journey
with tab1: 
    current_date = datetime.date.today()

    days_since_birth = current_date - usr_dob

    st.subheader("A cosmic Journey!")
    st.markdown(f'#### 👋 Hello {usr_name if usr_name else 'space traveller'}!')
    st.markdown(f'You were born on **<span style="font-size:15.0pt;">{usr_dob.strftime('%d-%b-%Y')}</span>**, it was a {usr_dob.strftime('%A')}, and you\'ve been travelling on this \
                amazing spaceship we call Earth for **<span style="font-size:15.0pt;">{days_since_birth.days:,}</span>** days.', 
                unsafe_allow_html=True)
    with st.expander("**Hey, do you know how fast you're going? Click here to find out!**"):
        st.markdown(f"""
                    - The Earth's speed at the equator relative to its center is 460 m/s (1656 km/h)  
                    - The Earth revolves around the Sun at a speed of 30 Km/s (108,000 Km/h)  
                    - Our solar system travels around the center of our galaxy at a speed of 220 km/s (792,000 km/h)  
                    - Galaxies around us travel at the incredible speed of 1000 Km/s (3,600,000 km/h) around the Great Attractor, 
                    a cluster of galaxies located at the gravitational center of Laniakea, the local supercluster to which the Milky Way 
                    also belongs.  
                    - The Great Attractor is about 150,000,000 light-years away from us; a light-year is equal to almost 9.461 billion kilometers.  
                    - So far, we've described these velocities relative to some other structure. But is there a universal reference point 
                    with respect to which we can define the motion and therefore the velocity of an object? The cosmic microwave background 
                    radiation, discovered in 1964, is the residual radiation from the early stages of the universe's birth and can still be 
                    observed today through a radio telescope. Towards the end of the 20th century, it was discovered that the Earth moves 
                    relative to the cosmic microwave background radiation at a well-defined speed and direction. The Earth travels at a 
                    speed of 370km/s ({earth_speed_kmh:,} km/h) in the direction of the constellation Leo.
                    """)
    st.markdown(f'Now, since `1 day = 24 hours`, it follows that `{days_since_birth.days:,} days = {24*days_since_birth.days:,} hours` \
                and since we just learned that Earth travels at a speed of {earth_speed_kmh:,} km/h it means that so far in your lifetime you have traveled **<span style="font-size:15.0pt;">{24*days_since_birth.days*1332000:,}</span>** km.', 
                unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1: 
        st.markdown(f"""
                ##### Feeling down?  
                On those days when you wake up and feel like you haven't accomplished enough or if you just need a little nudge, remember that in your lifetime you've already \
                    explored over **<span style="font-size:13.0pt;">{str(24*days_since_birth.days*earth_speed_kmh)[:3]} billion kilometers</span>** of \
                        cosmic space!
                """, unsafe_allow_html=True)
        st.markdown(" ")
    with col2: 
        st.markdown(f"""
                ##### Need some grounding?  
                When, on the other hand, you feel on top of the world and need to come back down to earth, consider that \
                    those {str(24*days_since_birth.days*earth_speed_kmh)[:3]} billion kilometers are equivalent to \
                        about **<span style="font-size:13.0pt;">{24*days_since_birth.days*earth_speed_kmh/9461000000000:.5f} light-years</span>**.
                """, unsafe_allow_html=True)
    
    st.markdown(f"Furthermore, consider that the observable universe currently has a diameter of about 92 billion light-years, \
                so the portion you've explored so far is equivalent to {(24*days_since_birth.days*earth_speed_kmh/9461000000000)/92000000000*100:.15f}% of \
                    its diameter.")
    st.markdown(f"Does this make you feel like a tiny ant? Well, know that the comparison doesn't hold up in reality. \
                In fact, a small ant like the Pharaoh ant is about {ant_cm}cm long, and if we compare it to Earth's diameter, \
                which is about {earth_diameter_cm:,}cm, then the insect is equivalent to about {ant_cm/earth_diameter_cm*100:.15f}% of the Earth's diameter, \
                so this comparison would underestimate the proportion by about {abs(magnitude((24*days_since_birth.days*earth_speed_kmh/9461000000000)/92000000000) - magnitude(ant_cm/earth_diameter_cm))} orders of magnitude!")
    st.error("👇 Cambiare da tardigrado a nucleo della cellula (grandezza giusta per confronto è 0.001cm): 👇")
    st.markdown(f"""To have a more accurate comparison, we need to borrow a microscope... :microscope:  
                ~~To have a more accurate comparison, we need to disturb the tardigrades... what? You don't know what tardigrades are? 
                Well, they are a phylum of coelomate protostome invertebrates! These are colloquially called "water bears," 
                eight-legged creatures whose smallest specimens are about 0.1mm long and whose peculiarity is that they can survive in 
                extreme conditions, even in space! So, compared to the Earth's diameter, a tardigrade has a length of 
                about {0.01/earth_diameter_cm*100:.15f}%, which is still about {math.floor((0.01/earth_diameter_cm) / ((24*days_since_birth.days*earth_speed_kmh/9461000000000)/92000000000))} \
                times bigger than the proportion we started with.~~""") 
    st.markdown(f"""Therefore, in conclusion, the correct proportion is that the distance you've traveled in space so far compared to \
                the length of the observable universe is equal to traveling one {math.floor((0.01/earth_diameter_cm) / ((24*days_since_birth.days*earth_speed_kmh/9461000000000)/92000000000))}th the length of a small tardigrade (less than 0.01mm) compared to \
                the Earth's diameter!""")
    st.markdown(f"""
            - prop: {((24*days_since_birth.days*earth_speed_kmh/9461000000000)/92000000000):.15f}
            - prop: {(0.001/earth_diameter_cm):.15f}
            - ratio: {math.floor((0.001/earth_diameter_cm) / ((24*days_since_birth.days*earth_speed_kmh/9461000000000)/92000000000))}
            """)



### Dieversaries
with tab2: 
    st.markdown(f"Your 10000 dieversary will be on the {usr_dob+datetime.timedelta(days=10000)}")
    st.markdown(f"Your 11111 dieversary will be on the {usr_dob+datetime.timedelta(days=11111)}")
    st.markdown(f"Your 12345 dieversary will be on the {usr_dob+datetime.timedelta(days=12345)}")
    st.markdown(f"Your 31415 dieversary will be on the {usr_dob+datetime.timedelta(days=31415)}")


### Memento Mori Life Calendar
# inspiration: https://store.dailystoic.com/collections/memento-mori/products/premium-memento-mori-calendar
with tab3: 
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




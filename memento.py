import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.express as px
import math


# Page config and setup
st.set_page_config(
    page_title="Memento Vivere",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
    #menu_items={
    #    'Get Help': 'https://www.extremelycoolapp.com/help',
    #    'Report a bug': "https://www.extremelycoolapp.com/bug",
    #    'About': "# This is a header. This is an *extremely* cool app!"
    #}
)

# Initial constants and functions definition
today = datetime.date.today()
earth_speed_kmh = 1332000
ant_cm = 0.2
earth_diameter_cm = 1274200000
def magnitude(n): 
    if n > 0: 
        return math.floor(math.log10(n))
    else: 
        return 1

st.header("Memento Vivere")

# Form to enter input information
col1, col2 = st.columns(2)
with col1: 
    st.markdown("#### Please enter your :orange[name] and :orange[date of birth] in the form below.")
    with st.form(key='data_entry', border=False):
        usr_name = st.text_input('Your Name', placeholder="Enter your name (optional)")
        usr_dob = st.date_input('Your Date of Birth', 
                                value=None, 
                                min_value=datetime.date(1900, 1, 1), 
                                max_value=datetime.date.today() - datetime.timedelta(days=1)
                                )
        st.form_submit_button('Calculate')

# Main body of the app
if usr_dob is None: 
    st.markdown(" ")
else:
    tab1, tab2, tab3 = st.tabs(["A Space Journey", "Your Dayversary", "Memento Mori"])

    ### Your Cosmic Journey
    with tab1: 
        current_date = datetime.date.today()

        days_since_birth = current_date - usr_dob

        st.subheader("A cosmic Journey!")
        st.markdown(f"#### 👋 Hello {usr_name if usr_name else 'space traveller'}!")
        st.markdown(f"""You were born on **<span style="font-size:15.0pt;">{usr_dob.strftime('%d-%b-%Y')}</span>**, it was a **{usr_dob.strftime('%A')}**, and you\'ve been travelling on this \
                    amazing spaceship we call Earth for **<span style="font-size:15.0pt;">{days_since_birth.days:,}</span>** days.""", 
                    unsafe_allow_html=True)
        with st.expander("**Hey, do you know how fast you're going? :orange[Click here] to find out!**"):
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
        st.markdown(f"""Now, since `1 day = 24 hours`, it follows that `{days_since_birth.days:,} days = {24*days_since_birth.days:,} hours` \
                    and since we just learned that **Earth travels at a speed of {earth_speed_kmh:,} km/h** it means that so far in your lifetime you have traveled **<span style="font-size:15.0pt;">{24*days_since_birth.days*1332000:,}</span>** km.""", 
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
                        those {str(24*days_since_birth.days*earth_speed_kmh)[:3]} billion kilometers are equivalent to just\
                            about **<span style="font-size:13.0pt;">{24*days_since_birth.days*earth_speed_kmh/9461000000000:.5f} light-years</span>**.
                    """, unsafe_allow_html=True)
        
        st.markdown("##### So is that a lot or not?")
        st.markdown(f"""It's hard to juggle such astronomical numbers in our head, so let's compare them to something we have more direct experience with.  
                    But first, consider this: the [**observable universe**](https://en.wikipedia.org/wiki/Observable_universe) currently has a diameter of about **<span style="font-size:13.0pt;">92 billion light-years</span>**,
                    so **the portion you've explored so far** is equivalent to 
                    **<span style="font-size:13.0pt;">{(24*days_since_birth.days*earth_speed_kmh/9461000000000)/92000000000*100:.15f}%</span>** \
                    of its diameter.  
                    <img src=https://images.rawpixel.com/image_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIzLTA5L3Jhd3BpeGVsX29mZmljZV8zM19zYmFfZ2FsYXh5X19pc29sYXRlZF9vbl93aGl0ZV9iYWNrZ3JvdW5kX2E2NmQ2YWJmLWMwN2QtNGU1Yy05OTNkLWIxM2Q1ZmUzOWRmZl8xLmpwZw.jpg alt="Galaxy artwork" width="350">
                    """, unsafe_allow_html=True)
        
        st.markdown(f"""Does this make you feel like a **tiny ant**? Well, you should know that the comparison doesn't actually hold up. \
                    In fact, a small ant like the [**Pharaoh ant**](https://en.wikipedia.org/wiki/Pharaoh_ant) is about {ant_cm}cm long, and if we compare it to Earth's diameter, \
                    which is about {earth_diameter_cm:,}cm, then the insect is equivalent to about **<span style="font-size:13.0pt;">{ant_cm/earth_diameter_cm*100:.15f}%</span>** of the Earth's diameter, \
                    so this comparison would underestimate the proportion by about **<span style="font-size:13.0pt;">{abs(magnitude((24*days_since_birth.days*earth_speed_kmh/9461000000000)/92000000000) - magnitude(ant_cm/earth_diameter_cm))} orders of magnitude</span>**!""", 
                    unsafe_allow_html=True)
        st.markdown("""<img src=https://media.istockphoto.com/id/1387046877/vector/many-ants-vector-seamless-pattern.jpg?s=612x612&w=0&k=20&c=Ri4xcPgpsIdSIDk05XNOy0ime8U3tQ5X62RTxmgXDQM= alt="Ants on white background" width="350">""", 
                        unsafe_allow_html=True)

        st.markdown(f"""To have a more accurate comparison, we need to borrow a microscope! :microscope:  
                    The **nucleus of an animal cell** measures an average of 0.001cm which, compared to the Earth's diameter, 
                    is about **<span style="font-size:13.0pt;">{0.001/earth_diameter_cm*100:.15f}%</span>**, which is much more aligned to 
                    our initial proportion (although it is still about **<span style="font-size:13.0pt;">{round((0.001/earth_diameter_cm) / ((24*days_since_birth.days*earth_speed_kmh/9461000000000)/92000000000),2)}
                    times bigger</span>** than the proportion we started with).  
                    <img src=https://etc.usf.edu/clipart/15300/15389/cell_15389_lg.gif alt="Cell and nucleus" width="200">
                    """, unsafe_allow_html=True) 
        
        st.markdown(f"""
                    <span style="font-size:13.0pt;">So in conclusion, we can say that **<span style="font-size:15.0pt;">the distance you've traveled in space so far</span>**
                    compared to 
                    **<span style="font-size:15.0pt;">the observable universe</span>**  
                    is equivalent to 
                    **<span style="font-size:15.0pt;">the length of the nucleus of an animal cell</span>** 
                    compared to 
                    **<span style="font-size:15.0pt;">the Earth's diameter</span>**!</span>
                    """, unsafe_allow_html=True)

    ### Dayversaries
    with tab2: 
        st.markdown(" ")
        st.markdown("##### Use the input below to find out the date of your past, current or future dayversary.")
        col1, col2 = st.columns(2)
        with col1: 
            days_input = col1.number_input("Enter the number of days", 
                                           value=10000, 
                                           min_value=0)
        if usr_dob+datetime.timedelta(days=days_input) < datetime.date.today(): 
            st.subheader(f"Your {days_input:,} dayversary was on the {usr_dob+datetime.timedelta(days=days_input)}")
            st.markdown(f"##### and you were about {days_input/365:.0f} years old")
        elif usr_dob+datetime.timedelta(days=days_input) > datetime.date.today(): 
            st.subheader(f"Your {days_input:,} dayversary will be on the {usr_dob+datetime.timedelta(days=days_input)}")
            st.markdown(f"###### and you will be about {days_input/365:.0f} years old")
        elif usr_dob+datetime.timedelta(days=days_input) == datetime.date.today(): 
            st.subheader(f"Hoorray! 🎉 Your dayversary is today!!")
        else: 
            st.markdown("Something went wrong... 🤖")

    ### Memento Mori Life Calendar
    # inspiration: https://store.dailystoic.com/collections/memento-mori/products/premium-memento-mori-calendar
    with tab3: 
        st.markdown(" ")
        st.markdown("##### The following is an interactive [Memento Mori](https://en.wikipedia.org/wiki/Memento_mori) calendar.")
        st.caption("*Credits: this calendar has been inspired by the Daily Stoic Memento Mori [calendar](https://store.dailystoic.com/collections/memento-mori/products/premium-memento-mori-calendar).*")
        st.markdown("""> *You could leave life right now. Let that determine what you do and say and think.*  
                    **Marcus Aurelius**""")
        years_left = 80 - (today - usr_dob).days/365 if (today - usr_dob).days/365 <= 80 else 0
        #st.markdown(f"""Nowadays, the average human lifespan is **80 years**, that is {80*52:,} weeks or {80*52*7:,} days. """)
        if (today - usr_dob).days/365 < 80: 
            st.markdown(f"""Nowadays, the average human lifespan is **80 years**, that is {80*52:,} weeks or {80*52*7:,} days.  
                        If you were lucky enough to live that long, you would have **<span style="font-size:15.0pt;">{years_left:.0f} years left to live</span>**, then think again to Marcus Aurelius words: **how will you spend them?** 
                        """, unsafe_allow_html=True)
        else: 
            st.markdown(f"""Nowadays, the average human lifespan is **80 years**, that is {80*52:,} weeks or {80*52*7:,} days and 
                        you were lucky enough to live that long! 
                        """)
        st.markdown("""
                        **Each square in this calendar represents a week of your life** and each column contains 52 weeks, that is 1 year of your life: 
                        - by looking at the :grey[**dark-grey squares**], you will see how much life you've already lived 
                        (or as [Seneca said](https://www.goodreads.com/quotes/447621-what-man-can-you-show-me-who-places-any-value), how much you’ve already died), 
                        - whereas the :grey[*light-grey squares*] will show you how much life you've (hopefully) got left.
                        """, unsafe_allow_html=True)
        st.info("Note: calendar redering is optimized for desktop consumption.")

        # data definition for calendar

        #dob = datetime.date(1988, 9, 25)
        #days = (today - dob).days
        #years = (today - dob).days/365

        # This if-else is necessary for those entering a dob resulting in an age greater than 80 years
        
        if (today - usr_dob).days/7 <= 4160: 
            weeks = (today - usr_dob).days/7
        else: 
            weeks = 4160

        weeks_max = 80*52
        weeks_rem = weeks_max - round(weeks)
        
        weeks_cal = np.vstack((np.ones((round(weeks),1)), 
                            np.zeros((weeks_rem,1)) ))
                            
        df_cal = pd.DataFrame(data=weeks_cal.reshape(-1,52).T, 
                            index=[str(wk) for wk in range(1,53)], 
                            columns=range(1,81))

        # plot
        cell_size = 15
        row_title_width = 50
        width = cell_size*len(df_cal.columns) + row_title_width
        height = cell_size*len(df_cal.index)

        fig = px.imshow(df_cal, width=width, height=height, color_continuous_scale=['lightgrey', 'darkgrey'], 
                        labels=dict(x="Years in your life", y="Weeks in the year", color="Lived / not yet lived")
                        )
        fig.update(layout_coloraxis_showscale=False)   # to remove the colorscale
        fig.update_layout(showlegend=False)
        fig.update_layout(xaxis={'side': 'top'})   # move x-axis to the top of the chart/calendar

        for i in range(len(df_cal.columns)):
            fig.add_shape(type="line", x0=0.5 + i, y0=0.5, x1=0.5 + i, y1=len(df_cal.index) + 0.5, line=dict(color="white", width=1))

        for i in range(len(df_cal.index)):
            fig.add_shape(type="line", x0=0.5, y0=0.5 + i, x1=len(df_cal.columns) + 0.5, y1=0.5 + i, line=dict(color="white", width=1))

        st.plotly_chart(fig, use_container_width=True, config = {'displayModeBar': False})

        st.markdown("""
                    Let's not forget that while we should to ponder on the brevity of life, we also need to hold that knowledge in tension with 
                    how incredible life can be when we remember to live it well and with purpouse: 
                    - Memento Mori: remember that you will die 
                    - Memento Vivere: **remember to live!**
                    """)





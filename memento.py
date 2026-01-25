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

# Physical constants
EARTH_SPEED_KMH = 1_332_000  # Earth's speed relative to CMB in km/h
LIGHT_YEAR_KM = 9_461_000_000_000  # One light-year in km
OBSERVABLE_UNIVERSE_LY = 92_000_000_000  # Observable universe diameter in light-years
ANT_CM = 0.2  # Pharaoh ant size in cm
CELL_NUCLEUS_CM = 0.001  # Average animal cell nucleus diameter in cm
EARTH_DIAMETER_CM = 1_274_200_000  # Earth's diameter in cm

# Time constants
HOURS_PER_DAY = 24
DAYS_PER_YEAR = 365.25  # Account for leap years
WEEKS_PER_YEAR = 52
AVERAGE_LIFESPAN_YEARS = 80

def magnitude(n):
    if n <= 0:
        raise ValueError("magnitude requires a positive number")
    return math.floor(math.log10(n))

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

        # Pre-calculate cosmic journey values
        total_hours = HOURS_PER_DAY * days_since_birth.days
        distance_km = total_hours * EARTH_SPEED_KMH
        distance_ly = distance_km / LIGHT_YEAR_KM
        universe_proportion = (distance_ly / OBSERVABLE_UNIVERSE_LY) * 100
        ant_proportion = (ANT_CM / EARTH_DIAMETER_CM) * 100
        cell_proportion = (CELL_NUCLEUS_CM / EARTH_DIAMETER_CM) * 100

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
                        - The Great Attractor is about 150,000,000 light-years away from us; a light-year is equal to almost 9.461 trillion kilometers.  
                        - So far, we've described these velocities relative to some other structure. But is there a universal reference point 
                        with respect to which we can define the motion and therefore the velocity of an object? The cosmic microwave background 
                        radiation, discovered in 1964, is the residual radiation from the early stages of the universe's birth and can still be 
                        observed today through a radio telescope. Towards the end of the 20th century, it was discovered that the Earth moves
                        relative to the cosmic microwave background radiation at a well-defined speed and direction. The Earth travels at a
                        speed of 370km/s ({EARTH_SPEED_KMH:,} km/h) in the direction of the constellation Leo.
                        """)
        st.markdown(f"""Now, since `1 day = 24 hours`, it follows that `{days_since_birth.days:,} days = {total_hours:,} hours` \
                    and since we just learned that **Earth travels at a speed of {EARTH_SPEED_KMH:,} km/h** it means that so far in your lifetime you have traveled **<span style="font-size:15.0pt;">{distance_km:,}</span>** km.""",
                    unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
                    ##### Feeling down?
                    On those days when you wake up and feel like you haven't accomplished enough or if you just need a little nudge, remember that in your lifetime you've already \
                        explored over **<span style="font-size:13.0pt;">{str(distance_km)[:3]} billion kilometers</span>** of \
                            cosmic space!
                    """, unsafe_allow_html=True)
            st.markdown(" ")
        with col2:
            st.markdown(f"""
                    ##### Need some grounding?
                    When, on the other hand, you feel on top of the world and need to come back down to earth, consider that \
                        those {str(distance_km)[:3]} billion kilometers are equivalent to just\
                            about **<span style="font-size:13.0pt;">{distance_ly:.5f} light-years</span>**.
                    """, unsafe_allow_html=True)
        
        st.markdown("##### So is that a lot or not?")
        st.markdown(f"""It's hard to juggle such astronomical numbers in our head, so let's compare them to something we have more direct experience with.
                    But first, consider this: the [**observable universe**](https://en.wikipedia.org/wiki/Observable_universe) currently has a diameter of about **<span style="font-size:13.0pt;">{OBSERVABLE_UNIVERSE_LY:,} light-years</span>**,
                    so **the portion you've explored so far** is equivalent to
                    **<span style="font-size:13.0pt;">{universe_proportion:.15f}%</span>** \
                    of its diameter.
                    """, unsafe_allow_html=True)
        _, img_col, _ = st.columns([1, 2, 1])
        with img_col:
            st.image("images/galaxy.jpg", width=350)
        
        st.markdown(f"""Does this make you feel like a **tiny ant**? Well, you should know that the comparison doesn't actually hold up. \
                    In fact, a small ant like the [**Pharaoh ant**](https://en.wikipedia.org/wiki/Pharaoh_ant) is about {ANT_CM}cm long, and if we compare it to Earth's diameter, \
                    which is about {EARTH_DIAMETER_CM:,}cm, then the insect is equivalent to about **<span style="font-size:13.0pt;">{ant_proportion:.15f}%</span>** of the Earth's diameter, \
                    so this comparison would underestimate the proportion by about **<span style="font-size:13.0pt;">{abs(magnitude(universe_proportion / 100) - magnitude(ant_proportion / 100))} orders of magnitude</span>**!""",
                    unsafe_allow_html=True)
        _, img_col, _ = st.columns([1, 2, 1])
        with img_col:
            st.image("images/ants.jpg", width=350)

        st.markdown(f"""To have a more accurate comparison, we need to borrow a microscope! :microscope:
                    The **nucleus of an animal cell** measures an average of {CELL_NUCLEUS_CM}cm which, compared to the Earth's diameter,
                    is about **<span style="font-size:13.0pt;">{cell_proportion:.15f}%</span>**, which is much more aligned to
                    our initial proportion (although it is still about **<span style="font-size:13.0pt;">{round(cell_proportion / universe_proportion, 2)}
                    times bigger</span>** than the proportion we started with).
                    """, unsafe_allow_html=True)
        _, img_col, _ = st.columns([1, 2, 1])
        with img_col:
            st.image("images/cell.gif", width=200) 
        
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
        dayversary_date = usr_dob + datetime.timedelta(days=days_input)
        if dayversary_date < datetime.date.today():
            st.subheader(f"Your {days_input:,} dayversary was on the {dayversary_date}")
            st.markdown(f"##### and you were about {days_input/DAYS_PER_YEAR:.0f} years old")
        elif dayversary_date > datetime.date.today():
            st.subheader(f"Your {days_input:,} dayversary will be on the {dayversary_date}")
            st.markdown(f"###### and you will be about {days_input/DAYS_PER_YEAR:.0f} years old")
        elif dayversary_date == datetime.date.today():
            st.subheader(f"Hooray! 🎉 Your dayversary is today!!")
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
        user_age_years = (today - usr_dob).days / DAYS_PER_YEAR
        years_left = AVERAGE_LIFESPAN_YEARS - user_age_years if user_age_years <= AVERAGE_LIFESPAN_YEARS else 0
        total_weeks = AVERAGE_LIFESPAN_YEARS * WEEKS_PER_YEAR
        total_days = total_weeks * 7

        if user_age_years < AVERAGE_LIFESPAN_YEARS:
            st.markdown(f"""Nowadays, the average human lifespan is **{AVERAGE_LIFESPAN_YEARS} years**, that is {total_weeks:,} weeks or {total_days:,} days.
                        If you were lucky enough to live that long, you would have **<span style="font-size:15.0pt;">{years_left:.0f} years left to live</span>**, then think again to Marcus Aurelius words: **how will you spend them?**
                        """, unsafe_allow_html=True)
        else:
            st.markdown(f"""Nowadays, the average human lifespan is **{AVERAGE_LIFESPAN_YEARS} years**, that is {total_weeks:,} weeks or {total_days:,} days and
                        you were lucky enough to live that long!
                        """)
        # Let user choose calendar orientation
        is_mobile = st.toggle("📱 Mobile view", value=False, help="Switch to portrait-friendly layout")

        if is_mobile:
            st.markdown("""
                        **Each square in this calendar represents a week of your life** and each row contains 52 weeks, that is 1 year of your life:
                        - by looking at the :grey[**dark-grey squares**], you will see how much life you've already lived
                        (or as [Seneca said](https://www.goodreads.com/quotes/447621-what-man-can-you-show-me-who-places-any-value), how much you've already died),
                        - whereas the :grey[*light-grey squares*] will show you how much life you've (hopefully) got left.
                        """, unsafe_allow_html=True)
        else:
            st.markdown("""
                        **Each square in this calendar represents a week of your life** and each column contains 52 weeks, that is 1 year of your life:
                        - by looking at the :grey[**dark-grey squares**], you will see how much life you've already lived
                        (or as [Seneca said](https://www.goodreads.com/quotes/447621-what-man-can-you-show-me-who-places-any-value), how much you've already died),
                        - whereas the :grey[*light-grey squares*] will show you how much life you've (hopefully) got left.
                        """, unsafe_allow_html=True)

        # data definition for calendar
        # This if-else is necessary for those entering a dob resulting in an age greater than 80 years
        weeks_max = AVERAGE_LIFESPAN_YEARS * WEEKS_PER_YEAR
        weeks_lived = (today - usr_dob).days / 7

        if weeks_lived <= weeks_max:
            weeks = weeks_lived
        else:
            weeks = weeks_max

        weeks_rem = weeks_max - round(weeks)

        weeks_cal = np.vstack((np.ones((round(weeks), 1)),
                            np.zeros((weeks_rem, 1))))

        # Create DataFrame with orientation based on screen size
        if is_mobile:
            # Mobile: 80 rows (years) × 52 columns (weeks) - portrait friendly
            df_cal = pd.DataFrame(data=weeks_cal.reshape(-1, WEEKS_PER_YEAR),
                                index=range(1, AVERAGE_LIFESPAN_YEARS + 1),
                                columns=[str(wk) for wk in range(1, WEEKS_PER_YEAR + 1)])
            x_label = "Weeks in the year"
            y_label = "Years in your life"
            cell_size = 6
        else:
            # Desktop: 52 rows (weeks) × 80 columns (years) - landscape friendly
            df_cal = pd.DataFrame(data=weeks_cal.reshape(-1, WEEKS_PER_YEAR).T,
                                index=[str(wk) for wk in range(1, WEEKS_PER_YEAR + 1)],
                                columns=range(1, AVERAGE_LIFESPAN_YEARS + 1))
            x_label = "Years in your life"
            y_label = "Weeks in the year"
            cell_size = 15

        # plot
        row_title_width = 50
        width = cell_size * len(df_cal.columns) + row_title_width
        height = cell_size * len(df_cal.index)

        fig = px.imshow(df_cal, width=width, height=height, color_continuous_scale=['lightgrey', 'darkgrey'],
                        labels=dict(x=x_label, y=y_label, color="Lived / not yet lived")
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
                    Let's not forget that while we should ponder on the brevity of life, we also need to hold that knowledge in tension with 
                    how incredible life can be when we remember to live it well and with purpose: 
                    - Memento Mori: remember that you will die 
                    - Memento Vivere: **remember to live!**
                    """)





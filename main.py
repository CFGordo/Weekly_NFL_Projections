import pandas as pd
import streamlit as st
import agstyler
from agstyler import PINLEFT, draw_grid
from enum import Enum

st.title("🏈 Weekly NFL Projections 🏈")
st.text("")

projections_db_link = st.secrets["projections_db_url"]
projections_db_csv = projections_db_link.replace('/edit#gid=', '/export?format=csv&gid=')
projections_db = pd.read_csv(projections_db_csv)


def color__red(value):
    """
  helper for non current observations.
  """

    if value != 1.2023:
        color = 'violet'
    else:
        color = 'white'

    return 'color: %s' % color


def color_green(value):
    """
  Colors elements green
  """

    if value > 2.6:
        color = 'green'
    elif value < 1.8:
        color = 'violet'
    else:
        color = 'white'

    return 'color: %s' % color


def color_good(value):
    """
  Colors elements green
  """

    if value > 20:
        color = 'green'
    elif value < 10:
        color = 'violet'
    else:
        color = 'white'

    return 'color: %s' % color

projections_db.set_index('Name', inplace=True)
zero = ['Salary', 'RBrank', 'WRrank', 'TErank', 'FLEXrank']
one = ['AvgPointsPerGame', 'predRush_yds',
       'predRec', 'predRec_yds',  'pred_standard',
       'pred_halfPPR', 'pred_PPR', 'Last Observed Pts PPR']
two = ['Pt_per_$1k (projected)', 'predRushTD', 'predRec_TD']
#projections_db = projections_db.round({'Salary': 0, 'RBrank': 0, 'WRrank': 0, 'TErank': 0, 'FLEXrank': 0})
#projections_db = projections_db.round({'AvgPointsPerGame': 1, 'predRush_yds': 1,
#       'predRec': 1, 'predRec_yds': 1,  'pred_standard': 1,
#       'pred_halfPPR': 1, 'pred_PPR': 1, 'Last Observed Pts PPR': 1})
#projections_db = projections_db.round({'Pt_per_$1k (projected)': 2, 'predRushTD': 2, 'predRec_TD': 2})
st.dataframe(projections_db.style.applymap(color__red, subset=['Last Observed Week.Season']).applymap(color_good, subset=['pred_PPR', 'Last Observed Pts PPR', 'AvgPointsPerGame']).applymap(color_green, subset=['Pt_per_$1k (projected)']).format(precision=0, subset = zero).format(precision=1, subset = one).format(precision=2, subset = two).format(precision=4, subset = ['Last Observed Week.Season']))

st.text("")
st.markdown("<p class='small-font'> Author= CFGordo </p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'> Data= NFLverse, FFverse, Draftkings </p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'> Calculations= CFGordo </p>", unsafe_allow_html=True)
st.text("")
st.write("Caveats & Dissembling:")
st.write("")
st.write("* These projections are based primarily on volume. Vegas Lines and other measures of Team and Player "
        "strength are not factored in.")
st.write("")
st.write("* These are meant as more of a baseline. They aren't adjusted for injuries to teammates, trades, "
        "coaching changes, etc.")
st.write("")
st.write("* The projections look back 8 weeks. For players who don't have 8 weeks of data (Rookies), missing data "
        "is input as league average at their position. For this reason Rookies, and players with dramatic "
        "changes in team or role will lag. Use your own knowledge of the league to determine whether you "
         "feel a particular projection is off base.")
st.write("")
st.write("* Some role players with a few spike weeks may be inflated. For this reason I've included the week "
        "& season, and points scored of the last recorded game for each player.")
st.write("")
st.write("* If the above notes haven't convinced you that these projections aren't all that sharp, allow me to "
        "remove all doubt - These projections aren't all that sharp. For the love of God don't use them to gamble "
        "large sums of money.")

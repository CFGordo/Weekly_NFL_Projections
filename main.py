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


def color_green2(value):
    """
  Colors elements green
  """

    if value > 20:
        color = 'green'
    elif value < 15:
        color = 'light green'
    else:
        color = 'white'


projections_db.set_index('Name', inplace=True)
zero = ['Salary', 'RBrank', 'WRrank', 'TErank', 'FLEXrank']
one = ['AvgPointsPerGame', 'predRush_yds',
       'predRec', 'predRec_yds',  'pred_standard',
       'pred_halfPPR', 'pred_PPR', 'Last Observed Pts PPR']
two = ['Pt_per_$1k (projected)', 'predRushTD', 'predRec_TD']
projections_db.round(round({zero: 0, one: 1, two: 0}), inplace=True)
projections_db.fillna('-', inplace=True)
st.dataframe(projections_db.style.applymap(color__red, subset=['Last Observed Week.Season']).applymap(color_green2, subset=['pred_PPR', 'Last Observed Pts PPR', 'AvgPointsPerGame']).applymap(color_green, subset=['Pt_per_$1k (projected)']))

st.text("")
st.markdown("<p class='small-font'> Author= CFGordo </p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'> Data= NFLverse, FFverse, Draftkings </p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'> Calculations= CFGordo </p>", unsafe_allow_html=True)

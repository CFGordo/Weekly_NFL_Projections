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
        color = 'purple'
    else:
        color = 'black'

    return 'color: %s' % color


def color_green(value):
    """
  Colors elements green
  """

    if value > 2.6:
        color = 'green'
    elif value < 1.8:
        color = 'purple'
    else:
        color = 'black'

    return 'color: %s' % color


def color_green2(value):
    """
  Colors elements green
  """

    if value > 20:
        color = 'green'
    elif value < 15:
        color = 'lime'
    else:
        color = 'black'


st.dataframe(projections_db.style.applymap(
    color__red, subset=['Last Observed Week.Season']).applymap(color_green2,
                                                               subset=['predPP',
                                                                       'Last Observed Pts PPR']).applymap(
                                                                        color_green, subset=['Pts_per_$1k']))

st.text("")
st.markdown("<p class='small-font'> Author= CFGordo </p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'> Data= NFLverse, FFverse, Draftkings </p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'> Calculations= CFGordo </p>", unsafe_allow_html=True)

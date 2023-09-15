import pandas as pd
import streamlit as st
import agstyler
from agstyler import PINLEFT, draw_grid
from enum import Enum


st.title("🏈 Weekly NFL Projections 🏈")

projections_db_link = st.secrets["projections_db_url"]
projections_db_csv = projections_db_link.replace('/edit#gid=', '/export?format=csv&gid=')
projections_db = pd.read_csv(projections_db_csv)

st.text("")


st.text("")
st.markdown("<p class='small-font'> Author= CFGordo </p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'> Data= NFLverse, FFverse, Draftkings </p>", unsafe_allow_html=True)
st.markdown("<p class='small-font'> Calculations= CFGordo </p>", unsafe_allow_html=True)

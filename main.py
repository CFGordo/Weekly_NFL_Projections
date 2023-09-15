import pandas as pd
import streamlit as st
import agstyler
from agstyler import PINLEFT, draw_grid
from enum import Enum


st.title("🏈 Weekly NFL Projections 🏈")

projections_db_link = st.secrets["projections_db_url"]
projections_db_csv = projections_db_link.replace('/edit#gid=', '/export?format=csv&gid=')
projections_db = pd.read_csv(projections_db_csv)
#columns =['2021_wk0','2021_wk1','2021_wk2','2021_wk3','2021_wk4','2021_wk5','2021_wk6','2021_wk7','2021_wk8','2021_wk9','2021_wk10','2021_wk11','2021_wk12','2021_wk13','2021_wk14','2021_wk15','2021_wk16','2021_wk17','2021_wk18','2021_final','2022_open','2022_wk1','2022_wk2','2022_wk3','2022_wk4','2022_wk5','2022_wk6','2022_wk7','2022_current','22 open vs. 21 final','current vs. 22 open','weighted ADP- curent vs. 22 open','pts above replacement- flex 1qb','pts above replacement- flex 2qb','2022_wk8','2022_wk9','2022_wk10','2022_wk11','2022_wk12','2022_wk13','2022_wk14','2022_wk15','2022_wk16','2022_wk17','2022_wk18']
#for column in columns:
#    projections_db[column] = pd.to_numeric(projections_db[column], errors = 'coerce')

st.text("")
st.markdown("Here lies a table. And why not?")
st.text("")
st.markdown("Use the 'Filters' and 'Columns' buttons on the right of the table to filter"
            " your search.")
class Color(Enum):
    GREEN_LIGHT = "rgb(0, 120, 60, .6)"
    RED_LIGHT = "rgb(120, 0, 40, .5)"


condition_one_value = "params.value >= 15"
condition_two_value = "params.value == 'Week 1 23'"
condition_three_value = "params.value >=2.6"

formatter = {
    'Name': ('Name', {**PINLEFT, 'width': 70}),
    'Roster Position': ('Roster Position', {'width': 70}),
    'Game Info': ('Game Info', {'width': 70}),
    'TeamAbbrev': ('Team', {'width': 70}),
    'AvgPointsPerGame': ('Avg PPG', {'width': 70, 'cellStyle': agstyler.highlight(Color.GREEN_LIGHT.value,
                                                                                                                condition_one_value)}),
    'Salary': ('Salary', {'width': 70}),
    'Pt_per_$1k (projected)': ('Pt_per_$1k (projected)', {'width': 70, 'cellStyle': agstyler.highlight(Color.GREEN_LIGHT.value,
                                                                                                                condition_three_value)}),
    'predRush_yds': ('Pred Rush Yds', {'width': 70}),
    'predRushTD': ('Pred Rush TD', {'width': 70}),
    'predRec': ('Pred Rec', {'width': 70}),
    'predRec_yds': ('Pred Rec Yds', {'width': 70}),
    'predRec_TD': ('Pred Rec TD', {'width': 70}),
    'pred_standard': ('Pred Standard', {'width': 70}),
    'pred_halfPPR': ('Pred Half PPR', {'width': 70}),
    'pred_PPR': ('Pred PPR', {'width': 70, 'cellStyle': agstyler.highlight(Color.GREEN_LIGHT.value,
                                                                                                                condition_one_value)}),
    'Last Observed Pts PPR': ('Last Observed Pts PPR', {'width': 70, 'cellStyle': agstyler.highlight(Color.GREEN_LIGHT.value,
                                                                                                                condition_one_value)}),
    'Last Observed Game Date': ('Last Observed Game Date', {'width': 70, 'cellStyle': agstyler.highlight(Color.Red_LIGHT.value,
                                                                                                                condition_two_value)}),
    'RBrank': ('RB Rank PPR', {'width': 70}),
    'WRrank': ('WR Rank PPR', {'width': 70}),
    'TErank': ('TE Rank PPR', {'width': 70}),
    'FLEXrank': ('FLEX Rank PPR', {'width': 70})
}
st.markdown("Select Season to Compare:")

data = draw_grid(
    projections_db,
    formatter=formatter,
    fit_columns=False,
    selection='single',  # or 'single', or None
    use_checkbox='True',  # or False by default
    filterable=False,
    max_height=400
)
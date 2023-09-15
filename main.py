import pandas as pd
import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid

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
gb = GridOptionsBuilder.from_dataframe(projections_db)
gb.configure_side_bar()  # Add a sidebar
gb.configure_selection('multiple', use_checkbox=True,
                       groupSelectsChildren="Group checkbox select children")  # Enable multi-row selection
gridOptions = gb.build()

grid_response = AgGrid(
    projections_db,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT',
    update_mode='MODEL_CHANGED',
    fit_columns_on_grid_load=False,
    theme='dark',  # Add theme color to the table
    enable_enterprise_modules=True,
    height=350,
    width='100%',
    reload_data=False
)

data = grid_response['data']
selected = grid_response['selected_rows']
df = pd.DataFrame(selected)  # Pass the selected rows to a new dataframe df

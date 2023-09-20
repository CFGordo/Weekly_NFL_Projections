from dash import Dash, html, dcc, Input, Output  # pip install dash
import dash_ag_grid as dag  # pip install dash-ag-grid
import pandas as pd  # pip install pandas
import plotly.express as px


projections_db_link = 'https://docs.google.com/spreadsheets/d/1ibuWDiDMknjTn9tuikjJSnOFD8MRlqnvJtFwlBaasXQ/edit#gid=176535567'
projections_db_csv = projections_db_link.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(projections_db_csv)


#df = pd.read_csv('C:/Users/chris/OneDrive/Documents/Fantasy_Football/weekly_expected_points/wk2_23_DK.csv')
df[['RBrank', 'WRrank', 'TErank', 'FLEXrank']] = df[['RBrank', 'WRrank', 'TErank', 'FLEXrank']].fillna(500)

cell_styles = {
            # Set of rules
            "styleConditions": [
                {
                    "condition": "params.value >=20",
                    "style": {"color": "green"},
                },
                {
                    "condition": "params.value <= 10",
                    "style": {"color": "violet"},
                },
            ],
        }
cell_styles2 = {
            # Set of rules
            "styleConditions": [
                {
                    "condition": "params.value >=2.6",
                    "style": {"color": "green"},
                },
                {
                    "condition": "params.value <= 1.8",
                    "style": {"color": "violet"},
                },
            ],
        }
cell_styles3 = {
            # Set of rules
            "styleConditions": [
                {
                    "condition": "params.value != 1.2023",
                    "style": {"color": "violet"},
                },
            ],
        }



table = dag.AgGrid(
    id="my-table",
    rowData=df.to_dict("records"),                                                          # **need it
    columnDefs=[
        {"field": "Name", "pinned": 'left'},
        {"field": "Roster Position"},
        {"field": "Game Info"},
        {"field": "TeamAbbrev"},
        {"field": "AvgPointsPerGame", "filter": "agNumberColumnFilter",
         "cellStyle": cell_styles,
         "valueFormatter": {"function": "d3.format('.1f')(params.value)"}},
        {"field": "Salary", "filter": "agNumberColumnFilter"},
        {"field": "Pt_per_$1k (projected)", "filter": "agNumberColumnFilter", "cellStyle": cell_styles2,
         "valueFormatter": {"function": "d3.format('.2f')(params.value)"}},
        {"field": "predRush_yds", "filter": "agNumberColumnFilter",
         "valueFormatter": {"function": "d3.format('.1f')(params.value)"}},
        {"field": "predRushTD", "filter": "agNumberColumnFilter",
         "valueFormatter": {"function": "d3.format('.2f')(params.value)"}},
        {"field": "predRec", "filter": "agNumberColumnFilter",
         "valueFormatter": {"function": "d3.format('.1f')(params.value)"}},
        {"field": "predRec_yds", "filter": "agNumberColumnFilter",
         "valueFormatter": {"function": "d3.format('.1f')(params.value)"}},
        {"field": "predRec_TD", "filter": "agNumberColumnFilter",
         "valueFormatter": {"function": "d3.format('.2f')(params.value)"}},
        {"field": "pred_standard", "filter": "agNumberColumnFilter",
         "valueFormatter": {"function": "d3.format('.1f')(params.value)"}},
        {"field": "pred_halfPPR", "filter": "agNumberColumnFilter",
         "valueFormatter": {"function": "d3.format('.1f')(params.value)"}},
        {"field": "pred_PPR", "filter": "agNumberColumnFilter", "cellStyle": cell_styles,
         "valueFormatter": {"function": "d3.format('.1f')(params.value)"}},
        {"field": "Last Observed Pts PPR", "filter": "agNumberColumnFilter", "cellStyle": cell_styles,
         "valueFormatter": {"function": "d3.format('.1f')(params.value)"}},
        {"field": "Last Observed Week&Season", "filter": "agNumberColumnFilter", "cellStyle": cell_styles3,
         "valueFormatter": {"function": "d3.format('.4f')(params.value)"}},
        {"field": "RBrank", "filter": "agNumberColumnFilter"},
        {"field": "WRrank", "filter": "agNumberColumnFilter"},
        {"field": "TErank", "filter": "agNumberColumnFilter"},
        {"field": "FLEXrank", "filter": "agNumberColumnFilter"},
    ],                                          # **need it
    defaultColDef={"resizable": True, "sortable": True, "filter": True, "minWidth":115},
    columnSize="sizeToFit",
    dashGridOptions={"pagination": False},
    className="ag-theme-alpine-dark",  # https://dashaggrid.pythonanywhere.com/layout/themes
)

graph = dcc.Graph(id="my-graph", figure={})


app = Dash(__name__)
server = app.server
app.layout = html.Div([graph, table])


@app.callback(Output("my-graph", "figure"), Input("my-table", "virtualRowData"))
def display_cell_clicked_on(vdata):
    if vdata:
        dff = pd.DataFrame(vdata)
        return px.scatter(dff, x="Salary", y="pred_PPR", color="Roster Position",
                          color_discrete_map={'WR/FLEX': '#007BC7',
                                              'RB/FLEX': '#C60C30',
                                              'TE/FLEX': '#008f00'},
                          hover_data=df[['Name', 'Salary', 'pred_PPR', 'Pt_per_$1k (projected)']])
    else:
        return px.scatter(df, x="Salary", y="pred_PPR", color="Roster Position",
                          color_discrete_map={'WR/FLEX': '#007BC7',
                                              'RB/FLEX': '#C60C30',
                                              'TE/FLEX': '#008f00'},
                          hover_data=df[['Name', 'Salary', 'pred_PPR', 'Pt_per_$1k (projected)']])

if __name__ == "__main__":
    app.run_server(debug=True)

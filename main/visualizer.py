from dash import (
    html,
    dcc,
    Dash,
    Input,
    Output,
    callback,
)  # import dash to visualize web application
import plotly.express as px  # import plotly to create graph
import pandas as pd

BOOTSTRAP_CDN = (
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
)

# create instance of dash class
app = Dash(__name__, external_stylesheets=[BOOTSTRAP_CDN])

# create data frame from existing csv file
frame = pd.read_csv("outputs/merged_daily_sales_data.csv")
frame = frame.sort_values(by="date")  # sort data by date

# TODO: SPECIFY COLORS
COLORS = {"primary": "#001524", "secondary": "#15616d", "font": "#edf6f9"}


# TODO: generate_figure
def generate_figure(chart_data):
    line_chart = px.line(chart_data, x="date", y="sales", title="", color="region")
    line_chart.update_layout(
        plot_bgcolor=COLORS["primary"],
        paper_bgcolor=COLORS["primary"],
        font_color=COLORS["font"],
        showlegend=False,
    )
    return line_chart


# TODO: visualize
visualization = dcc.Graph(id="visual", figure=generate_figure(frame))

# TODO: create header
header = html.Div(
    children=[
        html.Nav(
            [
                html.Div(
                    [
                        html.Span(
                            children="Sales Data Visualization",
                            className="navbar-brand mb-0 h1 fs-3",
                        )
                    ],
                    className="container-fluid d-flex justify-content-center",
                )
            ],
            className="navbar bg-body-tertiary",
        )
    ]
)

# TODO: add a region picker
region_picker = dcc.RadioItems(
    options=[
        {"label": "North", "value": "north"},
        {"label": "South", "value": "south"},
        {"label": "East", "value": "east"},
        {"label": "West", "value": "west"},
        {"label": "All", "value": "all"},
    ],
    value="north",
    id="region_picker",
    className="btn-group m-3",
    inline=True,
    inputClassName="btn-check",
    labelClassName="btn btn-outline-primary",
)

wrapper = html.Div([html.H3("Select a region: "), region_picker])


# TODO: region picker callback
@callback(Output(visualization, "figure"), Input(region_picker, "value"))
def update_graph(region):
    if region == "all":
        data = frame
    else:
        data = frame[frame["region"] == region]

    figure = generate_figure(data)
    return figure


# TODO: app layout
app.layout = html.Div(
    [header, visualization, wrapper],
    style={
        "text-align": "center",
    },
)

# start the app
if __name__ == "__main__":
    app.run_server(debug=True)

from dash import html, dcc, Dash  # import dash to visualize web application
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
# TODO: generate_figure
# TODO: visualize
# TODO: create header
# TODO: add a region picker
# TODO: region picker callback
# TODO: app layout

# figure of graph - line
fig = px.line(frame, x="date", y="sales", color="region")

# plot data
plot_layout = {
    "title": "",
    "margin": {"t": 2, "b": 2, "l": 2, "r": 2},
    # "font": {"size": 12, "color": "white"},
}

# update the layout of the graph
fig.update_layout(plot_layout)

# layout of the app
app.layout = html.Div(
    children=[
        html.Nav(
            children=[
                html.Div(
                    children=[
                        html.A(
                            children="Sales Data Visualization",
                            className="navbar-brand text-white",
                            href="#",
                        )
                    ],
                    className="container-fluid d-flex justify-content-center",
                )
            ],
            className="navbar text-center",
            style={"background-color": "grey", "color": "white"},
        ),
        # html.H1(children="Sales data visualization in dash"),
        html.Div(
            children="""
    Sales before and after the Pink Morsel price increase.
    """
        ),
        dcc.Graph(
            id="sales-graph",
            figure=fig,
        ),
        html.Div(
            children=[
                html.Button("North", className="btn btn-primary m-2"),
            ]
        ),
    ]
)

# start the app
if __name__ == "__main__":
    app.run_server(debug=True)

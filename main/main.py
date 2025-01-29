from dash import html, dcc, Dash  # import dash to visualize web application
import plotly.express as px  # import plotly to create graph
import pandas as pd


def readFile(file1: str, file2: str, file3: str):
    # read files
    frame_1 = pd.read_csv(file1)
    frame_2 = pd.read_csv(file2)
    frame_3 = pd.read_csv(file3)

    # concatinate two or more dataframes
    merge_df = pd.concat([frame_1, frame_2, frame_3])

    # drop values from merged data frame where product is not "pink morsel"
    filter_df = merge_df[merge_df["product"] == "pink morsel"].copy()

    # extract price
    new_price = []
    for val in filter_df["price"].values:
        data = val.split("$")  # strip dollar $
        new_price.append(float(data[1]))  # typecast to float

    # add a new column sales by mulitplying price and quantity
    filter_df.loc[:, "sales"] = filter_df["quantity"] * new_price

    # drop non-required columns
    filter_df.drop(columns=["price", "quantity"], axis=1, inplace=True)

    # format sales values by adding $
    filter_df.loc[:, "sales"] = (
        filter_df["sales"].astype(float).apply(lambda x: f"${x:.2f}")
    )

    # copy dataframe to avoid issues
    new_df = filter_df.copy()

    # write to csv file
    new_df.to_csv("outputs/merged_daily_sales_data.csv", index=False)


def visualize_data():
    # create instance of dash class
    app = Dash(__name__)

    # create data frame from existing csv file
    frame = pd.read_csv("outputs/merged_daily_sales_data.csv")
    frame = frame.sort_values(by="date")  # sort data by date

    # figure of graph - line
    fig = px.line(
        frame,
        x="date",
        y="sales",
        color="region",
    )

    # layout of the app
    app.layout = html.Div(
        children=[
            html.H1(children="Sales data visualization in dash"),
            html.Div(
                children="""
        Sales before and after the Pink Morsel price increase."
        """
            ),
            dcc.Graph(id="sales-graph", figure=fig),
        ]
    )

    # runserver
    app.run(debug=True)


def main():
    visualize_data()


if __name__ == "__main__":
    main()

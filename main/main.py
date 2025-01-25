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
    new_df.to_csv("outputs/merged_daily_sales_data.csv")


def main():
    readFile(
        "data/daily_sales_data_0.csv",
        "data/daily_sales_data_1.csv",
        "data/daily_sales_data_2.csv",
    )


if __name__ == "__main__":
    main()

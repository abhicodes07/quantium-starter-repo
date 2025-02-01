# import csv and pandas library
import csv
import pandas as pd


def readFileList(file: str):
    """
    Each row returned by the reader is a list of String elements
    containing the data found by removing the delimiters.
    """
    # open file (daily_sales_data_0)
    with open(file, mode="r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")  # csv.reader returns file object
        line = 0

        for row in reader:
            if line == 0:
                # first row returned contains the column names
                print(f"Columns : {', '.join(row)} ")
                line += 1
            else:
                # print data
                print(
                    f"On {row[3]} product was sold for {row[1]} in {row[4]} region with {row[2]} quantity."
                )
                line += 1
        print(f"\nProcessed {line} lines.")


def readFileDict(file: str):
    """
    The first line of the CSV file is assumed to contain
    the keys to use to build the dictionary.
    """
    with open(file, mode="r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        line = 0

        for row in reader:
            # first row returned contains the column names
            if line == 0:
                print(f"Columns: {', '.join(row)}")
                line += 1
            else:
                # print data
                print(
                    f"On {row['date']} product was sold for {row['price']} in {row['region']} with {row['quantity']} quantity."
                )
                line += 1
        print(f"\nProcessed {line} lines.")


def readFilePandas(file):
    # index_col : use a specific column as index
    # parse_dates : read data as a date
    frame = pd.read_csv(file, delimiter=",", index_col="product")
    regions = ["north"]
    mask = frame.region.isin(regions)
    print(mask)


def main():
    readFilePandas("outputs/merged_daily_sales_data.csv")


if __name__ == "__main__":
    main()

import pandas as pd

def readCSV():

    try:
        df = pd.read_csv('moduleInfoClassCodes.csv', sep=',', encoding="utf-8")
        return df

    except Exception:
        print("Could not open CSV file")


def searchForDepAndFac():
    df = readCSV()
    print(df)


if __name__ == '__main__':
    searchForDepAndFac()

import pandas as pd
import WebFormFiller as wf


# read in csv file
def readCSV():
    try:
        df = pd.read_csv('moduleInfoClassCodes.csv', sep=',', encoding="utf-8")
        return df

    except Exception:
        print("Could not open CSV file")


def searchForDepAndFac():
    df = readCSV()
    # Creates headers for department and faculty
    df['Department'] = ''
    df['Faculty'] = ''

    # loops all the rows of the csv file
    for index, row in df.iterrows():
        # Current module code
        mc = row['Module Code']

        # if module code is found search for it using webFormFiller and return the department and faculty
        if type(mc) == str:
            department, faculty = wf.fillForm(mc)
            row['Department'] = department
            row['Faculty'] = faculty

    writeToCSV(df)

# write to csv file
def writeToCSV(dataframe):
    dataframe.to_csv('moduleInfoAll.csv', sep=',', encoding="utf-8", index=False)


if __name__ == '__main__':
    searchForDepAndFac()

import pandas as pd
import WebFormFiller as wf


def readCSV():
    try:
        df = pd.read_csv('moduleInfoClassCodes.csv', sep=',', encoding="utf-8")
        return df

    except Exception:
        print("Could not open CSV file")


def searchForDepAndFac():
    df = readCSV()
    moudleCodes = df['Module Code']
    df['Department'] = ''
    df['Faculty'] = ''


    for index, row in df.iterrows():
        # Current module code
        mc = row['Module Code']
        if type(mc) == str:
             department, faculty = wf.fillForm(mc)
             row['Department'] = department
             row['Faculty'] = faculty


    writeToCSV(df)



def writeToCSV(dataframe):
        dataframe.to_csv('moduleInfoAll.csv', sep=',', encoding="utf-8", index=False)



# TODO potentially rewrite this with the old code because this is slow and doesn't work
# Maybe try and keep the dataframe stuff and make it work with the old code

if __name__ == '__main__':
    searchForDepAndFac()

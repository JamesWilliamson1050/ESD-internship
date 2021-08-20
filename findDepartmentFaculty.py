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
    print(df.columns)

    # TODO finish adding the faculty and department of a module
    # TODO Make sure that the department and faculty are being added as headers
    # Potential solution
    # Iterate over the df
    # For ever code that is a string pass it to the form filler function from webFormFiller module
    # Extract the department and faculty
    # Add the to data frame (Probably use the in build pandas function at and use the current index to do this)
    # Then you need to write the dataframe to a CSV file

    for mc in moudleCodes:
        if type(mc) == str:
            department, faculty = wf.fillForm(mc)
            df['Department'] = department
            break




if __name__ == '__main__':
    searchForDepAndFac()

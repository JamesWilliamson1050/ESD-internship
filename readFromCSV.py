import pandas
import openpyxl


# def convertToExcel():
#     csvName = 'WebOutputs.csv'
#     excelFile = pandas.read_csv('WebOutputs.csv')
#     excelFile = excelFile.to_excel('WebOutputs.xlsx', index=None, header=True)
#
#     print(excelFile)
#     return excelFile


def countYes(list):
    sdgList = [i for i in list if 'SDG' in i]

    sdgDict = {}
    for x in sdgList:
        count = 0
        print(df[x].values.tolist())





if __name__ == '__main__':
    df = pandas.read_excel('WebOutputs.xlsx')
    pandas.set_option('display.max_rows', df.shape[0] + 1)
    sdg1 = df["SDG1"]
    listDF = list(df)
    #print(list(tst))
    countYes(listDF)


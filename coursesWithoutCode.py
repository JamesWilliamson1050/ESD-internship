import csv


if __name__ == '__main__':

    with open("moduleInfo2codes.csv", 'r', encoding='utf-8') as csv_file:
        # reader = csv.DictReader.(csv_file)
        reader = csv.reader(csv_file)

        for row in reader:

            # print(type(reader))
            if row[0] == '':
                print(row[1].encode("utf-8"))

        csv_file.close()


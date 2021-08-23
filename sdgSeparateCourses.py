import csv

def readCSV():
    course = []
    # try:
    with open('SeparateCourses.csv', 'r', encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for r in reader:

            if r != [' ']:
                course.append(r)

            elif r == [' ']:
                separateModuleInfo(course)
                course.clear()

                # Pass info to another function

        csv_file.close()
    # except Exception:
    #     print("Could not find CSV file")


def separateModuleInfo(course):
    if len(course) >=1:
        courseTitle = course[0]
        modules = course[1:]


        # Write the course title to a csv file
        with open('sdgSeparateCourses.csv', 'a', encoding="utf-8", newline='') as sdgSeparate:
            writer = csv.writer(sdgSeparate)
            writer.writerow(courseTitle)


        for module in modules:
            moduleTitle = module[2]
            moduleDesc = module[3]
            degreeLevel = module[4]
            output = filterKeywords(moduleTitle, moduleDesc)

            for key in output.keys():
                with open('sdgSeparateCourses.csv', 'a', encoding="utf-8", newline='') as sdgSeparate:
                    writer = csv.writer(sdgSeparate)
                    writer.writerow([key] + [degreeLevel] + output[key])










def filterKeywords(moduleTitle, moduleDescription):
    sdg = {}
    output = {}
    moduleDescription = moduleDescription.lower().strip()
    with open("KEYWORDS.csv") as keywords_file:

        for inc, line in enumerate(keywords_file.readlines()):
            sdgNow = [word for word in line.lower().strip().split(',') if word not in ['', '\n', ' ']]
            sdg[inc + 1] = sdgNow

    keywords_file.close()

    sdgList = []

    for index in sdg.keys():

        if any(word in moduleDescription for word in sdg[index]):

            sdgList.append("YES")
        else:
            sdgList.append("NO")
    output[moduleTitle] = sdgList

    return output

def writeOutput(moduleTitle, moduleDesc, degreeLevel):

    with open('sdgSeparateCourses.csv', 'a', encoding="utf-8", newline='') as webOutputs:
        header = ['Module Title']
        toWrite = ''

        for sdgNo in range(1, 18):
            sdgHeader = 'SDG' + str(sdgNo)
            header.append(sdgHeader)

        writer = csv.writer(webOutputs)
        writer.writerow(header)
        output = filterKeywords(moduleTitle, moduleDesc)



        for key in output.keys():
            toWrite = toWrite + (key.replace(',', ';') + ',' + degreeLevel + ','.join(output[key]) +  '\n')
        webOutputs.write(toWrite)

def writeHeader():
    with open('sdgSeparateCourses.csv', 'w', encoding="utf-8", newline='') as sdgSeparate:
        header = ['Module Title', 'Degree Level']

        for sdgNo in range(1, 18):
            sdgHeader = 'SDG' + str(sdgNo)
            header.append(sdgHeader)

        writer = csv.writer(sdgSeparate)
        writer.writerow(header)

if __name__ == '__main__':
    writeHeader()
    readCSV()

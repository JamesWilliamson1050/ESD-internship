from tkinter import  *
from tkinter.filedialog import askopenfilename
import keywords

#Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

def browse(textEntry):
    filename = askopenfilename()
    textEntry.delete(0, END)
    textEntry.insert(0, filename)

# TODO figure out how to handle errors better
# TODO display errors using alert boxes
def runKeywords(fileInfo):
    try:
        if fileInfo:
            keywords.readCSV(fileInfo)
    except Exception:
        print("file not found")



def createGUI():
    window = Tk()
    window.title("Keyword Program")
    inputCSV = Label(window, text="Select CSV file", fg="black", font="none 12 bold").pack()

    fileInfo = Entry(window, width=50, bg="white")
    fileInfo.pack()
    browserButton = Button(window, text="Browse", command=lambda: browse(fileInfo))
    browserButton.pack()

    runButton = Button(window,text="Run", command=lambda: runKeywords(fileInfo.get()))
    runButton.pack()
    window.mainloop()

#filename = askopenfilename()

if __name__ == '__main__':
    # keywords.readCSV(filename)
    createGUI()
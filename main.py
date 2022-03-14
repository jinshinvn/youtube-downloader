from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube

def clickDownload():
    if (getURL.get() == ""):
        messagebox.showinfo("Url error", "Please enter the URL you want to download.")
        return
    elif (getDestination.get() == ""):
        messagebox.showinfo("Destination error", "Please enter the destionation you want to store files.")
        return

    listDownloadBoxSelective = listDownloadBox.curselection()
    quality = videos[listDownloadBoxSelective[0]]
    print(listDownloadBox)
    quality.download(getDestination.get())
    messagebox.showinfo("Downloading Finish", yt.title + " has been downloaded Sucessfully!!!")

def setURL():
    global yt
    global videos
    url = getURL.get()
    yt = YouTube(url)
    videos = yt.streams.filter(mime_type='video/mp4')
    count = 1
    for item in videos:
        listDownloadBox.insert(END, str(item.resolution) + " - " + str(item.is_progressive) + " - " + str(item) + "\n\n")
        count += 1

def clickBrowse():
    newDestination = filedialog.askdirectory()
    getDestination.set(newDestination)

def clickReset():
    getURL.set("")
    getDestination.set("")
    listDownloadBox.delete(0, END)

def generateFrame():
    global root
    root = Tk()
    root.title("YouTube Video Dowloader")
    root.geometry("786x400")
    root.resizable(False, False)

def generateLabel():
    urlLabel = Label(root, text="Enter URL:", font=("Times New Roman", 15)).grid(row=1, column=0, padx=10, pady=10)
    qualityLabel = Label(root, text="Quality:", font=("Times New Roman", 15)).grid(row=2, column=0, padx=10, pady=10)
    destinationLabel = Label(root, text="Destination folder:", font=("Times New Roman", 15)).grid(row=3, column=0, padx=10, pady=10)

generateFrame()
generateLabel()

getURL = StringVar()
urlEntry = Entry(root, font=("Times New Roman", 12), textvariable = getURL, width = 50, bd=3, relief=SOLID, borderwidth=1).grid(row=1, column=1, padx=10, pady=10)
getDestination = StringVar()
destinationEntry = Entry(root, font=("Times New Roman", 12), textvariable = getDestination, width = 50, bd=3, relief=SOLID, borderwidth=1).grid(row=3,column=1, padx=10, pady=10)

listDownloadBox = Listbox(root, font=("Times New Roman", 11), width = 57, height = 12, bd=3, relief=SOLID, borderwidth=1)
listDownloadBox.grid(row=2,column=1, padx=10, pady=10)

urlButton = Button(root, text = "Find", font=("Times New Roman", 10), width=15, relief=SOLID, borderwidth=1, command=setURL).grid(row=1, column=2, padx=10, pady=10)
browseButton = Button(root, text = "Browse", font=("Times New Roman", 10), width=15, relief=SOLID, borderwidth=1, command=clickBrowse).grid(row=3, column=2, padx=10, pady=10)
downloadButton = Button(root, text = "Download", font=("Times New Roman bold", 10), width=15, relief=SOLID, borderwidth=2, command=clickDownload).grid(row=4, column=1, padx=10, pady=10)
resetButton = Button(root, text = "Clear all",  font=("Times New Roman", 10), width=15, relief=SOLID, borderwidth=1, command=clickReset).grid(row=2, column=2, padx=10, pady=10)

root.mainloop()
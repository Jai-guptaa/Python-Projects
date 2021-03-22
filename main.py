from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
from tkinter import *
from pytube import *


file_size = 0




def progress(stream = None, chunk = None, file_handle = None, remaining = None):
    file_downloaded=(file_size-remaining)
    per = (file_downloaded/file_size) * 100
    btn.config(text="{} % downloaded".format(per))
    # print(text="{:00.0f} % downloaded".format(per))

def startDownload():
    global file_size
    try:
        url = urlfield.get()
        # print(url)
        # changing button text
        btn.config(text='Please Wait...')
        btn.config(state=DISABLED)
        path_save_video = askdirectory()
        # print(path_save_video)
        if path_save_video is None:
            print("Select Directory")
            return

        # creating youtube objects url
        ob = YouTube(url, on_progress_callback=progress)
        # All_streams= object.streams.all()
        # for s in All_streams:
        #     print(s)
        stram = ob.streams.first()
        file_size = stram.filesize
        vtitle.config(text=stram.title)
        vtitle.pack(side=TOP)
        print(file_size)
        stram.download(path_save_video)
        print("Done...")
        btn.config(text="start Download")
        btn.config(state=NORMAL)
        showinfo("Downloaded Finished", "Downloaded Successfully")
    except Exception as e:
        print(e)
        print("Error in Video Downloading")
        urlfield.delete(0, END)
        vtitle.pack_forget()


def startDownloadThread():
    # create thread
    thread = Thread(target=startDownload)
    thread.start()


# starting GUI Building
main = Tk()

# setting the title
main.title("Utube Downloader")

# set the icon
main.iconbitmap('icon.ico')

main.geometry("500x600")

# Icon
file = PhotoImage(file='newpng.png')

headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP, pady=25)

# urlField
urlfield = Entry(main, font=("verdana", 18), justify=CENTER)
urlfield.pack(side=TOP, fill=X, padx=15)

btn = Button(main, text="Start Download", font=("verdana", 18), relief = RIDGE, command=startDownloadThread)
btn.pack(side=TOP)
# video title
vtitle = Label(main, text="Video Title")
vtitle.pack(side=TOP)
main.mainloop()

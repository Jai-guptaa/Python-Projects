# https://www.youtube.com/watch?v=FsNPdhWmil4
def VideoUrl():
    DownloadingBarTextLable.configure(text=" ")
    DownloadingLabelResult.configure(text=" ")
    DownloadingSizeLabelResult.configure(text=" ")
    DownloadingLabelTimeLeft.configure(text=" ")
    DownloadingProgressBar.configure(value=0)
    getdetail = threading.Thread(target=getvideo)
    getdetail.start()

def getvideo():
    global streams
    ListBox.delete(0, END)
    url = urltext.get()
    data = pafy.new(url)
    streams = data.allstreams
    index = 1
    for i in streams:
        du = '{:00.1f}'.format(i.get_filesize()//(1024*1024))
        datas = str(index) + '.'.ljust(5, ' ') + str(i.quality).ljust(20, ' ') + str(i.extension).ljust(5, ' ') + str(i.mediatype) + ' ' + du.rjust(15, ' ') + "MB"
        ListBox.insert(END, datas)
        index += 1
def SelectCursor(evt):
    global downloadindex
    listboxdata = ListBox.get(ListBox.curselection())
    print(listboxdata)
    downloadstream = listboxdata[:3]
    downloadindex = int(''.join(x for x in downloadstream if x.isdigit()))


def DownloadVideo():
    getdata = threading.Thread(target=DownloadVideoData)
    getdata.start()

def DownloadVideoData():
    global downloadindex
    fgr = filedialog.askdirectory()
    DownloadingBarTextLable.configure(text="Downloading.....")
    def mycallback(total, recvd, ratio, rate, eta):
        global total12
        total12 = float('{:.3}'.format(total/(1024*1024)))
        DownloadingProgressBar.configure(maximum=total12)
        received1 = '{:.3} mb'.format(recvd / (1024 * 1024))
        eta1 = '{:.2f} sec'.format(eta)
        DownloadingSizeLabelResult.configure(text=total12)
        DownloadingLabelResult.configure(text=received1)
        DownloadingLabelTimeLeft.configure(text=eta1)
        DownloadingProgressBar['value'] = recvd/(1024*1024)

    streams[downloadindex].download(filepath=fgr, quiet=True, callback=mycallback)
    DownloadingBarTextLable.configure(text="Downloaded")


#####################################################################################################

def ChangeIntroLabelColor():
    ss = random.choice(colors)
    IntroLabel.configure(fg=ss)
    IntroLabel.after(20, ChangeIntroLabelColor)

from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import filedialog
import random
import threading
import pafy
root = Tk()
root['background']='#856ff8'
root.geometry('780x500')
root.title("Utube Downloader")
root.resizable(False, False)
root.attributes()
root.iconbitmap('icon.ico')

downloadindex = 0
total12 = 0
streams = ""
colors = ['red', 'pink','green','gold','blue','violet']
############################################################################################   ScrollBar
scrollbar = Scrollbar(root)
scrollbar.place(x=477, y=230, height=193, width=20)
############################################################################################  Entry
urltext = StringVar()
UrlEntry = Entry(root, textvariable=urltext, font=('arial', 20, 'italic bold'), width=31, bd=3)
UrlEntry.place(x=20, y=150)

############################################################################################  Labels
IntroLabel = Label(root, text='Welcome to Utube Video Downloader', width=36, relief='ridge', bd=4,
                   font=('chiller', 40, 'italic bold'), fg='red')
IntroLabel.place(x=10, y=23)
ChangeIntroLabelColor()
############################################################################################ Musics
btn= Label(root,text="Develop by : Jai & Ekjot",width=20,relief='ridge',
            font=('Arial',10,'bold'),fg="red")
btn.place(x=300,y=0)

ListBox = Listbox(root, yscrollcommand=scrollbar.set, width=50, height=10, font=('arial', 12, 'italic bold'),
                  relief='ridge', bd=2, highlightcolor="blue", highlightbackground="orange", highlightthickness=2)
ListBox.place(x=20, y=230)
ListBox.bind("<<ListboxSelect>>", SelectCursor)

scrollbar.configure(command=ListBox.yview)

DownloadingSizeLabel = Label(root, text='Total Size : ', font=('chiller', 20, 'italic bold'), bg='#856ff8')
DownloadingSizeLabel.place(x=500, y=240)

DownloadingLabel = Label(root, text='Downloaded : ', font=('chiller', 20, 'italic bold'), bg='#856ff8')
DownloadingLabel.place(x=500, y=290)

DownloadingTime = Label(root, text='Time Left  : ', font=('chiller', 20, 'italic bold'), bg='#856ff8')
DownloadingTime.place(x=500, y=340)

DownloadingSizeLabelResult = Label(root, text='', font=('arial', 15, 'italic bold'), bg='#856ff8')
DownloadingSizeLabelResult.place(x=650, y=245)

DownloadingLabelResult = Label(root, text='', font=('arial', 15, 'italic bold'), bg='#856ff8')
DownloadingLabelResult.place(x=650, y=295)

DownloadingLabelTimeLeft = Label(root, text='', font=('arial', 15, 'italic bold'), bg='#856ff8')
DownloadingLabelTimeLeft.place(x=650, y=345)

DownloadingBarTextLable = Label(root, text='Downloading bar', width=36, font=('chiller', 23, 'italic bold'), fg='red',
                    bg='#856ff8')
DownloadingBarTextLable.place(x=370, y=445)

DownloadingProgressBarLabel = Label(root, text='', width=36, font=('chiller', 40, 'italic bold'), fg='red', bg='#856ff8',
                     relief='raised')
DownloadingProgressBarLabel.place(x=20, y=445)


###########################################################################################  Progressbar

DownloadingProgressBar = Progressbar(DownloadingProgressBarLabel, orient=HORIZONTAL, value=0, length=100, maximum= total12)
DownloadingProgressBar.grid(row=0, column=0, ipadx=183, ipady=1)

#####################################################################################################  Buttons
ClickButton = Button(root, text='Enter Url And Click', font=('Arial', 11, 'italic bold'), bg='yellow', fg='Red',
                     activebackground='blue', width=23, bd=6, command=VideoUrl)
ClickButton.place(x=530, y=150)

DownloadButton = Button(root, text='Download', font=('Arial', 11, 'italic bold'), bg='#ff0000', fg='white',
                        activebackground='blue', width=23, bd=6, command=DownloadVideo)
DownloadButton.place(x=530, y=385)
################################################################################## Create Threads
root.mainloop()
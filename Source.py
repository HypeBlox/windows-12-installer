from tkinter import *
from PIL import ImageTk, Image
import requests
from itertools import count, cycle
from io import BytesIO

win = Tk()
win.title("Windows 12 Setup")

responseico = requests.get("https://cdn.discordapp.com/attachments/912359331817717841/1011668097826037790/image-removebg-preview_20.png")
ico = Image.open(BytesIO(responseico.content))
photo = ImageTk.PhotoImage(ico)
win.wm_iconphoto(True, photo)

class ImageLabel(Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

def crashed():
    wasd = Toplevel(win)
    wasd.title("bsod")
    frame2 = Frame(wasd)
    frame2.pack()
    frame2.place(anchor='nw', relx=0, rely=0)
    response = requests.get("https://cdn.discordapp.com/attachments/772470401057685544/1012828581015077005/unknown.png?size=4096")
    img2 = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
    label2 = Label(frame2, image = img2, borderwidth=0)
    label2.pack()
    label2.photo = img2
    def close_win(e):
        win.destroy()
    wasd.bind('<Escape>', lambda e: close_win(e))
    wasd.config(cursor="none")
    wasd.configure(bg="red")
    wasd.attributes('-fullscreen', True)

def precrash(x, labelname):
    x.destroy()
    response = requests.get("https://cdn.discordapp.com/attachments/979393895500763186/1013794131182632960/installer.png?size=4096")
    photo1 = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
    labelname.configure(image=photo1)
    labelname.photo = photo1

    response = requests.get("https://cdn.discordapp.com/attachments/979393895500763186/1013794131992137778/loading.gif?size=4096")
    gif = Image.open(BytesIO(response.content))
    img_label = ImageLabel(win, highlightthickness=0, borderwidth=0)
    img_label.pack()
    img_label.load(gif)
    img_label.place(x=185, y=136)

    win.after(9000,crashed)

response = requests.get("https://cdn.discordapp.com/attachments/979393895500763186/1013794131618832394/setup.png?size=4096")
img2 = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
label1 = Label(win, image = img2)
label1.place(x = 0, y = 0)
label1.photo = img2

win.geometry('800x550')

response = requests.get("https://cdn.discordapp.com/attachments/979392900993519646/1012714944778739753/install.png?size=4096")
img = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
btn=Button(win, image=img)
btn.configure(command=lambda:precrash(btn, label1), borderwidth=0)

btn.place(x=620, y=453)

win.configure(bg='blue', highlightthickness=0)
win.resizable(False,False)
win.mainloop()
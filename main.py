import tkinter
import PIL.Image, PIL.ImageTk #pip install pillow
import cv2 #pip install opencv2-python
from functools import partial
import threading
import time
import imutils

stream = cv2.VideoCapture("clip.mp4")
def play(speed):
    print(f"you clicked in play. Speed is {speed} ")
    
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
    grabbed, frame = stream.read()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)     

def pending(decision):
    frame = cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)  
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    time.sleep(3)

    frame = cv2.cvtColor(cv2.imread("sponcers.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)  
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    time.sleep(4)
    if decision == 'out':
        decisionImg = "out.png"
    else:   
        decisionImg = "notout.png"
    frame = cv2.cvtColor(cv2.imread(decisionImg),cv2.COLOR_BGR2RGB)    
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)  
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

def out():
    thread = threading.Thread(target=pending, args = ("out",))
    thread.daemon = 1
    thread.start()
    print("player is out")

def not_out():
    thread = threading.Thread(target=pending, args = ("not out",))
    thread.daemon = 1
    thread.start()
    print("player is not out")

# width & height of gui
SET_WIDTH = 850
SET_HEIGHT = 370

# tkinter gui start here
window = tkinter.Tk()
window.title("DRS review system")
cv_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()

# buttons to control playback
btn = tkinter.Button(window, text="<< previous (fast) ", width=50, command = partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< previous (slow) ", width=50, command = partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text=" next (slow) >>", width=50, command = partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text=" next (fast) >>", width=50, command = partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text=" give out ", width=50, command = out)
btn.pack()

btn = tkinter.Button(window, text=" give not out ", width=50,command = not_out)
btn.pack()


window.mainloop()
import camUtils

from Tkinter import *
from PIL import Image, ImageTk

class App:

    def __init__(self, master):
        self.master = master
        master.title("App ROV")
        master.geometry("700x450")

        self.checkButton = Checkbutton(master, text="Compress Videos", command=self.print_value, onvalue=1, offvalue=0)
        self.checkButton.pack()

        self.start_recording_button = Button(master, text="Start Recording", command=self.start_recording)
        self.start_recording_button.pack()

        self.start_camera_button = Button(master, text="Start Camera", command=self.start_camera)
        self.start_camera_button.pack()

        self.stop_recording_button = Button(master, text="Stop Recording", command=self.stop_recording)
        self.stop_recording_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        # self.video = Frame(master, bg='#000000')
        # self.video.pack()

    def start_recording(self):
        camUtils.startRecording()

    def start_camera(self):
        camUtils.startCamera()

    def stop_recording():
        camUtils.stopRecording()

    def print_value(self):
        print(self.checkButton.variable)
        print(var.get())

root = Tk()
app_gui = App(root)
root.mainloop()
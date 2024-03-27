import time 
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time()*1000))
    name = 'C:/Users/ayush/OneDrive/Desktop/ScreenShot app/Screenshots/{}.png'.format(name)
    img = pyautogui.screenshot(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = "Take ScreenShot",
    command=screenshot
)

button.pack(side = tk.LEFT)
close = tk.Button(
    frame,
    text = "Quit",
    command=quit
)
close.pack(side = tk.LEFT)

root.mainloop()
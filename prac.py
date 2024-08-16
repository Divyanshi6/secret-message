from tkinter import *

root = Tk()

# ("width x height")
root.geometry("334x465")  
# (width , height)

Label(root,text="MY FIRST GUI").pack()

def toggle_fullscreen(event=None):
    global fullscreen
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)
    return "break"

def end_fullscreen(event=None):
    global fullscreen
    fullscreen = False
    root.attributes("-fullscreen", False)
    return "break"

root =Tk()
fullscreen = False

# Bind the escape key to end fullscreen mode
root.bind("<Escape>", end_fullscreen)
# Bind the F11 key to toggle fullscreen mode
root.bind("<F11>", toggle_fullscreen)

# Start in fullscreen mode
toggle_fullscreen()

root.mainloop()
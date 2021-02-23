#import module with extra commands
from tkinter import Tk, Canvas, PhotoImage
master = Tk()
master.title("Program Animate")

#creating the window
window = Canvas(master, width=500, height=400, background="#000000")
window.pack()


#refreshes the window
def refresh():
    window.after(10)
    window.update()


#Set up images
backgroundimage = PhotoImage(file="beach/beach.gif")
background = window.create_image(250, 200, image=backgroundimage)

crab = PhotoImage(file="beach/crab.gif")
crabanimate = window.create_image(180, 320, image=crab)

ship = PhotoImage(file="beach/ship.gif")
shipanimate = window.create_image(400, 150, image=ship)

octopus = PhotoImage(file="beach/octopus.gif")
octopusanimate = window.create_image(400,180, image=octopus)
#Animation
for canvas in range(0, 250):
    window.move(shipanimate, -1, 0)
    window.move(octopusanimate, -0.5, 0)
    refresh()

for canvas in range(0, 250):
    window.move(crabanimate, 1, -0.05)
    refresh()

#Last line
window.mainloop()
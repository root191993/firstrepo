
from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter  as tk
root = tk.Tk()
root.title("Image Slideshow")   
root.geometry("400x400")


# list of image path
image_path = [
    r"C:\Users\Pavan Kumar\Pictures\Screenshots\Screenshot 2026-06-02 080452.png",
    r"C:\Users\Pavan Kumar\Pictures\Screenshots\Screenshot 2026-05-27 210038.png",
    r"C:\Users\Pavan Kumar\Pictures\Screenshots\Screenshot 2026-07-07 205530.png",
]

# resize the image 1080*1080
image_size = (1080,1080)
images = [Image.open(path). resize(image_size) for path in image_path]
photo_images  =  [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()


def update():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)



def start_slideshow():

         for _ in range(len(image_path)):
            update()




play_button = tk.Button(root, text="Start", command=start_slideshow)
play_button.pack(anchor="nw")


root.mainloop()



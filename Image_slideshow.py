from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# List of image paths
image_paths = [
    r"/Users/0mpandey/Downloads/WhatsApp Image 2026-03-19 at 18.41.41.jpeg",
    r"/Users/0mpandey/Downloads/WhatsApp Image 2026-04-11 at 19.27.25.jpeg",
]

# Resize images
image_size = (1080, 1080)

images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

# Label to display images
label = tk.Label(root)
label.pack()

# Create slideshow cycle
slideshow = cycle(photo_images)

# Function to update image
def update_image():
    photo = next(slideshow)
    label.config(image=photo)
    label.image = photo  # Keep reference
    root.after(3000, update_image)  # Change image every 3 seconds

# Function to start slideshow
def start_slideshow():
    update_image()

# Play button
play_button = tk.Button(root, text="Play Slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()
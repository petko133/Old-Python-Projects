from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont


def img_file():
    file = filedialog.askopenfilename()

    with Image.open(file) as img:
        global resized_img
        global new_image
        resized_img = img.resize((600, 400), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_img)
        canvas = Canvas(window, width=600, height=400)
        canvas.create_image(1, 1, anchor=NW, image=new_image)
        canvas.grid(row=3, column=0, columnspan=3, pady=10)


def watermarking():
    global canvas_image
    global im
    im = resized_img
    width, height = im.size

    draw = ImageDraw.Draw(im)

    text = text_entry.get()
    size = font_size.get()

    font = ImageFont.truetype('arial.ttf', int(size))
    textwidth, textheight = draw.textsize(text, font)

    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    draw.text((x, y), text, font=font)
    canvas_image = ImageTk.PhotoImage(im)
    canvas = Canvas(window, width=600, height=400)
    canvas.create_image(1, 1, anchor=NW, image=canvas_image)
    canvas.grid(row=3, column=0, columnspan=3, pady=10)

def save_img():
    im.save("D:/", "png")

window = Tk()
window.title("Watermarking")
window.config(bg="#398AB9", padx=20, pady=20)
window.minsize(300, 400)

label = Label(text="Imported image")
label.config(bg="#398AB9", fg="white")
label.grid(row=0, column=0, padx=10)

import_button = Button(text="Import Picture", command=img_file)
import_button.grid(row=0, column=1, padx=10)

watermark_button = Button(text="Import Watermark", command=watermarking)
watermark_button.grid(row=0, column=2, padx=10)

save_button = Button(text="Save Image", command=save_img)
save_button.grid(row=1, column=2, padx=10)

watermark_label = Label(text="Write the watermark")
watermark_label.config(bg="#398AB9", fg="white")
watermark_label.grid(row=1, column=0, padx=10)

text_entry = Entry(width=15)
text_entry.grid(column=1, row=1)
text_entry.focus()

font_label = Label(text="Size font")
font_label.config(bg="#398AB9", fg="white")
font_label.grid(row=2, column=0, padx=10)

font_size = Entry(width=10)
font_size.grid(column=1, row=2)

window.mainloop()
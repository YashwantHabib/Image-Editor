from customtkinter import *
import cv2
import numpy as np
import customtkinter
from PIL import Image, ImageTk

app = customtkinter.CTk()
app.geometry("1000x600")
app.resizable(0,0)
set_default_color_theme("dark-blue")
set_appearance_mode("light")

# Sidebar
sidebar = customtkinter.CTkFrame(master=app, width=70, height=600, fg_color="transparent", corner_radius=0)
sidebar.pack_propagate(0)
sidebar.pack(fill="y", anchor="w", side="left")

# Tool
tool = customtkinter.CTkFrame(master=app, width=230, height=600, fg_color="transparent", corner_radius=0)
tool.pack_propagate(0)  # Disable geometry propagation
tool.pack(side="left", fill="y")  # Fill the entire left side

# Canvas Frame
canvasFrame = customtkinter.CTkFrame(master=app, width=700, height=60, fg_color="transparent", corner_radius=0)
canvasFrame.pack_propagate(0)
canvasFrame.pack(side="right", fill="both", expand=True)



def flip_horizontally():
    global img
    img=cv2.flip(img,1)
    update_image()

def flip_vertically():
    global img
    img=cv2.flip(img,0)
    update_image()

def rotate_clockwise():
    global img
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    update_image()

def rotate_anticlockwise():
    global img
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    update_image()

cropping = False
drawing = False
draw_color= (43, 57, 192)
last_x, last_y = None, None
rect_start_x, rect_start_y = None, None
rect = None
draw = False

def set_color(new_color):
    global draw_color
    draw_color = new_color

def on_mouse_down(event):
    global rect_start_x, rect_start_y, rect, cropping, draw, last_x, last_y, drawing
    if cropping:
        rect_start_x, rect_start_y = event.x, event.y
        rect = canvas_img.create_rectangle(rect_start_x, rect_start_y, rect_start_x, rect_start_y, outline='green')
    if drawing:
        draw = True
        last_x, last_y = event.x, event.y

def on_mouse_move(event):
    global rect_start_x, rect_start_y, rect, cropping, img, draw_color, last_x, last_y, drawing
    if cropping and rect:
        if rect:
            canvas_img.coords(rect, rect_start_x, rect_start_y, event.x, event.y)
    if drawing and draw:
        x, y = event.x, event.y
        cv2.line(img, (last_x, last_y), (x, y), draw_color, 2)
        last_x, last_y = x, y
        update_image()

def on_mouse_up(event):
    global img, rect_start_x, rect_start_y, rect, cropping, draw
    if cropping:
        rect_end_x, rect_end_y = event.x, event.y
        if rect:
            canvas_img.delete(rect)
            rect = None
            roi = img[rect_start_y:rect_end_y, rect_start_x:rect_end_x]
            img = roi
            img = cv2.resize(img, (800, 600))
            update_image()
        cropping = False
    if drawing:
        draw = False




# Functions to change and update button colors
def change_toolbar(clicked_button):
    global cropping, drawing
    # Remove all existing widgets from the tool frame
    for widget in tool.winfo_children():
        widget.destroy()
    # Update button colors
    for button in sidebar_buttons:
        button.configure(fg_color="#fff")
    clicked_button.configure(fg_color="#fa814d")

    if clicked_button == crop_button:
        crop_update()
        cropping = True
        drawing = False
    elif clicked_button == filter_button:
        filter_update()
        cropping = False
        drawing = False
    elif clicked_button == doodle_button:
        doodle_update()
        cropping = False
        drawing = True
    elif clicked_button == resize_button:
        resize_update()
        cropping = False
        drawing = False
    elif clicked_button == text_button:
        text_update()
        cropping = False
        drawing = False

def filter_update():
    CTkLabel(master=tool, text="Filter", font=("Corbel Bold", 24), width=220, anchor="w").grid(row=0, column=0, sticky="nw", pady=(100,0), padx=5, columnspan=7)

def doodle_update():
    CTkLabel(master=tool, text="Doodle", font=("Corbel Bold", 24), width=220, anchor="w").grid(row=0, column=0, sticky="nw", pady=(100,0), padx=5, columnspan=7)
    CTkLabel(master=tool, text=f"Choose Color", font=("Corbel Bold", 18)).grid(row=1, column=0, sticky="nw", pady=20, padx=5, columnspan=3)
    col1_button = CTkButton(master=tool, text="", fg_color="#C0392B", width=28, height=28, hover_color="#C0392B", corner_radius=20, border_color="black", border_width=1, anchor="w", command=lambda: set_color((43, 57, 192)))
    col1_button.grid(row=2, column=0, sticky="nw", pady=5, padx=5)
    col2_button = CTkButton(master=tool, text="", fg_color="#9B59B6", width=28, height=28, hover_color="#9B59B6", corner_radius=20, border_color="black", border_width=1, anchor="w", command=lambda: set_color((182, 89, 155)))
    col2_button.grid(row=2, column=1, sticky="nw", pady=5, padx=5)
    col3_button = CTkButton(master=tool, text="", fg_color="#2980B9", width=28, height=28, hover_color="#2980B9", corner_radius=20, border_color="black", border_width=1, anchor="w", command=lambda: set_color((185, 128, 41)))
    col3_button.grid(row=2, column=2, sticky="nw", pady=5, padx=5)
    col4_button = CTkButton(master=tool, text="", fg_color="#1ABC9C", width=28, height=28, hover_color="#1ABC9C", corner_radius=20, border_color="black", border_width=1, anchor="w", command=lambda: set_color((156, 188, 26)))
    col4_button.grid(row=3, column=0, sticky="nw", pady=5, padx=5)
    col5_button = CTkButton(master=tool, text="", fg_color="#27AE60", width=28, height=28, hover_color="#27AE60", corner_radius=20, border_color="black", border_width=1, anchor="w", command=lambda: set_color((96, 174, 39)))
    col5_button.grid(row=3, column=1, sticky="nw", pady=5, padx=5)
    col6_button = CTkButton(master=tool, text="", fg_color="#F1C40F", width=28, height=28, hover_color="#F1C40F", corner_radius=20, border_color="black", border_width=1, anchor="w", command=lambda: set_color((15, 196, 241)))
    col6_button.grid(row=3, column=2, sticky="nw", pady=5, padx=5)
    col7_button = CTkButton(master=tool, text="", fg_color="#E67E22", width=28, height=28, hover_color="#E67E22", corner_radius=20, border_color="black", border_width=1, anchor="w", command=lambda: set_color((34, 126, 230)))
    col7_button.grid(row=4, column=0, sticky="nw", pady=5, padx=5)
    col8_button = CTkButton(master=tool, text="", fg_color="#ECF0F1", width=28, height=28, hover_color="#ECF0F1", corner_radius=20, border_color="black", border_width=1, anchor="w", command=lambda: set_color((241, 240, 236)))
    col8_button.grid(row=4, column=1, sticky="nw", pady=5, padx=5)
    col9_button = CTkButton(master=tool, text="", fg_color="#95A5A6", width=28, height=28, hover_color="#95A5A6", corner_radius=20, border_color="black", border_width=1, anchor="w", command=lambda: set_color((166, 165, 149)))
    col9_button.grid(row=4, column=2, sticky="nw", pady=5, padx=5)
    col10_button = CTkButton(master=tool, text="", fg_color="#34495E", width=28, height=28, hover_color="#34495E", corner_radius=20, border_color="black", border_width=1, anchor="w", command=lambda: set_color((94, 73, 52)))
    col10_button.grid(row=5, column=0, sticky="nw", pady=5, padx=5)
    col11_button = CTkButton(master=tool, text="", fg_color="#DE3163", width=28, height=28, hover_color="#DE3163", corner_radius=20, border_color="black", border_width=1, anchor="w", command=lambda: set_color((99, 49, 222)))
    col11_button.grid(row=5, column=1, sticky="nw", pady=5, padx=5)
    col12_button = CTkButton(master=tool, text="", fg_color="#000000", width=28, height=28, hover_color="#000000", corner_radius=20, border_color="black", border_width=1, anchor="w", command=lambda: set_color((0, 0, 0)))
    col12_button.grid(row=5, column=2, sticky="nw", pady=5, padx=5)
    col13_button = CTkButton(master=tool, text="", fg_color="#00FFFF", width=28, height=28, hover_color="#00FFFF", corner_radius=20, border_color="black", border_width=1, anchor="w", command=lambda: set_color((255, 255, 0)))
    col13_button.grid(row=6, column=0, sticky="nw", pady=5, padx=5)
    col14_button = CTkButton(master=tool, text="", fg_color="#4B5320", width=28, height=28, hover_color="#4B5320", corner_radius=20, border_color="black", border_width=1, anchor="w", command=lambda: set_color((32, 83, 75)))
    col14_button.grid(row=6, column=1, sticky="nw", pady=5, padx=5)
    col15_button = CTkButton(master=tool, text="", fg_color="#FFFFCC", width=28, height=28, hover_color="#FFFFCC", corner_radius=20, border_color="black", border_width=1, anchor="w", command=lambda: set_color((204, 255, 255)))
    col15_button.grid(row=6, column=2, sticky="nw", pady=5, padx=5)
    

def resize_update():
    CTkLabel(master=tool, text="Resize", font=("Corbel Bold", 24), width=220, anchor="w").grid(row=0, column=0, sticky="nw", pady=(100,0), padx=5, columnspan=7)
    CTkLabel(master=tool, text="Percentage", font=("Corbel Bold", 18)).grid(row=1, column=0, sticky="nw", pady=20, padx=5, columnspan=2)
    
    percentage = CTkLabel(master=tool, text="50%", font=("Corbel Bold", 18))
    percentage.grid(row=3, column=0, sticky="n", pady=10, padx=5, columnspan=2)
    
    def slider_event(value):
        percentage.configure(text=f"{int(value)}%")
    
    slider = customtkinter.CTkSlider(master=tool, from_=0, to=100, button_color="#fa814d", button_hover_color="#fa814d", progress_color="#fa814d", command=slider_event)
    slider.grid(row=2, column=0, sticky="nw", pady=10, padx=5, columnspan=2)

    def resize_button_event():
        print("button pressed")

    resize_button = customtkinter.CTkButton(tool, text="Resize",font=("Corbel", 18), anchor="center", fg_color="#fa814d", hover_color="#fa814d", text_color="black", command=resize_button_event)
    resize_button.grid(row=4, column=0, sticky="n" , columnspan=3)


    


def text_update():
    CTkLabel(master=tool, text="Text", font=("Corbel Bold", 24), width=220, anchor="w").grid(row=0, column=0, sticky="nw", pady=(100,0), padx=5, columnspan=7)
    CTkLabel(master=tool, text="Enter Text", font=("Corbel Bold", 18)).grid(row=1, column=0, sticky="nw", pady=20, padx=5, columnspan=2)
    entry = customtkinter.CTkEntry(tool, placeholder_text="Text", border_color="#fa814d")
    entry.grid(row=2, column=0, sticky="nw", pady=(5,15), padx=5, columnspan=2)
    select_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\selection.png")
    select_img = CTkImage(dark_image=select_img_data, light_image=select_img_data)
    text_col1_button = CTkButton(master=tool, text="", fg_color="#C0392B", width=28, height=28, hover_color="#C0392B", corner_radius=20, border_color="black", border_width=1, anchor="w")
    text_col1_button.grid(row=3, column=0, sticky="nw", pady=5, padx=5)
    text_col2_button = CTkButton(master=tool, text="", fg_color="#9B59B6", width=28, height=28, hover_color="#9B59B6", corner_radius=20, border_color="black", border_width=1, anchor="w")
    text_col2_button.grid(row=3, column=1, sticky="nw", pady=5, padx=5)
    text_col3_button = CTkButton(master=tool, text="", fg_color="#2980B9", width=28, height=28, hover_color="#2980B9", corner_radius=20, border_color="black", border_width=1, anchor="w")
    text_col3_button.grid(row=3, column=2, sticky="nw", pady=5, padx=5)
    text_col4_button = CTkButton(master=tool, text="", fg_color="#1ABC9C", width=28, height=28, hover_color="#1ABC9C", corner_radius=20, border_color="black", border_width=1, anchor="w")
    text_col4_button.grid(row=4, column=0, sticky="nw", pady=5, padx=5)
    text_col5_button = CTkButton(master=tool, text="", fg_color="#27AE60", width=28, height=28, hover_color="#27AE60", corner_radius=20, border_color="black", border_width=1, anchor="w")
    text_col5_button.grid(row=4, column=1, sticky="nw", pady=5, padx=5)
    text_col6_button = CTkButton(master=tool, text="", fg_color="#F1C40F", width=28, height=28, hover_color="#F1C40F", corner_radius=20, border_color="black", border_width=1, anchor="w")
    text_col6_button.grid(row=4, column=2, sticky="nw", pady=5, padx=5)
    text_col7_button = CTkButton(master=tool, text="", fg_color="#E67E22", width=28, height=28, hover_color="#E67E22", corner_radius=20, border_color="black", border_width=1, anchor="w")
    text_col7_button.grid(row=5, column=0, sticky="nw", pady=5, padx=5)
    text_col8_button = CTkButton(master=tool, text="", fg_color="#ECF0F1", width=28, height=28, hover_color="#ECF0F1", corner_radius=20, border_color="black", border_width=1, anchor="w")
    text_col8_button.grid(row=5, column=1, sticky="nw", pady=5, padx=5)
    text_col9_button = CTkButton(master=tool, text="", fg_color="#000000", width=28, height=28, hover_color="#000000", corner_radius=20, border_color="black", border_width=1, anchor="w")
    text_col9_button.grid(row=5, column=2, sticky="nw", pady=5, padx=5)

def crop_update():
    CTkLabel(master=tool, text=f"Crop", font=("Corbel Bold", 24), width=220, anchor="w").grid(row=0, column=0, sticky="nw", pady=(100,0), padx=5, columnspan=7)
    CTkLabel(master=tool, text=f"Select cropping area", font=("Corbel Bold", 18)).grid(row=1, column=0, sticky="nw", pady=20, padx=5, columnspan=2)
    
    CTkLabel(master=tool, text=f"Flip", font=("Corbel Bold", 18)).grid(row=2, column=0, sticky="nw", pady=20, padx=5)
    horizontal_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\mirror-horizontally.png")
    horizontal_img = CTkImage(dark_image=horizontal_img_data, light_image=horizontal_img_data)
    horizontal_button = CTkButton(master=tool, image=horizontal_img, text="", fg_color="transparent", width=28, height=28, hover_color="#fff8f5", anchor="w", command=flip_horizontally)
    horizontal_button.grid(row=3, column=0, sticky="nw", pady=0, padx=5)
    vertical_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\mirror-vertically.png")
    vertical_img = CTkImage(dark_image=vertical_img_data, light_image=vertical_img_data)
    vertical_button = CTkButton(master=tool, image=vertical_img, text="", fg_color="transparent", width=28, height=28, hover_color="#fff8f5", anchor="w", command=flip_vertically)
    vertical_button.grid(row=3, column=1, sticky="nw", pady=0, padx=5)
    CTkLabel(master=tool, text=f"Rotate", font=("Corbel Bold", 18)).grid(row=4, column=0, sticky="nw", pady=20, padx=5)
    anticlock_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\rotate-left.png")
    anticlock_img = CTkImage(dark_image=anticlock_img_data, light_image=anticlock_img_data)
    anticlock_button = CTkButton(master=tool, image=anticlock_img, text="", fg_color="transparent", width=28, height=28, hover_color="#fff8f5", anchor="w", command=rotate_anticlockwise)
    anticlock_button.grid(row=5, column=0, sticky="nw", pady=0, padx=5)
    clock_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\rotate-right.png")
    clock_img = CTkImage(dark_image=clock_img_data, light_image=clock_img_data)
    clock_button = CTkButton(master=tool, image=clock_img, text="", fg_color="transparent", width=28, height=28, hover_color="#fff8f5", anchor="w", command=rotate_clockwise)
    clock_button.grid(row=5, column=1, sticky="nw", pady=0, padx=5)

# Sidebar Buttons
sidebar_buttons = []

# Filter Button
filter_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\graphic-style.png")
filter_img = CTkImage(dark_image=filter_img_data, light_image=filter_img_data)
filter_button = CTkButton(master=sidebar, image=filter_img, text="", fg_color="#fa814d", width=30, height=30, hover_color="#ffdbd9", anchor="w", command=lambda: change_toolbar(filter_button))
filter_button.pack(anchor="center", ipady=5, pady=(150, 0))
sidebar_buttons.append(filter_button)

# Crop Button
crop_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\tool-crop.png")
crop_img = CTkImage(dark_image=crop_img_data, light_image=crop_img_data)
crop_button = CTkButton(master=sidebar, image=crop_img, text="", fg_color="#fff", width=30, height=30, hover_color="#ffdbd9", anchor="w", command=lambda: change_toolbar(crop_button))
crop_button.pack(anchor="center", ipady=5, pady=(16, 0))
sidebar_buttons.append(crop_button)

# Doodle Button
doodle_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\scribble.png")
doodle_img = CTkImage(dark_image=doodle_img_data, light_image=doodle_img_data)
doodle_button = CTkButton(master=sidebar, image=doodle_img, text="", fg_color="#fff", width=30, height=30, hover_color="#ffdbd9", anchor="w", command=lambda: change_toolbar(doodle_button))
doodle_button.pack(anchor="center", ipady=5, pady=(16, 0))
sidebar_buttons.append(doodle_button)

# Resize Button
resize_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\resize.png")
resize_img = CTkImage(dark_image=resize_img_data, light_image=resize_img_data)
resize_button = CTkButton(master=sidebar, image=resize_img, text="", fg_color="#fff", width=30, height=30, hover_color="#ffdbd9", anchor="w", command=lambda: change_toolbar(resize_button))
resize_button.pack(anchor="center", ipady=5, pady=(16, 0))
sidebar_buttons.append(resize_button)

# Text Button
text_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\text.png")
text_img = CTkImage(dark_image=text_img_data, light_image=text_img_data)
text_button = CTkButton(master=sidebar, image=text_img, text="", fg_color="#fff", width=30, height=30, hover_color="#ffdbd9", anchor="w", command=lambda: change_toolbar(text_button))
text_button.pack(anchor="center", ipady=5, pady=(16, 0))
sidebar_buttons.append(text_button)

# Initial Label
CTkLabel(master=tool, text=f"Filter", font=("Corbel Bold", 24), width=220, anchor="w").grid(row=0, column=0, sticky="nw", pady=(100,0), padx=5)

canvas_img = CTkCanvas(master=canvasFrame, width=800, height=600)
canvas_img.grid(row=0, column=0, sticky="nw", pady=20, padx=20, columnspan=7, rowspan=7)

def update_image():
    global tk_img
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    tk_img = ImageTk.PhotoImage(img_pil)
    canvas_img.create_image(0, 0, anchor='nw', image=tk_img)

img = cv2.imread(r"C:\Users\91984\Desktop\cgProj\Image-Editor\demo-img.jpg")
img = cv2.resize(img, (800, 600))  # Resize to fit your window if needed
update_image()



def open_image():
    global img, tk_img
    filepath = filedialog.askopenfilename()
    if not filepath:
        return
    img = cv2.imread(filepath)
    img = cv2.resize(img, (800, 600))  # Resize to fit your window if needed
    update_image()

def save_file():
    global img
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("BMP files", "*.bmp")])
    if file_path:
        cv2.imwrite(file_path, img)

open_button = customtkinter.CTkButton(master=canvasFrame, text="Open Image", fg_color="gray", hover_color="gray", width=100, height=40, font=("Corbel Bold", 16), command=open_image)
open_button.grid(row=8, column=5, sticky="e", padx=(0, 0), pady=(10, 10))

save_button = customtkinter.CTkButton(master=canvasFrame, text="Save Image", fg_color="#fc5e03", hover_color="#fc5e03", width=100, height=40, font=("Corbel Bold", 16), command=save_file)
save_button.grid(row=8, column=6, sticky="n", padx=(0, 0), pady=(10, 10))

# Bind mouse events to the canvas
canvas_img.bind("<ButtonPress-1>", on_mouse_down)
canvas_img.bind("<B1-Motion>", on_mouse_move)
canvas_img.bind("<ButtonRelease-1>", on_mouse_up)


app.mainloop()


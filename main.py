from customtkinter import *
import customtkinter
from PIL import Image

app = customtkinter.CTk()
app.geometry("1000x650")
app.resizable(0, 0)

set_default_color_theme("dark-blue")
set_appearance_mode("light")

# Sidebar
sidebar = customtkinter.CTkFrame(master=app, width=50, height=650, fg_color="transparent", corner_radius=0)
sidebar.pack_propagate(0)
sidebar.pack(fill="y", anchor="w", side="left")

# Tool
tool = customtkinter.CTkFrame(master=app, width=300, height=650, fg_color="transparent", corner_radius=0)
tool.pack_propagate(0)
tool.pack(side="left")

# Canvas Frame
canvasFrame = customtkinter.CTkFrame(master=app, width=650, height=650, fg_color="transparent", corner_radius=0)

# Functions to change label and update button colors
def change_label_and_color(label_text, clicked_button):
    # Remove all existing labels from the tool frame
    for widget in tool.winfo_children():
        if isinstance(widget, CTkLabel):
            widget.destroy()
    # Add a new label with the given text
    CTkLabel(master=tool, text=label_text, font=("Corbel Bold", 20)).pack(pady=(38, 0), padx=(10, 0), anchor="w")
    # Update button colors
    for button in sidebar_buttons:
        button.configure(fg_color="#fff")
    clicked_button.configure(fg_color="#fc633d")

# Sidebar Buttons
sidebar_buttons = []

# Filter Button
filter_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\graphic-style.png")
filter_img = CTkImage(dark_image=filter_img_data, light_image=filter_img_data)
filter_button = CTkButton(master=sidebar, image=filter_img, text="", fg_color="#fc633d", width=30, height=30, hover_color="#ffb3b3", anchor="w", command=lambda: change_label_and_color("Filter", filter_button))
filter_button.pack(anchor="center", ipady=5, pady=(150, 0))
sidebar_buttons.append(filter_button)

# Crop Button
crop_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\tool-crop.png")
crop_img = CTkImage(dark_image=crop_img_data, light_image=crop_img_data)
crop_button = CTkButton(master=sidebar, image=crop_img, text="", fg_color="#fff", width=30, height=30, hover_color="#ffb3b3", anchor="w", command=lambda: change_label_and_color("Crop", crop_button))
crop_button.pack(anchor="center", ipady=5, pady=(16, 0))
sidebar_buttons.append(crop_button)

# Doodle Button
doodle_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\scribble.png")
doodle_img = CTkImage(dark_image=doodle_img_data, light_image=doodle_img_data)
doodle_button = CTkButton(master=sidebar, image=doodle_img, text="", fg_color="#fff", width=30, height=30, hover_color="#ffb3b3", anchor="w", command=lambda: change_label_and_color("Doodle", doodle_button))
doodle_button.pack(anchor="center", ipady=5, pady=(16, 0))
sidebar_buttons.append(doodle_button)

# Resize Button
resize_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\resize.png")
resize_img = CTkImage(dark_image=resize_img_data, light_image=resize_img_data)
resize_button = CTkButton(master=sidebar, image=resize_img, text="", fg_color="#fff", width=30, height=30, hover_color="#ffb3b3", anchor="w", command=lambda: change_label_and_color("Resize", resize_button))
resize_button.pack(anchor="center", ipady=5, pady=(16, 0))
sidebar_buttons.append(resize_button)

# Text Button
text_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\text.png")
text_img = CTkImage(dark_image=text_img_data, light_image=text_img_data)
text_button = CTkButton(master=sidebar, image=text_img, text="", fg_color="#fff", width=30, height=30, hover_color="#ffb3b3", anchor="w", command=lambda: change_label_and_color("Text", text_button))
text_button.pack(anchor="center", ipady=5, pady=(16, 0))
sidebar_buttons.append(text_button)

# Initial Label
CTkLabel(master=tool, text="Filter", font=("Corbel Bold", 20)).pack(pady=(38, 0), padx=(10, 0), anchor="w")

app.mainloop()

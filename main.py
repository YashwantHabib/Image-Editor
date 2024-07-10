from customtkinter import *
import customtkinter
from PIL import Image

app = customtkinter.CTk()
app.geometry("1000x650")
set_default_color_theme("dark-blue")
set_appearance_mode("light")

# Sidebar
sidebar = customtkinter.CTkFrame(master=app, width=70, height=650, fg_color="transparent", corner_radius=0)
sidebar.pack_propagate(0)
sidebar.pack(fill="y", anchor="w", side="left")

# Tool
tool = customtkinter.CTkFrame(master=app, width=230, height=650, fg_color="transparent", corner_radius=0)
tool.pack_propagate(0)  # Disable geometry propagation
tool.pack(side="left", fill="both", expand=True)  # Fill the entire left side

# Canvas Frame
canvasFrame = customtkinter.CTkFrame(master=app, width=700, height=650, fg_color="transparent", corner_radius=0)
canvasFrame.pack()

# Functions to change and update button colors
def change_toolbar(clicked_button):
    # Remove all existing widgets from the tool frame
    for widget in tool.winfo_children():
        widget.destroy()
    # Update button colors
    for button in sidebar_buttons:
        button.configure(fg_color="#fff")
    clicked_button.configure(fg_color="#fa814d")

    if clicked_button == crop_button:
        crop_update()
    elif clicked_button == filter_button:
        filter_update()
    elif clicked_button == doodle_button:
        doodle_update()
    elif clicked_button == resize_button:
        resize_update()
    elif clicked_button == text_button:
        text_update()

def filter_update():
    CTkLabel(master=tool, text="Filter", font=("Corbel Bold", 24)).grid(row=0, column=0, sticky="nw", pady=(100,0), padx=5)

def doodle_update():
    CTkLabel(master=tool, text="Doodle", font=("Corbel Bold", 24)).grid(row=0, column=0, sticky="nw", pady=(100,0), padx=5, columnspan=2)
    CTkLabel(master=tool, text=f"Choose Color", font=("Corbel Bold", 18)).grid(row=1, column=0, sticky="nw", pady=20, padx=5, columnspan=3)
    col1_button = CTkButton(master=tool, text="", fg_color="#C0392B", width=28, height=28, hover_color="#C0392B", corner_radius=20, border_color="black", border_width=1, anchor="w")
    col1_button.grid(row=2, column=0, sticky="nw", pady=5, padx=5)
    col2_button = CTkButton(master=tool, text="", fg_color="#9B59B6", width=28, height=28, hover_color="#9B59B6", corner_radius=20, border_color="black", border_width=1, anchor="w")
    col2_button.grid(row=2, column=1, sticky="nw", pady=5, padx=5)
    col3_button = CTkButton(master=tool, text="", fg_color="#2980B9", width=28, height=28, hover_color="#2980B9", corner_radius=20, border_color="black", border_width=1, anchor="w")
    col3_button.grid(row=2, column=2, sticky="nw", pady=5, padx=5)
    col4_button = CTkButton(master=tool, text="", fg_color="#1ABC9C", width=28, height=28, hover_color="#1ABC9C", corner_radius=20, border_color="black", border_width=1, anchor="w")
    col4_button.grid(row=3, column=0, sticky="nw", pady=5, padx=5)
    col5_button = CTkButton(master=tool, text="", fg_color="#27AE60", width=28, height=28, hover_color="#27AE60", corner_radius=20, border_color="black", border_width=1, anchor="w")
    col5_button.grid(row=3, column=1, sticky="nw", pady=5, padx=5)
    col6_button = CTkButton(master=tool, text="", fg_color="#F1C40F", width=28, height=28, hover_color="#F1C40F", corner_radius=20, border_color="black", border_width=1, anchor="w")
    col6_button.grid(row=3, column=2, sticky="nw", pady=5, padx=5)
    col7_button = CTkButton(master=tool, text="", fg_color="#E67E22", width=28, height=28, hover_color="#E67E22", corner_radius=20, border_color="black", border_width=1, anchor="w")
    col7_button.grid(row=4, column=0, sticky="nw", pady=5, padx=5)
    col8_button = CTkButton(master=tool, text="", fg_color="#ECF0F1", width=28, height=28, hover_color="#ECF0F1", corner_radius=20, border_color="black", border_width=1, anchor="w")
    col8_button.grid(row=4, column=1, sticky="nw", pady=5, padx=5)
    col9_button = CTkButton(master=tool, text="", fg_color="#95A5A6", width=28, height=28, hover_color="#95A5A6", corner_radius=20, border_color="black", border_width=1, anchor="w")
    col9_button.grid(row=4, column=2, sticky="nw", pady=5, padx=5)
    col10_button = CTkButton(master=tool, text="", fg_color="#34495E", width=28, height=28, hover_color="#34495E", corner_radius=20, border_color="black", border_width=1, anchor="w")
    col10_button.grid(row=5, column=0, sticky="nw", pady=5, padx=5)
    col11_button = CTkButton(master=tool, text="", fg_color="#DE3163", width=28, height=28, hover_color="#DE3163", corner_radius=20, border_color="black", border_width=1, anchor="w")
    col11_button.grid(row=5, column=1, sticky="nw", pady=5, padx=5)
    col12_button = CTkButton(master=tool, text="", fg_color="#000000", width=28, height=28, hover_color="#000000", corner_radius=20, border_color="black", border_width=1, anchor="w")
    col12_button.grid(row=5, column=2, sticky="nw", pady=5, padx=5)
    col13_button = CTkButton(master=tool, text="", fg_color="#00FFFF", width=28, height=28, hover_color="#00FFFF", corner_radius=20, border_color="black", border_width=1, anchor="w")
    col13_button.grid(row=6, column=0, sticky="nw", pady=5, padx=5)
    col14_button = CTkButton(master=tool, text="", fg_color="#4B5320", width=28, height=28, hover_color="#4B5320", corner_radius=20, border_color="black", border_width=1, anchor="w")
    col14_button.grid(row=6, column=1, sticky="nw", pady=5, padx=5)
    col15_button = CTkButton(master=tool, text="", fg_color="#FFFFCC", width=28, height=28, hover_color="#FFFFCC", corner_radius=20, border_color="black", border_width=1, anchor="w")
    col15_button.grid(row=6, column=2, sticky="nw", pady=5, padx=5)
    

def resize_update():
    CTkLabel(master=tool, text="Resize", font=("Corbel Bold", 24)).grid(row=0, column=0, sticky="nw", pady=(100,0), padx=5)
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
    CTkLabel(master=tool, text="Text", font=("Corbel Bold", 24)).grid(row=0, column=0, sticky="nw", pady=(100,0), padx=5)
    CTkLabel(master=tool, text="Enter Text", font=("Corbel Bold", 18)).grid(row=1, column=0, sticky="nw", pady=20, padx=5, columnspan=2)
    entry = customtkinter.CTkEntry(tool, placeholder_text="Text", border_color="#fa814d")
    entry.grid(row=2, column=0, sticky="nw", pady=5, padx=5, columnspan=2)
    select_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\selection.png")
    select_img = CTkImage(dark_image=select_img_data, light_image=select_img_data)
    text_button = CTkButton(master=tool, image=select_img, text="", fg_color="transparent", width=28, height=28, hover_color="#fff8f5", anchor="w")
    text_button.grid(row=2, column=3, sticky="nw", pady=5, padx=5)

def crop_update():
    CTkLabel(master=tool, text=f"Crop", font=("Corbel Bold", 24)).grid(row=0, column=0, sticky="nw", pady=(100,0), padx=5)
    CTkLabel(master=tool, text=f"Selection Tool", font=("Corbel Bold", 18)).grid(row=1, column=0, sticky="nw", pady=20, padx=5, columnspan=2)
    select_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\selection.png")
    select_img = CTkImage(dark_image=select_img_data, light_image=select_img_data)
    select_button = CTkButton(master=tool, image=select_img, text="", fg_color="transparent", width=28, height=28, hover_color="#fff8f5", anchor="w")
    select_button.grid(row=1, column=2, sticky="nw", pady=20, padx=5)
    CTkLabel(master=tool, text=f"Flip", font=("Corbel Bold", 18)).grid(row=2, column=0, sticky="nw", pady=20, padx=5)
    horizontal_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\mirror-horizontally.png")
    horizontal_img = CTkImage(dark_image=horizontal_img_data, light_image=horizontal_img_data)
    horizontal_button = CTkButton(master=tool, image=horizontal_img, text="", fg_color="transparent", width=28, height=28, hover_color="#fff8f5", anchor="w")
    horizontal_button.grid(row=3, column=0, sticky="nw", pady=0, padx=5)
    vertical_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\mirror-vertically.png")
    vertical_img = CTkImage(dark_image=vertical_img_data, light_image=vertical_img_data)
    vertical_button = CTkButton(master=tool, image=vertical_img, text="", fg_color="transparent", width=28, height=28, hover_color="#fff8f5", anchor="w")
    vertical_button.grid(row=3, column=1, sticky="nw", pady=0, padx=5)
    CTkLabel(master=tool, text=f"Rotate", font=("Corbel Bold", 18)).grid(row=4, column=0, sticky="nw", pady=20, padx=5)
    anticlock_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\rotate-left.png")
    anticlock_img = CTkImage(dark_image=anticlock_img_data, light_image=anticlock_img_data)
    anticlock_button = CTkButton(master=tool, image=anticlock_img, text="", fg_color="transparent", width=28, height=28, hover_color="#fff8f5", anchor="w")
    anticlock_button.grid(row=5, column=0, sticky="nw", pady=0, padx=5)
    clock_img_data = Image.open(r"C:\Users\91984\Desktop\cgProj\Image-Editor\rotate-right.png")
    clock_img = CTkImage(dark_image=clock_img_data, light_image=clock_img_data)
    clock_button = CTkButton(master=tool, image=clock_img, text="", fg_color="transparent", width=28, height=28, hover_color="#fff8f5", anchor="w")
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
CTkLabel(master=tool, text=f"Filter", font=("Corbel Bold", 24)).grid(row=0, column=0, sticky="nw", pady=(100,0), padx=5)

app.mainloop()

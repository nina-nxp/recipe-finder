import requests
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk

# GUI logic
def show_recipe():
    try:
        response = requests.get(
            "https://www.themealdb.com/api/json/v1/1/search.php?s=" + recipe_entry.get()
        )
        response.raise_for_status()
        food = response.json()

        if not food["meals"]:
            meal_name = "Not Found"
            meal_instructions = "No recipe found for your search."
            meal_ingredients = ""
        else:
            meal = food["meals"][0]
            meal_name = meal.get("strMeal", "Unknown")
            meal_instructions = meal.get("strInstructions", "No instructions available.")
            meal_ingredients = ""
            i = 1
            while True:
                ingredient = meal.get(f"strIngredient{i}")
                measure = meal.get(f"strMeasure{i}")
                if not ingredient or ingredient.strip() == "":
                    break
                meal_ingredients += f"{ingredient.strip():<25}{measure.strip()}\n"
                i += 1

    except requests.RequestException as e:
        meal_name = "Error"
        meal_instructions = f"Network error: {e}"
        meal_ingredients = ""
    except Exception as e:
        meal_name = "Error"
        meal_instructions = f"Unexpected error: {e}"
        meal_ingredients = "N/A"
    output_string.set(
        f"Cuisine: {meal_name}\n\nIngredients:\n{meal_ingredients}\n\nInstructions:\n{meal_instructions}"
    )
    scroll_frame.pack()

window = tk.Tk()
window.title('Small Recipe Finder')
window.configure(background="darkred")
window.geometry('600x500')
bg_image = PhotoImage(file='/Users/nxp/Documents/Python Projects on VSCode/Recipe/woodbg.png')
image = tk.Label(window, image=bg_image)
image.place(x=0, y=0, relwidth=1, relheight=1)

scroll_frame = ctk.CTkScrollableFrame(window,
                                      width=550,
                                      height=300,
                                      fg_color=("maroon"),
                                      bg_color=("transparent"),
                                      scrollbar_button_color="brown",
                                      scrollbar_button_hover_color="burgundy",)

title_label = tk.Label(window,
                       text='Enter Recipe!',
                       bg="brown",
                       fg="white",
                       relief="flat",
                       highlightthickness=2,
                       highlightbackground="darkred",
                       font=('courier', 16, 'bold'))
title_label.pack(pady=10)

recipe_entry = tk.StringVar()
recipe_name = tk.Entry(window,
                       textvariable=recipe_entry,
                       bg="brown",
                       fg="white",
                       insertbackground="white",
                       relief="flat",
                       highlightthickness=2,
                       highlightbackground="darkred")
recipe_name.pack(pady=5)

button_image = Image.open('/Users/nxp/Documents/Python Projects on VSCode/Recipe/redbrown.png')
button_image = ImageTk.PhotoImage(button_image)
button = tk.Button(window,
                   text='Show Recipe',
                   fg="white",
                   bg="brown",
                   width=100,
                   height=25,
                   image=button_image,
                   relief="flat",
                   highlightthickness=2,
                   highlightbackground="darkred",
                   compound="center",
                   font=('courier', 14, 'bold'),
                   command=show_recipe)
button.pack(pady=5)

# original pil
plaid_image_pil = Image.open("/Users/nxp/Documents/Python Projects on VSCode/Recipe/plaidbg.png")
# initial pil
plaid_image_tk = ImageTk.PhotoImage(plaid_image_pil)

output_string = tk.StringVar()
output_label = tk.Label(scroll_frame,
                        borderwidth=0,
                        highlightthickness=0,
                        text="",
                        textvariable=output_string,
                        width=550,
                        wraplength=550,
                        justify='left',
                        font="courier",
                        bg="brown")

output_label.pack()

window.mainloop()

"""
Adding Image:
bg_image = Image.open("/Users/nxp/Documents/Python Projects on VSCode/Recipe/knitbg.png")
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = Label(window, image=bg_image)
bg_label.pack()
"""

"""
# Testing Canvas
canvas_1 = tk.Canvas(window)
canvas_1.pack()
points = [50, 100, 100, 50, 150, 100, 100, 150]
canvas_1.create_polygon(points, fill='blue', smooth=True)
"""

"""
# Trying to Output Data on Canvas and Resize Canvas Properly
bg = PhotoImage(file="/Users/nxp/Documents/Python Projects on VSCode/Recipe/plaidbg.png")
my_canvas = Canvas(scroll_frame)

def fetched_data():
    fetched = output_string.get()
    my_canvas.itemconfigure(canvas_text, text=fetched)

my_canvas.create_image(0,0, image=bg)
canvas_text = my_canvas.create_text(5,5,
                      text="Hello!",
                      font=("courier"),
                      anchor="nw"
                      )

my_canvas.pack(fill="both", expand=True)
"""

"""
#image=plaid_image_tk, compound="center" <-- add back to output_label to have plaid_image behind text

def resize_plaid(event):
    # Resize using the original PIL image
    resized = plaid_image_pil.resize((event.width, event.height), Image.LANCZOS)
    new_img = ImageTk.PhotoImage(resized)
    output_label.image = new_img  # keep reference
    output_label.config(image=new_img)
    
output_label.bind("<Configure>", resize_plaid)
"""

"""
ori_width = ori_height = None  # start as None
def back_normal(event):
    global ori_width, ori_height

    # Store original size the first time
    if ori_width is None or ori_height is None:
        ori_width, ori_height = event.width, event.height

    # Only resize if we have valid dimensions
    if ori_width > 0 and ori_height > 0:
        original = plaid_image_pil.resize((ori_width, ori_height), Image.LANCZOS)
        ori_img = ImageTk.PhotoImage(original)
        output_label.image = ori_img  # keep reference
        output_label.config(image=ori_img)

output_label.bind("<Configure>", back_normal)
"""
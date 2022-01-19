import tkinter as tk
from PIL import Image,ImageTk

root = tk.Tk()
root.title("Multipurpose Application")

app_width = 1000
app_height = 500
root.geometry(f'{app_width}x{app_height}')

screen_width = root.winfo_screenmmwidth()
screen_height = root.winfo_screenheight()
#bg = tk.PhotoImage(file="E:\Ayan Toshi\Grade 12\Computer Science\Computer Project\Background_image.png")

bg_img = Image.open('E:\Ayan Toshi\Grade 12\Computer Science\Computer Project\Background_image.png')
bg_img = bg_img.resize((1000,1000), Image.ANTIALIAS)
bg_img = ImageTk.PhotoImage(bg_img)
# bg_label = tk.Label(image=bg_img, anchor="center")
# bg_label.image = bg_img
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)

canvas = tk.Canvas(root, width=app_width, height=app_height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0,0, image=bg_img, anchor="nw")

# window.grid(columnspan=3, rowspan=3)


# my_label = tk.Label(root, text=f"Width:{screen_width}, Height:{screen_height}")
# my_label.pack(pady=20)

def logo_code():
    logo = Image.open('E:\Ayan Toshi\Grade 12\Computer Science\Computer Project\Logo\Multipurpose App-logos_black.png')
    logo = logo.resize((700,700), Image.ANTIALIAS)  #Code to resize image, ANTIALIAS: Removes image structural padding
    
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo, anchor="center")
    logo_label.image = logo
    logo_label.place(relx=0.5, rely=0.19, anchor="center")
    #logo_label.grid(column=1, row=0) #columnspan=3 removed from beginning to change relative position
logo_code()

def gui_command_code():
    frst_menu = tk.Label(root, text="Select the application you would like to use", font=("Raleway",20))
    frst_menu.place(relx=0.5, rely=0.45, anchor="center")
gui_command_code()

def buttons():
    #Travel Service Button
    test_button_text = tk.StringVar()
    test_button = tk.Button(root, textvariable=test_button_text, font="Raleway", 
                            bg='#20bebe', fg="white", height=2, width=17)
    test_button_text.set("Travel Service")
    test_button.place(relx=0.5, rely=0.6, anchor="center")

    #Restaurent Service Button
    test_button_text_2 = tk.StringVar()
    test_button_2 = tk.Button(root, textvariable=test_button_text_2, font="Raleway", 
                            bg='#20bebe', fg="white", height=2, width=17)
    test_button_text_2.set("Restaurent Service")
    test_button_2.place(relx=0.5, rely=0.7, anchor="center")

    #Online Shopping Button
    test_button_text_3 = tk.StringVar()
    test_button_3 = tk.Button(root, textvariable=test_button_text_3, font="Raleway", 
                            bg='#20bebe', fg="white", height=2, width=17)
    test_button_text_3.set("Online Shopping")
    test_button_3.place(relx=0.5, rely=0.8, anchor="center")

buttons()  

# #Setting-up UI spacing - GRID
# GRID method - TERMINATED/ABANDONED
# window = tk.Canvas(root, width=600, height=250)
# window.grid(columnspan=3)

#Terminating loop
root.mainloop()



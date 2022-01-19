import tkinter as tk
from PIL import Image,ImageTk

root = tk.Tk()
root.title("Multipurpose Application")

app_width = 1000
app_height = 500
root.geometry(f'{app_width}x{app_height}+{100}+{100}')

# window = tk.Canvas(root, width=600, height=300)
# window.grid(columnspan=3, rowspan=3)

screen_width = root.winfo_screenmmwidth()
screen_height = root.winfo_screenheight()
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
    frst_menu = tk.Label(root, text="Select the mode of usage", font=("Raleway",20))
    frst_menu.place(relx=0.5, rely=0.45, anchor="center")
gui_command_code()

def buttons():
    test_button_text = tk.StringVar()
    test_button = tk.Button(root, textvariable=test_button_text, font="Raleway", 
                            bg='#20bebe', fg="white", height=2, width=15)
    test_button_text.set("User")
    test_button.place(relx=0.5, rely=0.6, anchor="center")

    test_button_text_2 = tk.StringVar()
    test_button_2 = tk.Button(root, textvariable=test_button_text_2, font="Raleway", 
                            bg='#20bebe', fg="white", height=2, width=15)
    test_button_text_2.set("Admin")
    test_button_2.place(relx=0.5, rely=0.7, anchor="center")
buttons()  

# #Setting-up UI spacing - GRID
# GRID method - TERMINATED/ABANDONED
# window = tk.Canvas(root, width=600, height=250)
# window.grid(columnspan=3)

#Terminating loop
root.mainloop()



import customtkinter
from tkinter import PhotoImage

def button_click(button_text):
    print(f"Button {button_text} clicked!")

frame = customtkinter.CTk()
frame.geometry("700x700")

# Load images
image1 = PhotoImage(file="UI_up.png")  # Replace "image1.png" with the actual file path
image2 = PhotoImage(file="UI_down.png")



button1 = customtkinter.CTkButton(master=frame, image=image1, command=lambda: button_click(1), text="")
button2 = customtkinter.CTkButton(master=frame, image=image1, command=lambda: button_click(2), text="")
button3 = customtkinter.CTkButton(master=frame, image=image1, command=lambda: button_click(3), text="")
button4 = customtkinter.CTkButton(master=frame, image=image2, command=lambda: button_click(4), text="")
button5 = customtkinter.CTkButton(master=frame, image=image2, command=lambda: button_click(5), text="")
button6 = customtkinter.CTkButton(master=frame, image=image2, command=lambda: button_click(6), text="")
# Calculate relative distances based on window size
window_width = frame.winfo_reqwidth()
window_height = frame.winfo_reqheight()

# Set the coordinates for the triangular shape
x1, y1 = (window_width / 2), window_height - 20  # Bottom center
x2, y2 = window_width + 40, window_height + 150   # Top left
x3, y3 = (window_width / 2) * 4, window_height - 20  # Top right

button1.place(x=x1, y=y1)
button2.place(x=x2, y=y2)
button3.place(x=x3, y=y3)
button4.place(x=x1, y=y1+60)
button5.place(x=x2, y=y2+60)
button6.place(x=x3, y=y3+60)
frame.mainloop()

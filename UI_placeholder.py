import tkinter as tk
from PIL import Image, ImageTk
import send_commands

# Global variables to track button state
forward_button_pressed = False
backward_button_pressed = False

def on_forward_button_press(portnum):
    global forward_button_pressed
    forward_button_pressed = True
    if portnum == 1:
        move_forward1()
    if portnum == 2:
        move_forward2()
    if portnum == 3:
        move_forward3()

def on_backward_button_press(portnum):
    global backward_button_pressed
    backward_button_pressed = True
    if portnum == 1:
        move_backward1()
    if portnum == 2:
        move_backward2()
    if portnum == 3:
        move_backward3()

def on_button_release(event):
    global forward_button_pressed, backward_button_pressed
    forward_button_pressed = False
    backward_button_pressed = False
    send_commands.ser.write(b'S')  # Send 'S' to stop the movement

def move_forward1():
    if forward_button_pressed:
        send_commands.cw1()
        root.after(50, move_forward1)  # Repeat after 50 milliseconds

def move_backward1():
    if backward_button_pressed:
        send_commands.ccw1()
        root.after(50, move_backward1)  # Repeat after 50 milliseconds

def move_forward2():
    if forward_button_pressed:
        send_commands.cw2()
        root.after(50, move_forward2)  # Repeat after 50 milliseconds

def move_backward2():
    if backward_button_pressed:
        send_commands.ccw2()
        root.after(50, move_backward2)  # Repeat after 50 milliseconds

def move_forward3():
    if forward_button_pressed:
        send_commands.cw3()
        root.after(50, move_forward3)  # Repeat after 50 milliseconds

def move_backward3():
    if backward_button_pressed:
        send_commands.ccw3()
        root.after(50, move_backward3)  # Repeat after 50 milliseconds

def on_exit():
    send_commands.ser.close()
    root.destroy()

root = tk.Tk()
root.geometry("700x700")

# Load images
image1 = Image.open("UI_up.png") 
image2 = Image.open("UI_down.png")

# Convert images to Tkinter PhotoImage objects
tk_image1 = ImageTk.PhotoImage(image1)
tk_image2 = ImageTk.PhotoImage(image2)

# Create a canvas
canvas = tk.Canvas(root, width=700, height=700)
canvas.pack()

# Place images at specific locations on the canvas
image1_id = canvas.create_image(100, 100, anchor=tk.NW, image=tk_image1)
image2_id = canvas.create_image(300, 300, anchor=tk.NW, image=tk_image1)
image3_id = canvas.create_image(500, 100, anchor=tk.NW, image=tk_image1)
image4_id = canvas.create_image(100, 160, anchor=tk.NW, image=tk_image2)
image5_id = canvas.create_image(300, 360, anchor=tk.NW, image=tk_image2)
image6_id = canvas.create_image(500, 160, anchor=tk.NW, image=tk_image2)

# Bind press and release events to the images
canvas.tag_bind(image1_id, '<ButtonPress-1>', lambda event: on_forward_button_press(1))
canvas.tag_bind(image2_id, '<ButtonPress-1>', lambda event: on_forward_button_press(2))
canvas.tag_bind(image3_id, '<ButtonPress-1>', lambda event: on_forward_button_press(3))
canvas.tag_bind(image4_id, '<ButtonPress-1>', lambda event: on_backward_button_press(1))
canvas.tag_bind(image5_id, '<ButtonPress-1>', lambda event: on_backward_button_press(2))
canvas.tag_bind(image6_id, '<ButtonPress-1>', lambda event: on_backward_button_press(3))

canvas.tag_bind(image1_id, '<ButtonRelease-1>', on_button_release)
canvas.tag_bind(image2_id, '<ButtonRelease-1>', on_button_release)
canvas.tag_bind(image3_id, '<ButtonRelease-1>', on_button_release)
canvas.tag_bind(image4_id, '<ButtonRelease-1>', on_button_release)
canvas.tag_bind(image5_id, '<ButtonRelease-1>', on_button_release)
canvas.tag_bind(image6_id, '<ButtonRelease-1>', on_button_release)

root.protocol("WM_DELETE_WINDOW", on_exit)  # Bind window close event

root.mainloop()

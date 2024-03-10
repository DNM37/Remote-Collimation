
#ddeprecated
import tkinter as tk
import send_commands  # Assuming send_commands.py is in the same directory

def on_forward_button_press():
    send_commands.cw()

def on_backward_button_press():
    send_commands.ccw()

def on_button_release():
    send_commands.ser.write(b'S')  # Send 'S' to stop the movement

def on_exit():
    send_commands.ser.close()
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Serial Control App")
root.geometry("400x200")

# Create Forward button
button_forward = tk.Button(root, text="Forward", command=on_forward_button_press, repeatdelay=500, repeatinterval=100)
button_forward.pack(pady=10)
button_forward.bind("<ButtonRelease-1>", lambda event: on_button_release())

# Create Backward button
button_backward = tk.Button(root, text="Backward", command=on_backward_button_press, repeatdelay=500, repeatinterval=100)
button_backward.pack(pady=10)
button_backward.bind("<ButtonRelease-1>", lambda event: on_button_release())

# Create an exit button
button_exit = tk.Button(root, text="Exit", command=on_exit)
button_exit.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

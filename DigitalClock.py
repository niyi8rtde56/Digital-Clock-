import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='light pink', foreground='white')

# Pack the label into the window
label.pack(anchor='center')

# Call the update_time function to initialize the clock
update_time()

# Run the Tkinter event loop
root.mainloop()
         
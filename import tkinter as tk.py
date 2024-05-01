import tkinter as tk
import random

# List of items to pack for a picnic
items_to_pack = ["PEN", "ID CARD", "CHIPS", "SANDWICH", "DRINK", "FRUIT", "SUNSCREEN", "HAT"]

# Function to generate and display a random number
def generate_random_number():
    random_index = random.randint(0, len(items_to_pack) - 1)
    random_number_label.config(text=str(random_index))

# Create the main window
root = tk.Tk()
root.title("Picnic Pack Helper")

# Create two labels
items_label = tk.Label(root, text=str(items_to_pack))
random_number_label = tk.Label(root, text="")

# Create a button to generate a random number
generate_button = tk.Button(root, text="Generate Random Item Index", command=generate_random_number, fg="white", bg="blue")

# Place the elements in the center of the window
items_label.place(relx=0.5, rely=0.3, anchor='center')
random_number_label.place(relx=0.5, rely=0.5, anchor='center')
generate_button.place(relx=0.5, rely=0.7, anchor='center')

# Run the application
root.mainloop()

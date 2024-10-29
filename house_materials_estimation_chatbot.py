import tkinter as tk
from tkinter import messagebox, scrolledtext
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset for training the model
data = {
    'floor_area': [50, 100, 150, 200, 250, 300],
    'num_rooms': [2, 4, 6, 8, 10, 12],
    'cement_bags': [5, 10, 15, 20, 25, 30]
}
df = pd.DataFrame(data)

# Features and target variable
X = df[['floor_area', 'num_rooms']]
y = df['cement_bags']

# Train the model
model = LinearRegression()
model.fit(X, y)

def predict_cement_bags(floor_area, num_rooms):
    return model.predict([[floor_area, num_rooms]])[0]

def calculate_costs():
    try:
        cement_price = float(cement_price_entry.get())
        number_of_cements = int(number_of_cements_entry.get())
        
        brick_price = float(brick_price_entry.get())
        number_of_bricks = int(number_of_bricks_entry.get())
        
        roof_type = roof_type_var.get()
        roof_price_per_unit = float(roof_price_entry.get())
        roof_quantity = int(roof_quantity_entry.get())
        
        wood_price = float(wood_price_entry.get())
        number_of_wood = int(number_of_wood_entry.get())
        
        number_of_windows = int(number_of_windows_entry.get())
        total_window_cost = float(total_window_cost_entry.get())
        
        number_of_doors = int(number_of_doors_entry.get())
        total_door_cost = float(total_door_cost_entry.get())
        
        door_frame_price = float(door_frame_price_entry.get())
        total_door_frames = int(total_door_frames_entry.get())
        
        tile_price = float(tile_price_entry.get())
        floor_area = float(floor_area_entry.get())
        
        predicted_cement_bags = predict_cement_bags(floor_area, number_of_doors)
        messagebox.showinfo("Prediction", f"Suggested Cement Bags: {predicted_cement_bags:.1f}")

        total_cement_cost = number_of_cements * cement_price
        total_brick_cost = number_of_bricks * brick_price
        total_roof_cost = roof_quantity * roof_price_per_unit
        total_wood_cost = number_of_wood * wood_price
        total_floor_cost = floor_area * tile_price
        total_door_frame_cost = total_door_frames * door_frame_price
        
        total_cost = (total_cement_cost + total_brick_cost + total_roof_cost + 
                      total_wood_cost + total_window_cost + total_door_cost + 
                      total_floor_cost + total_door_frame_cost)

        results = (
            f"Total Cement Cost: R{total_cement_cost:.2f}\n"
            f"Total Brick Cost: R{total_brick_cost:.2f}\n"
            f"Roof ({roof_type}) Cost: R{total_roof_cost:.2f}\n"
            f"Total Wood Cost: R{total_wood_cost:.2f}\n"
            f"Total Window Cost: R{total_window_cost:.2f}\n"
            f"Total Door Cost: R{total_door_cost:.2f}\n"
            f"Total Floor Cost: R{total_floor_cost:.2f}\n"
            f"Total Door Frame Cost: R{total_door_frame_cost:.2f}\n"
            f"Total Estimated Cost: R{total_cost:.2f}"
        )

        messagebox.showinfo("Estimation Summary", results)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

def chatbot_response(user_input):
    responses = {
        "how many cements do i need?": "Please provide the floor area and number of rooms for an estimate.",
        "what is the cost of bricks?": "Please enter the price per brick in the input fields.",
        "what's the total cost?": "After you enter all details, click 'Calculate Costs' for the total estimate.",
        "help": "You can ask about cement needs, brick costs, or how to calculate totals.",
        "hi": "Hello! How can I assist you today?",
        "bye": "Goodbye! Have a great day!",
    }
    return responses.get(user_input.lower(), "I'm sorry, I didn't understand that. Can you rephrase?")

def send_message():
    user_input = user_input_entry.get()
    chat_display.insert(tk.END, f"You: {user_input}\n")
    response = chatbot_response(user_input)
    chat_display.insert(tk.END, f"Bot: {response}\n")
    chat_display.yview(tk.END)
    user_input_entry.delete(0, tk.END)

def clear_fields():
    entries = [cement_price_entry, number_of_cements_entry, brick_price_entry,
               number_of_bricks_entry, roof_price_entry, roof_quantity_entry,
               wood_price_entry, number_of_wood_entry, number_of_windows_entry,
               total_window_cost_entry, number_of_doors_entry, total_door_cost_entry,
               door_frame_price_entry, total_door_frames_entry, tile_price_entry, floor_area_entry]
    for entry in entries:
        entry.delete(0, tk.END)
    chat_display.delete(1.0, tk.END)

# Setting up the GUI
root = tk.Tk()
root.title("House Materials Cost Estimation System")
root.geometry("900x650")

# Main frame for inputs and chatbot
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Cost estimation frame
frame = tk.Frame(main_frame, padx=10, pady=10)
frame.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

# Labels and entries
labels = [
    "Price of Cement (Rands):", "Number of Cement Bags:", "Price of Brick (Rands):",
    "Number of Bricks:", "Roof Price per Unit (Rands):", "Roof Quantity:",
    "Price of Wood (Rands):", "Number of Wood:", "Number of Windows:",
    "Total Window Cost (Rands):", "Number of Doors:", "Total Door Cost (Rands):",
    "Price of Door Frame (Rands):", "Number of Door Frames:", "Price of Tile (Rands):",
    "Total Floor Area (m²):"
]

entries = []
for label in labels:
    tk.Label(frame, text=label).pack(anchor='w')
    entry = tk.Entry(frame, width=40)
    entry.pack()
    entries.append(entry)

# Assigning entries to variables
(cement_price_entry, number_of_cements_entry, brick_price_entry,
 number_of_bricks_entry, roof_price_entry, roof_quantity_entry,
 wood_price_entry, number_of_wood_entry, number_of_windows_entry,
 total_window_cost_entry, number_of_doors_entry, total_door_cost_entry,
 door_frame_price_entry, total_door_frames_entry, tile_price_entry,
 floor_area_entry) = entries

# Roof type selection
roof_frame = tk.Frame(frame)
roof_frame.pack(pady=10)
roof_type_var = tk.StringVar(value="Roof Tiles")
tk.Label(roof_frame, text="Select Roof Type:").pack(anchor='w')
tk.Radiobutton(roof_frame, text="Roof Tiles", variable=roof_type_var, value="Roof Tiles").pack(anchor='w')
tk.Radiobutton(roof_frame, text="Zinc", variable=roof_type_var, value="Zinc").pack(anchor='w')

# Buttons
button_frame = tk.Frame(frame)
button_frame.pack(pady=10)
calculate_button = tk.Button(button_frame, text="Calculate Costs", command=calculate_costs)
calculate_button.pack(side='left', padx=5)
clear_button = tk.Button(button_frame, text="Clear", command=clear_fields)
clear_button.pack(side='left', padx=5)

# Chatbot frame
chat_frame = tk.Frame(main_frame)
chat_frame.grid(row=0, column=1, sticky="ne", padx=20, pady=20)

tk.Label(chat_frame, text="Chat with Bot:", pady=5).pack()
chat_display = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, width=50, height=15, state='normal')
chat_display.pack(padx=10, pady=5)
user_input_entry = tk.Entry(chat_frame, width=40)
user_input_entry.pack(padx=10, pady=5)
send_button = tk.Button(chat_frame, text="Send", command=send_message)
send_button.pack()

# Run the application
root.mainloop()




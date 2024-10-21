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
        # Get input values
        cement_price = float(cement_price_entry.get())
        number_of_cements = int(number_of_cements_entry.get())
        
        brick_price = float(brick_price_entry.get())
        number_of_bricks = int(number_of_bricks_entry.get())
        
        roofing_cost = float(roofing_cost_entry.get())
        
        number_of_windows = int(number_of_windows_entry.get())
        total_window_cost = float(total_window_cost_entry.get())
        
        number_of_doors = int(number_of_doors_entry.get())
        total_door_cost = float(total_door_cost_entry.get())
        
        door_frame_price = float(door_frame_price_entry.get())
        total_door_frames = int(total_door_frames_entry.get())
        
        tile_price = float(tile_price_entry.get())
        floor_area = float(floor_area_entry.get())
        
        # Predict cement bags needed
        predicted_cement_bags = predict_cement_bags(floor_area, number_of_doors)
        messagebox.showinfo("Prediction", f"Suggested Cement Bags: {predicted_cement_bags:.1f}")

        # total costs
        total_cement_cost = number_of_cements * cement_price
        total_brick_cost = number_of_bricks * brick_price
        total_floor_cost = floor_area * tile_price
        total_door_frame_cost = total_door_frames * door_frame_price
        
        # Calculating the total estimated cost
        total_cost = (total_cement_cost + total_brick_cost + roofing_cost + 
                      total_window_cost + total_door_cost + total_floor_cost + 
                      total_door_frame_cost)

        # Display results
        results = (
            f"Total Cement Cost: R{total_cement_cost:.2f}\n"
            f"Total Brick Cost: R{total_brick_cost:.2f}\n"
            f"Roofing Cost: R{roofing_cost:.2f}\n"
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
    user_input = user_input.lower()
    responses = {
        "how many cements do i need?": "Please provide the floor area and number of rooms for an estimate.",
        "what is the cost of bricks?": "Please enter the price per brick in the input fields.",
        "what's the total cost?": "After you enter all details, click 'Calculate Costs' for the total estimate.",
        "help": "You can ask about cement needs, brick costs, or how to calculate totals.",
        "hi": "Hello! How can I assist you today?",
        "bye": "Goodbye! Have a great day!",
    }
    return responses.get(user_input, "I'm sorry, I didn't understand that. Can you rephrase?")

def send_message():
    user_input = user_input_entry.get()
    chat_display.insert(tk.END, f"You: {user_input}\n")
    response = chatbot_response(user_input)
    chat_display.insert(tk.END, f"Bot: {response}\n")
    user_input_entry.delete(0, tk.END)

def clear_fields():
    """Clears all entry fields."""
    cement_price_entry.delete(0, tk.END)
    number_of_cements_entry.delete(0, tk.END)
    brick_price_entry.delete(0, tk.END)
    number_of_bricks_entry.delete(0, tk.END)
    roofing_cost_entry.delete(0, tk.END)
    number_of_windows_entry.delete(0, tk.END)
    total_window_cost_entry.delete(0, tk.END)
    number_of_doors_entry.delete(0, tk.END)
    total_door_cost_entry.delete(0, tk.END)
    door_frame_price_entry.delete(0, tk.END)
    total_door_frames_entry.delete(0, tk.END)
    tile_price_entry.delete(0, tk.END)
    floor_area_entry.delete(0, tk.END)
    chat_display.delete(1.0, tk.END)  # Clear chat display

# Setting up the GUI
root = tk.Tk()
root.title("House Materials Cost Estimation System")

# cost estimation
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=20, pady=20)

# labels and entries
labels = [
    "Price of Cement (Rands):", "Number of Cement Bags:", "Price of Brick (Rands):",
    "Number of Bricks:", "Roofing Cost (Rands):", "Number of Windows:",
    "Total Window Cost (Rands):", "Number of Doors:", "Total Door Cost (Rands):",
    "Price of Door Frame (Rands):", "Number of Door Frames:", "Price of Tile (Rands):",
    "Total Floor Area (m²):"
]

entries = []
for label in labels:
    tk.Label(frame, text=label).pack(anchor='w')
    entry = tk.Entry(frame)
    entry.pack()
    entries.append(entry)

# Assigning entries to variables for easy access
(cement_price_entry, number_of_cements_entry, brick_price_entry,
 number_of_bricks_entry, roofing_cost_entry, number_of_windows_entry,
 total_window_cost_entry, number_of_doors_entry, total_door_cost_entry,
 door_frame_price_entry, total_door_frames_entry, tile_price_entry,
 floor_area_entry) = entries

# Calculate and Clear buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

calculate_button = tk.Button(button_frame, text="Calculate Costs", command=calculate_costs)
calculate_button.pack(side='left', padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_fields)
clear_button.pack(side='left', padx=5)

# Chatbot section
tk.Label(root, text="Chat with Bot:", pady=10).pack()
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, state='normal')
chat_display.pack(padx=20, pady=10)

user_input_entry = tk.Entry(root, width=50)
user_input_entry.pack(padx=20, pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# running the system
root.mainloop()



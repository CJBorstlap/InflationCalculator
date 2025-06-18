import tkinter as tk
from tkinter import ttk

def calculate_inflation_degradation():
    try:
        amount = float(entry_amount.get())
        rate = float(entry_rate.get()) / 100
        years = int(entry_years.get())
        # Main result
        result = amount * (1 - rate) ** years
        label_result.config(text=f"Value in today's money: R{result:,.2f}")
        # Calculate up to 3 intervals at 5-year steps
        interval_results = []
        for y in range(5, years+1, 5):
            if len(interval_results) >= 3:
                break
            value = amount * (1 - rate) ** y
            degradation_pct = (1 - value/amount) * 100
            interval_results.append((y, value, degradation_pct))
        # Clear existing table entries
        for i in tree.get_children():
            tree.delete(i)
        # Insert new interval results into the table
        for year, value, degradation_pct in interval_results:
            tree.insert(
                "", "end",
                values=(f"{year} yr", f"R{int(value):,}", f"{degradation_pct:.1f}%")
            )
    except ValueError:
        label_result.config(text="Please enter valid numbers.")
        for i in tree.get_children():
            tree.delete(i)

# Configure main window
window = tk.Tk()
window.title("Inflation Degradation Calculator")
window.geometry("500x400")

# Input fields
ttk.Label(window, text="Current Amount (R):").pack(pady=5)
entry_amount = ttk.Entry(window)
entry_amount.pack()

ttk.Label(window, text="Inflation Rate (%):").pack(pady=5)
entry_rate = ttk.Entry(window)
entry_rate.pack()

ttk.Label(window, text="Number of Years:").pack(pady=5)
entry_years = ttk.Entry(window)
entry_years.pack()

# Calculate button
btn_calculate = ttk.Button(window, text="Calculate", command=calculate_inflation_degradation)
btn_calculate.pack(pady=10)

# Main result label
label_result = ttk.Label(window, text="", font=('Arial', 11, 'bold'))
label_result.pack(pady=5)

# Table for interval results
columns = ("Years", "Value (R)", "Loss")
tree = ttk.Treeview(window, columns=columns, show="headings", height=4)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")
tree.pack(pady=10, fill="x")

window.mainloop()

import tkinter as tk
from tkinter import ttk
from datetime import datetime
import tkinter
import requests

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.amount_var = tk.DoubleVar()
        self.currency_var = tk.StringVar(value="USD")
        self.category_var = tk.StringVar(value="life expenses")
        self.date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        self.payment_method_var = tk.StringVar(value="Cash")
        self.create_gui()

    def create_gui(self):
        tk.Label(self.root, text="Amount:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.amount_var).grid(row=0, column=1)
        tk.Label(self.root, text="Currency:").grid(row=1, column=0)
        currency_combobox = ttk.Combobox(self.root, textvariable=self.currency_var, values=["USD", "EUR", "GBP"])
        currency_combobox.grid(row=1, column=1)
        tk.Label(self.root, text="Category:").grid(row=2, column=0)
        category_combobox = ttk.Combobox(self.root, textvariable=self.category_var,
                                        values=["life expenses", "electricity", "gas", "rental", "grocery",
                                                "savings", "education", "charity"])
        category_combobox.grid(row=2, column=1)
        tk.Label(self.root, text="Date:").grid(row=3, column=0)
        tk.Entry(self.root, textvariable=self.date_var).grid(row=3, column=1)
        tk.Label(self.root, text="Payment Method:").grid(row=4, column=0)
        payment_method_combobox = ttk.Combobox(self.root, textvariable=self.payment_method_var,
                                                values=["Cash", "Credit Card", "Paypal"])
        payment_method_combobox.grid(row=4, column=1)
        tk.Button(self.root, text="Submit", command=self.submit_expense).grid(row=5, column=0, columnspan=2)
        columns = ("Amount", "Currency", "Category", "Date", "Payment Method")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.grid(row=6, column=0, columnspan=2)

    def submit_expense(self):
        amount = self.amount_var.get()
        currency = self.currency_var.get()
        category = self.category_var.get()
        date = self.date_var.get()
        payment_method = self.payment_method_var.get()
        if not amount or not date:
            tk.messagebox.showwarning("Warning", "Please enter both amount and date.")
            return
        api_url = "f80ca48aa8b118ea1eb49c0bafaecd7516f7d357" 
        data = {"amount": amount, "currency": currency, "category": category,
                "date": date, "payment_method": payment_method}
        try:
            response = requests.post(api_url, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            tkinter.messagebox.showerror("Error", f"Failed to submit expense: {e}")
            return
        self.tree.insert("", "end", values=(amount, currency, category, date, payment_method))

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

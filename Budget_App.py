import tkinter as tk
from tkinter import messagebox, ttk
import pymysql

class BudgetManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Management System")
        self.root.geometry("900x600")
        self.user_id = None  
        self.meals_window = None
        
        # Database Connection
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="romario",
            database="project_budget"
        )
        self.cursor = self.db.cursor()
        
        # Create Main Frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=20, pady=20)
        
        # Title label
        title_label = tk.Label(self.main_frame, text="Budget Management System", font=("Helvetica", 20, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
        
        # Username Label and Entry Field
        tk.Label(self.main_frame, text="Email:").grid(row=1, column=0, padx=5, pady=40)
        self.email_entry = tk.Entry(self.main_frame)
        self.email_entry.grid(row=1, column=1, padx=5, pady=3)
        
        # Password Label and Entry Field
        tk.Label(self.main_frame, text="Password:").grid(row=2, column=0, padx=5, pady=30)
        self.password_entry = tk.Entry(self.main_frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=5, pady=3)
        
        # Login and Signup Buttons
        self.login_button = tk.Button(self.main_frame, text="Login", command=self.login)
        self.signup_button = tk.Button(self.main_frame, text="Signup", command=self.signup)
        self.login_button.grid(row=3, column=0, padx=5, pady=20)
        self.signup_button.grid(row=3, column=1, padx=5, pady=20)


    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        # Check if the user exists in the signup table
        self.cursor.execute("SELECT * FROM signup WHERE email = %s AND password = %s", (email, password))
        signup_user = self.cursor.fetchone()
        
        # Check if the user exists in the users table
        self.cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        users_user = self.cursor.fetchone()
        
        if signup_user or users_user:
            messagebox.showinfo("Success", "Login Successful!")
            self.user_id = users_user[0] if users_user else signup_user[0]
            self.open_budget_manager()
        else:
            messagebox.showerror("Error", "Invalid email or password")

    def signup(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Check if the email already exists in the database
        self.cursor.execute("SELECT * FROM signup WHERE email = %s", (email,))
        existing_user = self.cursor.fetchone()

        if existing_user:
            messagebox.showerror("Error", "Email already exists. Please use another email.")
        else:
            # Insert new user into signup table
            self.cursor.execute("INSERT INTO signup (email, password) VALUES (%s, %s)", (email, password))
            self.db.commit()
            messagebox.showinfo("Success", "Signup Successful! You can now login.")

    def open_budget_manager(self):
        self.root.withdraw()  # Hide the login window
        budget_window = tk.Toplevel()
        budget_window.title("Budget Manager")
        budget_window.geometry("900x900")

        # Display Records Button
        self.display_records_button = tk.Button(budget_window, text="Display Records", command=self.display_records)
        self.display_records_button.pack(pady=(200, 10), anchor="center")

        # Add/Edit Records Button
        self.add_edit_records_button = tk.Button(budget_window, text="Add/Edit Records", command=self.add_edit_records)
        self.add_edit_records_button.pack(pady=10, anchor="center")

        # Meals Button
        self.meals_button = tk.Button(budget_window, text="Meals", command=self.show_meals)
        self.meals_button.pack(pady=10, anchor="center")

        # Logout Button
        self.logout_button = tk.Button(budget_window, text="Logout", command=self.logout)
        self.logout_button.pack(pady=10, anchor="center")


    def display_records(self):
        # Create a new window for displaying records
        records_window = tk.Toplevel()
        records_window.title("Records")
        records_window.geometry("900x900")
        # Create a Treeview widget to display records
        tree = ttk.Treeview(records_window)
        tree["columns"] = ("Record Type", "Information")
        tree.heading("#0", text="Record Type")
        tree.heading("Record Type", text="Record Type")
        tree.heading("Information", text="Information")
        tree.pack(fill="both", expand=True)

        # Fetch and display records
        try:
            user_id = self.user_id

            # Fetch expenses
            self.cursor.execute("SELECT name, cost, date, category FROM expenses WHERE user_id = %s", (user_id,))
            expenses = self.cursor.fetchall()
            for expense in expenses:
                tree.insert("", tk.END, text="Expenses", values=(f"Name: {expense[0]}, Cost: {expense[1]}, Date: {expense[2]}, Category: {expense[3]}"))

            # Fetch income
            self.cursor.execute("SELECT income FROM users WHERE id = %s", (user_id,))
            income_row = self.cursor.fetchone()
            if income_row:
                income = income_row[0]
                tree.insert("", tk.END, text="Income", values=(f"Income: {income}"))
            else:
                tree.insert("", tk.END, text="Income", values=("No income data available",))

            # Fetch debt
            self.cursor.execute("SELECT debt, interest FROM debts WHERE user_id = %s", (user_id,))
            debt_row = self.cursor.fetchone()
            if debt_row:
                debt, interest = debt_row
                tree.insert("", tk.END, text="Debt", values=(f"Debt: {debt}, Interest: {interest}"))
            else:
                tree.insert("", tk.END, text="Debt", values=("No debt data available",))

            # Fetch budget
            self.cursor.execute("SELECT funds FROM users WHERE id = %s", (user_id,))
            budget_row = self.cursor.fetchone()
            if budget_row:
                budget = budget_row[0]
                tree.insert("", tk.END, text="Budget (per period)", values=(f"Budget: {budget}"))
            else:
                tree.insert("", tk.END, text="Budget (per period)", values=("No budget data available",))

            # Fetch spending
            # Assume spending is calculated elsewhere and fetched from another table
            spending = 0  # Placeholder for spending
            tree.insert("", tk.END, text="Spending (daily)", values=(f"Spending: {spending}"))

            # Fetch emergency funds
            self.cursor.execute("SELECT funds FROM users WHERE id = %s", (user_id,))
            emergency_funds_row = self.cursor.fetchone()
            if emergency_funds_row:
                emergency_funds = emergency_funds_row[0] * 0.1  # Assuming 10% of funds is emergency funds
                tree.insert("", tk.END, text="Emergency funds", values=(f"Emergency Funds: {emergency_funds}"))
            else:
                tree.insert("", tk.END, text="Emergency funds", values=("No emergency funds data available",))

            # Fetch subscriptions
            self.cursor.execute("SELECT subscription_name, cost, one_time_payment, pay_period FROM subscriptions WHERE user_id = %s", (user_id,))
            subscriptions = self.cursor.fetchall()
            for subscription in subscriptions:
                tree.insert("", tk.END, text="Subscriptions", values=(f"Name: {subscription[0]}, Cost: {subscription[1]}, One Time Payment: {subscription[2]}, Pay Period: {subscription[3]}"))

            # Fetch periodic summary
            # Assuming periodic summary is calculated elsewhere and fetched from another table
            periodic_summary = ""  # Placeholder for periodic summary
            tree.insert("", tk.END, text="Periodic summary", values=(periodic_summary))

        except pymysql.Error as e:
            print("Error retrieving data:", e)

    def add_edit_records(self):
        # Open a new window for adding/editing records
        add_edit_window = tk.Toplevel()
        add_edit_window.title("Add/Edit Records")
        # Set the window size to be larger
        add_edit_window.geometry("900x700")

        # Add/Edit Expense Button
        add_expense_button = tk.Button(add_edit_window, text="Add/Edit Expense", command=self.add_edit_expense)
        add_expense_button.place(relx=0.5, rely=0.2, anchor="center")

        # Edit Income Button
        edit_income_button = tk.Button(add_edit_window, text="Edit Income", command=self.edit_income)
        edit_income_button.place(relx=0.5, rely=0.3, anchor="center")

        # Add/Delete Subscription Button
        add_delete_subscription_button = tk.Button(add_edit_window, text="Add/Delete Subscription", command=self.add_delete_subscription)
        add_delete_subscription_button.place(relx=0.5, rely=0.4, anchor="center")

        # Add/Edit Debt Button
        add_edit_debt_button = tk.Button(add_edit_window, text="Add/Edit Debt", command=self.add_edit_debt)
        add_edit_debt_button.place(relx=0.5, rely=0.5, anchor="center")

        # Add/Edit Budget Button
        add_edit_budget_button = tk.Button(add_edit_window, text="Add/Edit Budget", command=self.add_edit_budget)
        add_edit_budget_button.place(relx=0.5, rely=0.6, anchor="center")



    def add_edit_expense(self):
        # Function for adding expense
        def add_expense():
            # Open a new window for adding expense
            add_expense_window = tk.Toplevel()
            add_expense_window.title("Add Expense")
            add_expense_window.geometry("900x600")

            # Labels and entry fields for expense details
            tk.Label(add_expense_window, text="Name:").grid(row=0, column=0, padx=5, pady=5)
            name_entry = tk.Entry(add_expense_window)
            name_entry.grid(row=0, column=1, padx=5, pady=5)

            tk.Label(add_expense_window, text="Cost:").grid(row=1, column=0, padx=5, pady=5)
            cost_entry = tk.Entry(add_expense_window)
            cost_entry.grid(row=1, column=1, padx=5, pady=5)

            tk.Label(add_expense_window, text="Category:").grid(row=2, column=0, padx=5, pady=5)
            category_var = tk.StringVar()
            category_var.set("Utilities")  # Default category
            category_dropdown = tk.OptionMenu(add_expense_window, category_var, "Utilities", "Entertainment", "Food", "Rent")
            category_dropdown.grid(row=2, column=1, padx=5, pady=5)

            tk.Label(add_expense_window, text="Date (YYYY-MM-DD):").grid(row=3, column=0, padx=5, pady=5)
            date_entry = tk.Entry(add_expense_window)
            date_entry.grid(row=3, column=1, padx=5, pady=5)

            # Function to add new expense
            def add_new_expense():
                name = name_entry.get()
                cost_str = cost_entry.get()
                category = category_var.get()
                date = date_entry.get()

                # Check if any field is empty
                if not name or not cost_str or not date:
                    messagebox.showerror("Error", "Please fill all fields.")
                    return

                try:
                    cost = float(cost_str)
                    # Insert the new expense
                    self.cursor.execute("INSERT INTO expenses (user_id, name, cost, category, date) VALUES (%s, %s, %s, %s, %s)",
                                        (self.user_id, name, cost, category, date))
                    self.db.commit()
                    messagebox.showinfo("Success", "Expense added successfully!")
                    add_expense_window.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Invalid input.")
                except pymysql.Error as e:
                    messagebox.showerror("Error", f"Error adding expense: {e}")

            # Add Expense Button
            add_button = tk.Button(add_expense_window, text="Add Expense", command=add_new_expense)
            add_button.grid(row=4, columnspan=2, padx=5, pady=10)
        def edit_expense():
            # Open a new window for editing expense
            edit_expense_window = tk.Toplevel()
            edit_expense_window.title("Edit Expense")
            edit_expense_window.geometry("900x600")

            # Labels and entry fields for expense details
            tk.Label(edit_expense_window, text="Expense ID:").grid(row=0, column=0, padx=5, pady=5)
            expense_id_entry = tk.Entry(edit_expense_window)
            expense_id_entry.grid(row=0, column=1, padx=5, pady=5)

            tk.Label(edit_expense_window, text="Name:").grid(row=1, column=0, padx=5, pady=5)
            name_entry = tk.Entry(edit_expense_window)
            name_entry.grid(row=1, column=1, padx=5, pady=5)

            tk.Label(edit_expense_window, text="Cost:").grid(row=2, column=0, padx=5, pady=5)
            cost_entry = tk.Entry(edit_expense_window)
            cost_entry.grid(row=2, column=1, padx=5, pady=5)

            tk.Label(edit_expense_window, text="Category:").grid(row=3, column=0, padx=5, pady=5)
            category_var = tk.StringVar()
            category_var.set("Utilities")  # Default category
            category_dropdown = tk.OptionMenu(edit_expense_window, category_var, "Utilities", "Entertainment", "Food", "Rent")
            category_dropdown.grid(row=3, column=1, padx=5, pady=5)

            tk.Label(edit_expense_window, text="Date (YYYY-MM-DD):").grid(row=4, column=0, padx=5, pady=5)
            date_entry = tk.Entry(edit_expense_window)
            date_entry.grid(row=4, column=1, padx=5, pady=5)

            # Function to load expense details
            def load_expense():
                expense_id = expense_id_entry.get()

                if not expense_id:
                    messagebox.showerror("Error", "Please enter an expense ID.")
                    return

                try:
                    self.cursor.execute("SELECT name, cost, category, date FROM expenses WHERE id = %s AND user_id = %s", (expense_id, self.user_id))
                    expense = self.cursor.fetchone()

                    if expense:
                        name_entry.delete(0, tk.END)
                        name_entry.insert(0, expense[0])

                        cost_entry.delete(0, tk.END)
                        cost_entry.insert(0, str(expense[1]))

                        category_var.set(expense[2])

                        date_entry.delete(0, tk.END)
                        date_entry.insert(0, str(expense[3]))
                    else:
                        messagebox.showerror("Error", "Expense not found.")
                except pymysql.Error as e:
                    messagebox.showerror("Error", f"Error loading expense: {e}")

            # Load Expense Button
            load_button = tk.Button(edit_expense_window, text="Load Expense", command=load_expense)
            load_button.grid(row=0, column=2, padx=5, pady=5)

            # Function to update expense
            def update_expense():
                expense_id = expense_id_entry.get()
                name = name_entry.get()
                cost_str = cost_entry.get()
                category = category_var.get()
                date = date_entry.get()

                if not expense_id:
                    messagebox.showerror("Error", "Please load an expense first.")
                    return

                # Check if any field is empty
                if not name or not cost_str or not date:
                    messagebox.showerror("Error", "Please fill all fields.")
                    return

                try:
                    cost = float(cost_str)
                    # Update the expense
                    self.cursor.execute("UPDATE expenses SET name = %s, cost = %s, category = %s, date = %s WHERE id = %s AND user_id = %s",
                                        (name, cost, category, date, expense_id, self.user_id))
                    self.db.commit()
                    messagebox.showinfo("Success", "Expense updated successfully!")
                    edit_expense_window.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Invalid input.")
                except pymysql.Error as e:
                    messagebox.showerror("Error", f"Error updating expense: {e}")

            # Update Expense Button
            update_button = tk.Button(edit_expense_window, text="Update Expense", command=update_expense)
            update_button.grid(row=5, columnspan=2, padx=5, pady=10)
        
        def view_expenses():
            try:
                # Fetch all expenses for the user
                self.cursor.execute("SELECT id, name, cost, category, date FROM expenses WHERE user_id = %s", (self.user_id,))
                expenses = self.cursor.fetchall()

                total_spend = 0
                for expense in expenses:
                    total_spend += expense[2]

                # Fetch user's income
                self.cursor.execute("SELECT income FROM users WHERE id = %s", (self.user_id,))
                user_income = self.cursor.fetchone()[0]

                remaining_amount = user_income - total_spend

                # Displaying all expenses
                expenses_info = ""
                for expense in expenses:
                    expenses_info += f"ID: {expense[0]}, Name: {expense[1]}, Cost: {expense[2]}, Category: {expense[3]}, Date: {expense[4]}\n"

                messagebox.showinfo("Expenses Overview", f"All Expenses:\n{expenses_info}\nTotal Spend: {total_spend}\nRemaining Amount: {remaining_amount}")
            except pymysql.Error as e:
                messagebox.showerror("Error", f"Error viewing expenses: {e}")
                
        # Open a new window for adding/editing expense
        expense_window = tk.Toplevel()
        expense_window.title("Add/Edit Expense")
        expense_window.geometry("900x600")

        # Add Expense Button
        add_expense_button = tk.Button(expense_window, text="Add Expense", command=add_expense)
        add_expense_button.place(relx=0.5, rely=0.2, anchor="center")

        # Edit Expense Button
        edit_expense_button = tk.Button(expense_window, text="Edit Expense", command=edit_expense)
        edit_expense_button.place(relx=0.5, rely=0.4, anchor="center")

        # View Expenses Button
        view_expense_button = tk.Button(expense_window, text="View Expenses", command=view_expenses)
        view_expense_button.place(relx=0.5, rely=0.6, anchor="center")



    def edit_income(self):
        # Open a new window for editing income
        income_window = tk.Toplevel()
        income_window.title("Edit Income")
        income_window.geometry("900x600")
        # Label and entry field for income
        tk.Label(income_window, text="New Income:").grid(row=0, column=0, padx=5, pady=5)
        income_entry = tk.Entry(income_window)
        income_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to edit income
        def edit_income_inner():
            new_income_str = income_entry.get()

            # Check if the income field is empty
            if not new_income_str:
                messagebox.showerror("Error", "Please enter a valid income.")
                return

            try:
                new_income = float(new_income_str)
                # Update the user's income
                self.cursor.execute("UPDATE users SET income = %s WHERE id = %s", (new_income, self.user_id))
                self.db.commit()
                messagebox.showinfo("Success", "Income updated successfully!")
                income_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid income.")
            except pymysql.Error as e:
                messagebox.showerror("Error", f"Error updating income: {e}")

        # Edit Income Button
        edit_income_button = tk.Button(income_window, text="Edit Income", command=edit_income_inner)
        edit_income_button.grid(row=1, columnspan=2, padx=5, pady=10)
    
    def add_delete_subscription(self):
        def add_subscription_window():
            # Function to add a new subscription
            def add_subscription():
                subscription_name = subscription_name_entry.get()
                subscription_cost = cost_entry.get()
                one_time_payment = one_time_payment_entry.get()
                pay_period = pay_period_entry.get()

                # Check if any field is empty
                if not subscription_name or not subscription_cost or not one_time_payment or not pay_period:
                    messagebox.showerror("Error", "Please fill all fields.")
                    return

                try:
                    # Insert the new subscription
                    self.cursor.execute("INSERT INTO subscriptions (user_id, subscription_name, cost, one_time_payment, pay_period) VALUES (%s, %s, %s, %s, %s)",
                                        (self.user_id, subscription_name, float(subscription_cost), float(one_time_payment), pay_period))
                    self.db.commit()
                    messagebox.showinfo("Success", "Subscription added successfully!")
                    add_subscription_window.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid values for cost and one-time payment.")
                except pymysql.Error as e:
                    messagebox.showerror("Error", f"Error adding subscription: {e}")

            # Open a new window for adding a subscription
            add_subscription_window = tk.Toplevel()
            add_subscription_window.title("Add Subscription")
            add_subscription_window.geometry("900x600")

            # Labels and entry fields for subscription details
            tk.Label(add_subscription_window, text="Subscription Name:").grid(row=0, column=0, padx=5, pady=5)
            subscription_name_entry = tk.Entry(add_subscription_window)
            subscription_name_entry.grid(row=0, column=1, padx=5, pady=5)

            tk.Label(add_subscription_window, text="Cost:").grid(row=1, column=0, padx=5, pady=5)
            cost_entry = tk.Entry(add_subscription_window)
            cost_entry.grid(row=1, column=1, padx=5, pady=5)

            tk.Label(add_subscription_window, text="One-time Payment:").grid(row=2, column=0, padx=5, pady=5)
            one_time_payment_entry = tk.Entry(add_subscription_window)
            one_time_payment_entry.grid(row=2, column=1, padx=5, pady=5)

            tk.Label(add_subscription_window, text="Pay Period:").grid(row=3, column=0, padx=5, pady=5)
            pay_period_entry = tk.Entry(add_subscription_window)
            pay_period_entry.grid(row=3, column=1, padx=5, pady=5)

            # Add Subscription Button
            add_subscription_button = tk.Button(add_subscription_window, text="Add Subscription", command=add_subscription)
            add_subscription_button.grid(row=4, columnspan=2, padx=5, pady=10)

        def delete_subscription():
            # Function to delete a subscription
            def delete_subscription_inner():
                subscription_name = subscription_name_entry.get()

                # Check if the field is empty
                if not subscription_name:
                    messagebox.showerror("Error", "Please enter the subscription name.")
                    return

                try:
                    # Delete the subscription
                    self.cursor.execute("DELETE FROM subscriptions WHERE user_id = %s AND subscription_name = %s",
                                        (self.user_id, subscription_name))
                    self.db.commit()
                    messagebox.showinfo("Success", "Subscription deleted successfully!")
                    delete_subscription_window.destroy()
                except pymysql.Error as e:
                    messagebox.showerror("Error", f"Error deleting subscription: {e}")

            # Open a new window for deleting a subscription
            delete_subscription_window = tk.Toplevel()
            delete_subscription_window.title("Delete Subscription")
            delete_subscription_window.geometry("900x600")

            # Labels and entry fields for subscription details
            tk.Label(delete_subscription_window, text="Subscription Name:").grid(row=0, column=0, padx=5, pady=5)
            subscription_name_entry = tk.Entry(delete_subscription_window)
            subscription_name_entry.grid(row=0, column=1, padx=5, pady=5)

            # Delete Subscription Button
            delete_subscription_button = tk.Button(delete_subscription_window, text="Delete Subscription", command=delete_subscription_inner)
            delete_subscription_button.grid(row=1, columnspan=2, padx=5, pady=10)

        # Open a new window for adding/deleting subscription
        subscription_window = tk.Toplevel()
        subscription_window.title("Add/Delete Subscription")
        subscription_window.geometry("900x600")
        

        # Add Subscription Button
        add_subscription_button = tk.Button(subscription_window, text="Add Subscription", command=add_subscription_window)
        add_subscription_button.place(relx=0.5, rely=0.3, anchor="center")

        # Delete Subscription Button
        delete_subscription_button = tk.Button(subscription_window, text="Delete Subscription", command=delete_subscription)
        delete_subscription_button.place(relx=0.5, rely=0.5, anchor="center")
    
    def add_edit_debt(self):
        def add_debt_window():
            # Function to add a new debt
            def add_debt():
                debt_amount_str = debt_entry.get()
                interest_str = interest_entry.get()

                # Check if the debt and interest fields are empty
                if not debt_amount_str or not interest_str:
                    messagebox.showerror("Error", "Please enter valid debt amount and interest.")
                    return

                try:
                    debt_amount = float(debt_amount_str)
                    interest = float(interest_str)
                    # Insert the new debt
                    self.cursor.execute("INSERT INTO debts (user_id, debt, interest) VALUES (%s, %s, %s)",
                                        (self.user_id, debt_amount, interest))
                    self.db.commit()
                    messagebox.showinfo("Success", "Debt added successfully!")
                    add_debt_window.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid debt amount and interest.")
                except pymysql.Error as e:
                    messagebox.showerror("Error", f"Error adding debt: {e}")

            # Open a new window for adding a debt
            add_debt_window = tk.Toplevel()
            add_debt_window.title("Add Debt")
            add_debt_window.geometry("900x600")

            # Labels and entry fields for debt details
            tk.Label(add_debt_window, text="Debt Amount:").grid(row=0, column=0, padx=5, pady=5)
            debt_entry = tk.Entry(add_debt_window)
            debt_entry.grid(row=0, column=1, padx=5, pady=5)

            tk.Label(add_debt_window, text="Interest:").grid(row=1, column=0, padx=5, pady=5)
            interest_entry = tk.Entry(add_debt_window)
            interest_entry.grid(row=1, column=1, padx=5, pady=5)

            # Add Debt Button
            add_debt_button = tk.Button(add_debt_window, text="Add Debt", command=add_debt)
            add_debt_button.grid(row=2, columnspan=2, padx=5, pady=10)

        def edit_debt_window():
            # Function to edit an existing debt
            def edit_debt():
                new_debt_amount_str = new_debt_entry.get()
                new_interest_str = new_interest_entry.get()
                debt_id_str = debt_id_entry.get()  # Get the debt ID

                # Check if the new debt, interest, and debt ID fields are empty
                if not new_debt_amount_str or not new_interest_str or not debt_id_str:
                    messagebox.showerror("Error", "Please enter valid debt amount, interest, and debt ID.")
                    return

                try:
                    new_debt_amount = float(new_debt_amount_str)
                    new_interest = float(new_interest_str)
                    debt_id = int(debt_id_str)
                    # Update the existing debt
                    self.cursor.execute("UPDATE debts SET debt = %s, interest = %s WHERE id = %s AND user_id = %s",
                                        (new_debt_amount, new_interest, debt_id, self.user_id))
                    self.db.commit()
                    messagebox.showinfo("Success", "Debt updated successfully!")
                    edit_debt_window.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid debt amount, interest, and debt ID.")
                except pymysql.Error as e:
                    messagebox.showerror("Error", f"Error updating debt: {e}")

            # Open a new window for editing a debt
            edit_debt_window = tk.Toplevel()
            edit_debt_window.title("Edit Debt")
            edit_debt_window.geometry("900x600")

            # Labels and entry fields for debt details
            tk.Label(edit_debt_window, text="New Debt Amount:").grid(row=0, column=0, padx=5, pady=5)
            new_debt_entry = tk.Entry(edit_debt_window)
            new_debt_entry.grid(row=0, column=1, padx=5, pady=5)

            tk.Label(edit_debt_window, text="New Interest:").grid(row=1, column=0, padx=5, pady=5)
            new_interest_entry = tk.Entry(edit_debt_window)
            new_interest_entry.grid(row=1, column=1, padx=5, pady=5)

            tk.Label(edit_debt_window, text="Debt ID:").grid(row=2, column=0, padx=5, pady=5)
            debt_id_entry = tk.Entry(edit_debt_window)
            debt_id_entry.grid(row=2, column=1, padx=5, pady=5)

            # Edit Debt Button
            edit_debt_button = tk.Button(edit_debt_window, text="Edit Debt", command=edit_debt)
            edit_debt_button.grid(row=3, columnspan=2, padx=5, pady=10)

        # Open a new window for adding/editing debt
        debt_window = tk.Toplevel()
        debt_window.title("Add/Edit Debt")
        debt_window.geometry("900x600")

        # Add Debt Button
        add_debt_button = tk.Button(debt_window, text="Add Debt", command=add_debt_window)
        add_debt_button.place(relx=0.5, rely=0.3, anchor="center")

        # Edit Debt Button
        edit_debt_button = tk.Button(debt_window, text="Edit Debt", command=edit_debt_window)
        edit_debt_button.place(relx=0.5, rely=0.5, anchor="center")



    def add_edit_budget(self):
        # Open a new window for adding/editing budget
        budget_window = tk.Toplevel()
        budget_window.title("Add/Edit Budget")
        budget_window.geometry("900x600")

        # Label and entry field for budget
        tk.Label(budget_window, text="New Budget:").grid(row=0, column=0, padx=5, pady=5)
        budget_entry = tk.Entry(budget_window)
        budget_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to edit budget
        def edit_budget_inner():
            new_budget_str = budget_entry.get()

            # Check if the budget field is empty
            if not new_budget_str:
                messagebox.showerror("Error", "Please enter a valid budget.")
                return

            try:
                new_budget = float(new_budget_str)
                # Update the user's budget
                self.cursor.execute("UPDATE users SET budget = %s WHERE id = %s", (new_budget, self.user_id))
                self.db.commit()
                messagebox.showinfo("Success", "Budget updated successfully!")
                budget_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid budget.")
            except pymysql.Error as e:
                messagebox.showerror("Error", f"Error updating budget: {e}")

        # Edit Budget Button
        edit_budget_button = tk.Button(budget_window, text="Edit Budget", command=edit_budget_inner)
        edit_budget_button.grid(row=1, columnspan=2, padx=5, pady=10)

    def show_meals(self):
        # Open a new window for displaying meal options
        self.meals_window = tk.Toplevel()
        self.meals_window.title("Meal Options")
        self.meals_window.geometry("900x600")

        # Frame for displaying meal options
        meals_frame = tk.Frame(self.meals_window)
        meals_frame.pack(padx=20, pady=20)

        # Title label
        title_label = tk.Label(meals_frame, text="Meal Options", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Label for ingredients wishlist
        wishlist_label = tk.Label(meals_frame, text="Ingredients Wishlist:")
        wishlist_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        # Entry for ingredients wishlist
        wishlist_entry = tk.Entry(meals_frame)
        wishlist_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        # Label for blacklist
        blacklist_label = tk.Label(meals_frame, text="Blacklist for Allergies:")
        blacklist_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

        # Entry for blacklist
        blacklist_entry = tk.Entry(meals_frame)
        blacklist_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        # Button to display meal options
        display_button = tk.Button(meals_frame, text="Display Meal Options", command=lambda: self.display_meal_options(wishlist_entry.get(), blacklist_entry.get()))
        display_button.grid(row=3, columnspan=2, pady=10)

    def display_meal_options(self, wishlist, blacklist):
        try:
            user_id = 1  # Assuming user_id is hardcoded for demonstration

            # Fetch all meals initially
            self.cursor.execute("SELECT food, price, ingredients FROM meals WHERE user_id = %s", (user_id,))
            all_meals = self.cursor.fetchall()

            # Filter meals based on wishlist and blacklist
            filtered_meals = []
            for meal in all_meals:
                ingredients = meal[2].split(', ')
                if not wishlist or any(item in wishlist.split(', ') for item in ingredients):
                    if not blacklist or not any(item in blacklist.split(', ') for item in ingredients):
                        filtered_meals.append(meal)

            if filtered_meals:
                # Frame for displaying meal options
                options_frame = tk.Frame(self.meals_window)
                options_frame.pack(padx=20, pady=20)

                # Title label
                title_label = tk.Label(options_frame, text="Meal Options", font=("Helvetica", 16, "bold"))
                title_label.grid(row=0, column=0, columnspan=2, pady=10)

                # Display meal options
                row = 1
                for meal in filtered_meals:
                    food_label = tk.Label(options_frame, text=meal[0])
                    food_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)

                    price_label = tk.Label(options_frame, text=f"${meal[1]:.2f}")
                    price_label.grid(row=row, column=1, sticky="e", padx=5, pady=5)

                    ingredients_label = tk.Label(options_frame, text=meal[2], wraplength=400, justify="left")
                    ingredients_label.grid(row=row+1, column=0, columnspan=2, padx=5, pady=5)

                    row += 2
            else:
                messagebox.showinfo("Info", "No meal options found.")

        except pymysql.Error as e:
            print("Error retrieving meal options:", e)



    def logout(self):
        # Close the budget manager window and show the login window
        self.root.deiconify()  # Show the login window
        self.root.destroy()  # Close the budget manager window

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetManagerApp(root)
    root.mainloop()

    #cd C:\Users\Romario Salama\Desktop\School\343\budget app\Budget App
    #python Budget_App.py
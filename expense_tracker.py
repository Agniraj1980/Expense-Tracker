format_output = "\033[47m\033[30m"
format_reset = "\033[0m"
 
# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")

# creating the nested dictionary with example entries
expenses = {
	1: {"amount": 60.00, "category": "Entertainment", "desc": "Concert"},
    2: {"amount": 20.00, "category": "Entertainment", "desc": "Movie"},
    3: {"amount": 35.90, "category": "Food", "desc": "Groceries"},
    4: {"amount": 700.00, "category": "Bills", "desc": "Rent"},
    5: {"amount": 10.99, "category": "Subscription", "desc": "Netflix"},
    6: {"amount": 23.99, "category": "Bills", "desc": "mobile"},
    7: {"amount": 42.58, "category": "Food", "desc": "Restaurant"},
    8: {"amount": 7.99, "category": "Subscription", "desc": "Audible"}
}

#  An example collection of categories and subtotals
cate_gory = {
    "Entertainment": 0,
    "Food": 0,
    "Bills": 0,
    "Subscription": 0,
    "Miscellaneous": 0
} 


# Log an expense
def log_expense():
    try:    
        id = int(input("Please enter the id: "))
        for i in expenses:
            if id == i:
                raise KeyError
        amount = float(input("Please enter the amount: "))
        if amount <= 0 or amount == "":
            raise ValueError
        category = input("Please enter the category: ")
        if category == "Entertainment" or category == "Food" or category == "Bills" or category == "Subscription" or category == "Miscellaneous":
            desc = input("Please enter the description: ")
            expenses[id] = {"amount": amount, "category": category, "desc": desc}    
            print(f"    {id}: {amount} ({category}:{desc}) logged successfully")
            carry_on()
        else:
            print("    [Error: Please enter a valid category]    ")
            log_expense()
    except KeyError:
        print(f"    [Error: entry already exists]    ")
        log_expense()
    except ValueError:
        print(f"    [Error: Please enter a valid amount]    ")
        log_expense()
    except Exception as e:
        print(f"    [An error occured: {e}]    ")
        carry_on()


# Show all expenses method 1
def show_all():
    try:
        for i in expenses:
            print(f"    {i}: £{"{:.2f}".format(expenses[i]["amount"])} spent on {expenses[i]["category"]}: {expenses[i]["desc"]}")
    except Exception as e:
        print(f"    [An error occured: {e}]    ")
        carry_on()


# Show all expenses method 2
def show_all_expenses():
    try:
        print ("    {:<4} {:<10} {:<18} {:<18}".format('ID','Amount(£)','Category','Description'))
        for k, v in expenses.items():
            amount, category, desc = v
            print ("    {:<4} {:<10} {:<18} {:<18}".format(k, "{:.2f}".format(expenses[k]["amount"]), expenses[k]["category"], expenses[k]["desc"]))
    except Exception as e:
        print(f"    [An error occured: {e}]    ")
        carry_on()        


# Total expense
def total_expense():
    sum = 0
    try:
        for i in expenses:
            sum += (expenses[i]["amount"])
        print(f"    The current total expense is £{"{:.2f}".format(sum)}")
    except Exception as e:
        print(f"     [An error occured: {e}]    ")
        carry_on()


# Total expense per category method 1
def total_per_category():
    sum_ent = 0
    sum_foo = 0
    sum_bil = 0
    sum_sub = 0
    sum_mis = 0
    try: 
        for i in expenses:
            if expenses[i]["category"] == "Entertainment":
                sum_ent += (expenses[i]["amount"])
            elif expenses[i]["category"] == "Food":
                sum_foo += (expenses[i]["amount"])
            elif expenses[i]["category"] == "Bills":
                sum_bil += (expenses[i]["amount"])
            elif expenses[i]["category"] == "Subscription":
                sum_sub += (expenses[i]["amount"])
            else:
                sum_mis += (expenses[i]["amount"])
        print(f"    Total Entertainment Expense: £{"{:.2f}".format(sum_ent)}")
        print(f"    Total Food Expense: £{"{:.2f}".format(sum_foo)}") 
        print(f"    Total Bills Expense: £{"{:.2f}".format(sum_bil)}") 
        print(f"    Total Subscription Expense: £{"{:.2f}".format(sum_sub)}")
        print(f"    Total Miscellaneous Expense: £{"{:.2f}".format(sum_mis)}")  
    except Exception as e:
        print(f"    [An error occured: {e}]    ")
        carry_on()


# Total expense per Category method 2
def tot_per_category():
    for i in expenses:
        for j in cate_gory:
            if expenses[i]["category"] == j:
                cate_gory[j] += expenses[i]["amount"]
    for j in cate_gory:
        print(f"    Total {j} expense: £{"{:.2f}".format(cate_gory[j])}")




# Introduction
def intro():
    print("    [Welcome to Expense Tracker 1.0]    ")


#########
intro()##
#########


# Main Menu
def menu():
    print("    [Main Menu]    ")
    main_menu = {
        1: "Log an expense",
        2: "Show all expenses",
        3: "Show Total expense",
        4: "Show Total expense per category",
        5: "Exit"
}
    for key in main_menu:    
        print(f"    {[key]}: {main_menu[key]}")


########
menu()##
########


# Returning to the Main Menu
def carry_on():
    try:
        choice_2 = int(input("Enter [1] for Main Menu or [2] for Exit: "))
        if choice_2 == 1:
            menu()
            user_choice()
        elif choice_2 == 2:
            print("    [Thank you for using Expense Tracker]    ")
            return
        else:
            raise ValueError
    except ValueError:
        print("invalid entry: Please enter 1 or 2")
        carry_on()
    except Exception as e:
        print(f"An error occured: {e}")
        carry_on()


# User's Choice
def user_choice():
    try:
        choice = int(input("Please choose an option: "))
        
        match choice:
            case 1:
                print("====[Log an expense]====")
                log_expense()
            case 2:
                print("====[Show all expenses]====")
                show_all_expenses()
                carry_on()
            case 3:
                print("====[Show Total expense]====")
                total_expense()
                carry_on()
            case 4:
                print("====[Show Total expense per category]====")
                tot_per_category()
                carry_on()
            case 5:
                print("    [Thank you for using Expense Tracker]    ")
                return
            case _:
                print("    [Invalid entry: Please enter a number between 1 and 5]    ")
                user_choice()
    except ValueError:
        print("    [Invalid entry: Please enter a number between 1 and 5]    ")
        user_choice()
    except Exception as e:
        print(f"    [An error occured: {e}]    ")
        user_choice()


###############
user_choice()##
###############







































# Formatted Message - Signify End of Output
print(f"{format_output}---END---{format_reset}")

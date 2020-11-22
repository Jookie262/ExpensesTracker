# Codes by Jookie262 - November 22, 2020
# This app is at the terminal phase 

# =================== Import Libraries Here ==========================#
import csv
import os.path
import texttable
# ==================== Create Method Here ============================#

# This method is use to ask user about the information
def save_items(): 
    # Ask user for an item that you have spent
    input_name = input("Item that I spent money today: ")
    # Ask user for the price of the item
    input_price = input("How much did I spent? ₱")
    # Returns name and price of the item
    return input_name, input_price

# This method is used to store data in the csv file
def add_spent(name, ammount): 
    with open("data/items.csv", "a") as save_file:
        save_file.write('\n'+ name + ',' + ammount)

# This method prints the CSV data in table view
def expenses_summary():
    # using texttable pip
    val = ['','']
    dic = csv.DictReader(open("data/items.csv"))
    for data in dic:
        val[0] += data['name'] + "\n"
        val[1] += data['price'] + "\n"

    table = texttable.Texttable()
    table.add_rows(
                [
                ['Name', 'Price'],
                [val[0], val[1]],
                ['Total Expenses', total_expenses()]
                ])
    return(table.draw())

# This method gets and calculate for the total expenses found in items.csv
def total_expenses():
    total_price = 0;
    input_file = csv.DictReader(open("data/items.csv"))
    for data in input_file:
        total_price += float(data['price'])
    return str(total_price)

# This method is used to check if the item.csv is in the file
# if the csv file is not exist this method will create it
# if the csv file is already exist it will disregard it
def check_CSV():
    if not os.path.exists('data/items.csv'):
        #create a cvs for items
        save_file = open('data/items.csv','a')
        save_file.write('name' + ',' + 'price' + '\n')
        save_file.close()


# This is the main method of the proram that ask users for options
def main():
    print("-------------------------------------------------------------------")
    print("Savings Tracker at your service, choose the following options you want:")
    print("1. Save items today")
    print("2. View savings summary")
    print("3. End the program")
    print("-------------------------------------------------------------------")
    options = input("> ")
    
    if(options == '1'):
        name, ammount = save_items()
        # Calling out the function add_spent
        add_spent(name, ammount)
        main()
    elif(options == '2'):
        # Printin the result in the expenses_summary method
        print(expenses_summary())
        main()

# ==================== Callout Method Here ===========================#

# Lets check if out csv files are created 
# If not then this method will created the missing ones
check_CSV()

# call the main function
main()

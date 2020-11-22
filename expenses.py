# Codes by Jookie262 - November 22, 2020
# This app is at the terminal phase 

# =================== Import Libraries Here ==========================#
import csv
import os.path
import texttable
import datetime
# ==================== Create Method Here ============================#

# This method is use to ask user about the information
def save_items(): 
    # Automatically inputs time based on the users computer
    auto_datetime = str(datetime.datetime.now())
    # Ask user for an item that you have spent
    input_name = input("Item that I spent money today: ")
    # Ask user for the price of the item
    input_price = input("How much did I spent? ₱")
    # Returns name and price of the item
    return auto_datetime, input_name, input_price

# This method is used to store data in the csv file
def add_spent(date, name, ammount): 
    with open("data/items.csv", "a") as save_file:
        save_file.write('\n' + date + ',' + name + ',' + ammount)

# This method prints the CSV data in table view
def expenses_summary():
    # using texttable pip
    val = ['','','']
    dic = csv.DictReader(open("data/items.csv"))
    for data in dic:
        cr_date = datetime.datetime.strptime(data['datetime'], '%Y-%m-%d %H:%M:%S.%f')
        cr_date = cr_date.strftime("%B %d %Y")
        val[0] += cr_date + "\n"
        val[1] += data['name'] + "\n"
        val[2] += data['price'] + "\n"

    print(dic)

    table = texttable.Texttable()
    table.add_rows(
                [
                ['Date', 'Name', 'Price'],
                [val[0], val[1], val[2]],
                ['Total Expenses', '', total_expenses()]
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
        save_file.write('datetime' + ',' + 'name' + ',' + 'price' )
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
        date, name, ammount = save_items()
        # Calling out the function add_spent
        add_spent(date, name, ammount)
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

#Testing codes here

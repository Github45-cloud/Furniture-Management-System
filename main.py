#Importing necessary functions 
from operations import buy_furniture, sell_furniture
from read import read_stock

def main():
    # File that contains the stock information
    file_name = "stock.txt"
    # Reading the stock data from the file
    stock = read_stock(file_name)

    # Starting Infinite loop
    while True:
    
        print("\n" + "=" * 152)
        print(" \t\t\t\t\t\t\t BRJ FURNITURE STORE MANAGEMENT SYSTEM ")
        print("\n")
        print(" \t\t\t\t\t\t\t Location: Radhe Radhe, Bhaktapur")
        print("\n")
        print(" \t\t\t\t\t\t\t Contact no:9874522134")
        print("=" * 152)
        print("1. Buy Furniture")
        print("2. Sell Furniture")
        print("3. Exit")
        print("=" * 152)

        try:
            # Taking user input 
            option = int(input("Enter your choice (1-3): "))
            
            if option < 1 or option > 3:
                print(" Invalid option. Please choose a number between 1 and 3.")
            elif option == 1:
                # Calls the buy_furniture function if option 1
                buy_furniture(stock, file_name)
            elif option == 2:
                # Calls the sell_furniture function if option 2
                sell_furniture(stock, file_name)
            elif option == 3:
                # Exit the program if user chooses option 3
                print("Thank you for using our System, Bye Bye!")
                
                break #Breaking infinite loop
        except ValueError:
            # Gives error message if input is not integer
            print("Invalid input. Please enter a valid number from 1-3")

if __name__ == "__main__":
    main()

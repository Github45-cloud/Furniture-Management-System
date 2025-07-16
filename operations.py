from datetime import datetime
from write import write_stock

def buy_furniture(stock, file_name):
    """Handles the process of buying furniture."""
    customer_name = input("Enter your name: ")

    #initializing variables to keep track
    final_price = 0
    purchased_items = []

    while True:#Infinite loop
        #Checks available stocks
        if not stock:
            print("No furniture available in Stock.")
            break
        
        # Displays available furniture with details
        print("ID | Manufacturer | Product Name | Quantity | Price")
        print("---------------------------------------------------------")
        for item_id, info in stock.items():
            print(str(item_id) + " | " + info['manufacturer'] + " | " + info['product_name'] + " | " + str(info['quantity']) + " | $" + str(info['price']))
        print("-----------------------------------------------------")

        #Asks for a valid furniture ID
        item_id = input("Enter the ID of the furniture you want to buy: ")
        if item_id in stock:
            #Asks for a valid quantity
            quantity = int(input("Enter the quantity you want to buy: "))
            if quantity <= stock[item_id]['quantity']:
                item_price = stock[item_id]['price']#Retrives the price of an item from stock dictionary using item ID
                final_price += item_price * quantity#final_price=final_price+(item_price*quantity)
                purchased_items.append((stock[item_id]['product_name'], quantity, item_price * quantity))

                # Updating our stock
                stock[item_id]['quantity'] -= quantity
                if stock[item_id]['quantity'] == 0:
                    del stock[item_id]

                # Asks if the user wants to continue shopping
                more_shopping = input("Do you want to shop more? (y/n): ").lower()
                if more_shopping != 'y':
                    break
            else:#Error messages for invalid input
                print("Quantity  is more than what is available in the stock .")
        else:
            print("Invalid ID. Please input a valid ID.")

    # Ask about shipping cost
    shipping_cost = 0
    ship_response = input("Would you like to add shipping? (y/n): ").lower()
    if ship_response == 'y':
        shipping_cost = int(input("Enter the shipping cost: "))

    # Applying VAT (13%) and generating the bill
    vat = final_price * 0.13
    total_with_vat_and_shipping = final_price + vat + shipping_cost
    bill_content = create_bill(customer_name, purchased_items, final_price, vat, total_with_vat_and_shipping, selling=False, shipping_cost=shipping_cost)

    #Displays the generated bill
    print("\nYour Bill:")
    print(bill_content)

    # Write the bill to a file
    bill_name = customer_name + '-' + datetime.now().strftime('%Y/%m/%d_%H-%M%-S') + '.txt'
    with open(bill_name, 'w') as bill_file:
        bill_file.write(bill_content)

    # The updated stock is written back to the file
    write_stock(file_name, stock)

    print("Thank you for shopping, " + customer_name + "! This is your BILL")
    

def sell_furniture(stock, file_name):
    """Handles the process of selling furniture."""
    customer_name = input("Enter your name: ")

    #Initializing variabls
    total_earns = 0
    sold_items = []

    while True:
        #Checking the stocks
        if not stock:
            print("No furniture available in the inventory.")
            break
        
    #Displays available stock in detail
        print("ID | Manufacturer | Product Name | Quantity | Price")
        print("-----------------------------------------------------")
        for item_id, info in stock.items():
            print(str(item_id) + " | " + info['manufacturer'] + " | " + info['product_name'] + " | " + str(info['quantity']) + " | $" + str(info['price']))
        print("-----------------------------------------------------")

        #Asks the user to input valid ID
        item_id = input("Enter the ID of the furniture you want to sell: ")
        if item_id in stock:
            quantity = int(input("Enter the quantity you want to sell: "))

            #Updating the stocks
            stock[item_id]['quantity'] += quantity #adds the quantity
            item_price = stock[item_id]['price']
            total_earns += item_price * quantity #total_earns=total_earns+(item*quantity)
            sold_items.append((stock[item_id]['product_name'], quantity, item_price * quantity))

            # Asks if the user wants to continue selling
            more_selling = input("Do you want to sell more? (y/n): ").lower()
            if more_selling != 'y':
                break #exits infinite loop
        else:
            print("Invalid ID. Please try again.")

    # Asks about shipping cost for selling
    shipping_cost = 0
    ship_response = input("Would you like to add shipping? (y/n): ").lower()
    if ship_response == 'y':
        shipping_cost = int(input("Enter the shipping cost: "))

    # Applying  13% VAT and calculate total
    vat = total_earns * 0.13
    total_with_vat_and_shipping = total_earns + vat + shipping_cost
    bill = create_bill(customer_name, sold_items, total_earns, vat, total_with_vat_and_shipping, selling=True, shipping_cost=shipping_cost)

    #Displays ou bill on screen
    print("\nYour Bill:")
    print(bill)

    # Write the bill to a file
    bill_name = customer_name + '-' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.txt'
    with open(bill_name, 'w') as bill_file:
        bill_file.write(bill)

    # Writes the updated stock back to the file
    write_stock(file_name, stock)

    print("Thank you for selling, " + customer_name + "! Your bill has been generated.")
    

def create_bill(customer_name, items, subtotal, vat, total, selling, shipping_cost):
    """Generates the bill content inside a simple box."""
    bill_type = "Sale" if selling else "Purchase"
    bill_design = [
        "Customer Name: " + customer_name,
        "Date: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "Bill Type: " + bill_type,
        "-------------------------------------------",
        "Item Name | Quantity | Total Price",
        "--------------------------------------------"
    ]
    
    for item_name, quantity, price in items:
        bill_design.append(item_name + " | " + str(quantity) + " | $" + str(price))
    
    bill_design.append("----------------------------------------")
    bill_design.append("Subtotal: $" + str(subtotal))
    bill_design.append("VAT (13%): $" + str(vat))
    bill_design.append("Shipping Charges: $" + str(shipping_cost))
    bill_design.append("Total: $" + str(total))
    
    # Generating the box with a  border
    border = '-' * 50
    square_bill = [border]
    for line in bill_design:
        square_bill.append("! " + line.ljust(48) + " !")
    square_bill.append(border)
    
    return "\n".join(square_bill)#Join is used to combine all the elements into single string

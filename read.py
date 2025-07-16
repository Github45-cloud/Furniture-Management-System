
def read_stock(file_name):
    """Reads the stock from the file and returns it as a dictionary."""
    stock = {}
    try:
        #Opening file in read mode
        with open(file_name, 'r') as file:
            
            for line in file:
                #Splits the line items into 5 items
                products = line.split(',')
                #Only processes if there are 5 items in the list
                if len(products) == 5:
                    item_id = products[0] # Extract the item ID from the first element of the split line
                    manufacturer = products[1]# Extract manufacturer from the second element of the split line
                    product_name = products[2] # Extract the product_name from the third element of the split line
                    quantity = int(products[3]) # Extract quantity from the fourth element , converting it to integer
                    price = float(products[4].replace('$', '').replace(',', ''))  
                    
                    # Adds the item details to the stock dictionary using item_id as the key
                    stock[item_id] = {
                        'manufacturer': manufacturer,
                        'product_name': product_name,
                        'quantity': quantity,
                        'price': price
                    }
    except Exception as e:
        print("An error has occurred while reading the stock")

    return stock

def write_stock(file_name, stock):
    try:
        # Opening file in write mode
        with open(file_name, 'w') as file:
            for item_id, info in stock.items():
                #Writing each items in the stock
                file.write(str(item_id) + ',' + str(info['manufacturer']) + ',' + str(info['product_name']) + ',' + str(info['quantity']) + ',' + str(info['price']) + '\n')

    except Exception as e:
        print("There is a Error!!!")

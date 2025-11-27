def main_menu():
    return {
        1: "Open Cafe",
        2: "Close Cafe"
    }
    
def disp_main_menu(menu_dict):
    while True:
        print("Welcome to the Main Menu\n")
        for k,v in menu_dict.items():
            print(f"{k}. {v}")
    
        while True:
            selection = input("Enter '1' to open application. Enter '2' to close it:\n")
        
            if selection not in ("1","2"):
                print("Invalid entry. Try again.")
                continue
            if selection == "1":
                return True
            else:
                return False      

def cafe_menu():
        
        menu = dict(
            Coffee = 5.25,
            Tea = 3.50,
            Sandwich = 6.50,
            Muffin = 3.75,
            Cookie = 2.50,
            Smoothie = 5.25
            )
        return menu

def display_menu(menu):

    print("{:^25}\n".format("Welcome to our shop!"))
    print("{:^25}".format("- - - CAFE MENU - - -"))

    for k,v in menu.items():
            line = "{:<15} ${:>5.2f}\n".format(k,v)
            print("{:^25}".format(line))

def build_cart():

    return []

def get_item_choice(menu):

    while True:
        item = input("Enter the name of the item you wish to add to your order, or enter 'checkout' to complete your order:\n")
        item = item.strip().capitalize()

        if item == "Checkout":
            return item

        if item not in menu:
            print(f"Sorry, we do not sell an item called {item}. Please select an item in the menu or check out.\n")
            continue

        return item

def get_quantity(item):

    while True: 
            try:
                quantity = int(input(f"How many {item}(s) would you like to add to your order?:\n"))

                if quantity >= 30:
                    print("This quantity cannot be fulfilled without contacting our catering dept. Please reduce the quantity to less than 30.")
                    continue
                
                if quantity < 1:
                    print("Quanitity must be at least 1. Please update the quantity you wish to add.")
                    continue

                return quantity
            
            except ValueError:
                print("Quantity must be a whole number. Please check your input and try again.")

def add_item_cart(cart,item,quantity):

    cart.append((item,quantity))
    print(f"{quantity} {item}(s) added to your order.\n")
    return cart

def confirm_order(cart):

    print("Let's verify your order is correct.\n")
    print("Your order:\n")
            
    # show current order
    for i, thing in enumerate(cart):
        print(f"Item #{i+1}: {thing[0]}")
        print(f"Quantity: {thing[1]}\n")

    print("Does this look correct?\n")

    # Ask Y/N. Ensure valid response.
    while True:
        correct = input("Enter 'y' to proceed, or 'n' to update the order:\n").strip().lower()

        if correct not in ("y","n"):
            print("Invalid entry. Try again")
            continue

        return correct

def edit_order(cart):
    while True:
        # show current cart
        print("Your current order:\n")
        for i, item in enumerate(cart):
            print(f"{i+1}. {item[0]}")
            print(f"Quantity: {item[1]}\n")

        # step 1. choose an operation first
        operations = ["Change quantity", "Remove Item", "Add More Items"]

        print("What would you like to do?\n")
        for n, option in enumerate(operations):
            print(f"{n+1}: {option}\n")

        # validate operation choice
        while True:
            try:
                op_choice = int(input("Enter a number for the operation you wish to complete:\n"))
                op_idx = op_choice - 1

                if op_idx not in range(len(operations)):
                    print("Invalid entry. Try again.")
                    continue

                break
            except ValueError:
                print("Entry must be a whole number corresponding with a valid operation. Try again.\n")

        # if they chose Add More Items
        if op_choice == 3:
            print("Returning to menu to add more items.\n")
            return ("add more items", cart)

        # reprint cart before asking which item to edit/remove
        print("\nHere is your order again:\n")
        for i, item in enumerate(cart):
            print(f"{i+1}. {item[0]}")
            print(f"Quantity: {item[1]}\n")

        # ask which specific item they want to touch
        while True:
            try:
                update = int(input("Enter the number of the item you want to update/remove:\n"))
                update_idx = update - 1

                if update_idx not in range(len(cart)):
                    print("Sorry. The number you entered does not match any item in your order. Try again.\n")
                    continue

                break  
            except ValueError:
                print("Entry must be a whole number that matches an item in your order.\n")

        # 1. change quantity
        if op_choice == 1:
            while True:
                try:
                    quantity = int(input("What quantity do you want instead?:\n"))

                    if quantity >= 30:
                        print("This quantity cannot be fulfilled without contacting our catering dept. Please reduce the quantity to less than 30.\n")
                        continue

                    if quantity < 1:
                        print("Quantity must be at least 1. Please update the quantity you wish to add.\n")
                        continue

                    name = cart[update_idx][0]
                    cart[update_idx] = (name, quantity)

                    print(f"Quantity of {name} updated to {quantity}\n")
                    break

                except ValueError:
                    print("Quantity must be a whole number. Please check your input and try again.\n")

        # 2. remove item
        elif op_choice == 2:
            removed_item = cart.pop(update_idx)
            print(f"{removed_item} successfully removed from your order.\n")

            if len(cart) == 0:
                print("Your order is now empty.\n")

        # ask if more edits
        while True:
            more_edits = input("Do you need to make more changes to your order? Enter 'y' to keep editing or 'n' if you're done editing:\n").strip().lower()
            if more_edits not in ("y", "n"):
                print("Invalid entry. Try again.\n")
                continue
            break

        if more_edits == "n":
            return ("done editing", cart)

def cafe():

    menu = cafe_menu()
    cart = build_cart()
    ordering = True

    while True:
        # ORDERING PHASE
        while ordering:
            display_menu(menu)

            item = get_item_choice(menu)

            if item == "Checkout":
                if len(cart) == 0:
                    print("Your order is empty. To check out, please add an item to your order.")
                    continue
                break
        
            quantity = get_quantity(item)

            cart = add_item_cart(cart,item,quantity)

            while True:
                again = input("Add another item? Enter 'y' to add another item or 'n' to check out:\n").strip().lower()
                if again not in ("y","n"):
                    print("Invalid entry. Please check your input and try again.")
                    continue
                break
        
            if again == "n":
                ordering = False  # leave the ordering phase and move to checkout
    
        # CONFIRM / EDIT PHASE
        while True:
            # guard against empty cart before confirming
            if len(cart) == 0:
                print("Your order is currently empty. You must add at least one item before checking out.\n")
                ordering = True
                break  # go back to ordering to add items

            correct = confirm_order(cart)

            if correct == "y":
                # final guard, just in case
                if len(cart) == 0:
                    print("Your order is empty. Please add an item before checking out.\n")
                    ordering = True
                    break
                print("Order confirmed. Proceeding to checkout.")
                return cart  # final approved cart
            
            status, cart = edit_order(cart)

            if status == "add more items":
                ordering = True
                break

            if status == "done editing":
                continue

def calc_subtotal(menu,cart):

    subtotal = 0
    order_data = []
    for i, item in enumerate(cart):
        item_name = item[0]
        quantity = item[1]
        item_cost = menu.get(item_name)
        ext_cost = quantity * item_cost
        item_data = {
            "item": item_name, 
            "item cost": item_cost, 
            "quantity": quantity, 
            "extended cost": ext_cost
        }
        order_data.append(item_data)
        subtotal += ext_cost
    
    return (subtotal, order_data)

def calc_disc(subtotal, order_data):

    total_disc = 0
    discounted_sub = subtotal
    for item_data in order_data:
        if item_data["item"] == "Muffin":
            if item_data["quantity"] >= 3:
                muffin_disc = 1
                item_data["Happy Hour Discount"] = muffin_disc
                total_disc += muffin_disc
                discounted_sub -= muffin_disc
                
        if item_data["item"] == "Coffee":
            if item_data["quantity"] >= 2:
                coffee_disc = item_data.get("extended cost") * .2
                item_data["Bulk Deal"] = coffee_disc
                total_disc += coffee_disc
                discounted_sub -= coffee_disc
        

    results = [subtotal, total_disc, discounted_sub, order_data]
    return results        

def calc_tax(results):

    updated_copy = results[:]
    tax = 0.05 * results[2]
    final_total = tax + results[2]
    updated_copy.insert(3, tax)
    updated_copy.insert(4, final_total)
    return updated_copy 

def print_receipt(updated_copy):
    subtotal = updated_copy[0]
    total_disc = updated_copy[1]
    discounted_sub = updated_copy[2]
    tax = updated_copy[3]
    total = updated_copy[4]
    order_data = updated_copy[5]

    receipt = {
        "gross" : subtotal,
        "net" : total,
        "items" : []
    }

    receipt_width = 100
    block_width = 20

    print("\n{:^{w}}".format("--- Receipt ---", w=receipt_width))

    for item in order_data:
        name = item["item"]
        unit_price = item["item cost"]
        qty = item["quantity"]
        line_total = item["extended cost"]
        disc_amt = 0
        disc_label = "None"
        if "Happy Hour Discount" in item:
            disc_label = "Happy Hour Discount"
            disc_amt = item["Happy Hour Discount"]
        if "Bulk Deal" in item:
            disc_label = "Bulk Deal"
            disc_amt = item["Bulk Deal"]

        item_kpi = {
            "name" : name,
            "quantity" : qty
        }

        receipt["items"].append(item_kpi)

        line = f"Item: {name:<15} - Unit Price: ${unit_price:>5.2f} - Quantity: {qty:>2} - Item Total: ${line_total:>5.2f} - Discount Applied: {disc_label:<} - Saved: ${disc_amt:>5.2f}"

        print("{:^{w}}\n".format(line, w=receipt_width))

    line_subtotal = "Subtotal: ${:.2f}".format(subtotal)
    line_discount = "Discount: -${:.2f}".format(total_disc)
    line_tax      = "Tax (5%): ${:.2f}".format(tax)
    line_total    = "Total:    ${:.2f}".format(total)

    sub_block   = "{:>{w}}".format(line_subtotal,  w=block_width)
    disc_block  = "{:>{w}}".format(line_discount,  w=block_width)
    tax_block   = "{:>{w}}".format(line_tax,       w=block_width)
    total_block = "{:>{w}}".format(line_total,     w=block_width)

    print("{:>{w}}".format(sub_block,   w=receipt_width))
    print("{:>{w}}".format(disc_block,  w=receipt_width))
    print("{:>{w}}".format(tax_block,   w=receipt_width))
    print("{:>{w}}".format(total_block, w=receipt_width))

    thanks_line = "Thanks for dining at our cafe! We hope you enjoy!"
    print("{:^{w}}\n".format(thanks_line, w=receipt_width))

    return receipt

def track_kpis(receipts_folder):

    orders = len(receipts_folder)
    net_revenue = sum(receipt["net"] for receipt in receipts_folder)
    gross_revenue = sum(receipt["gross"] for receipt in receipts_folder)
    best_seller = ""
    best_seller_counter = 0

    item_counts = {}

    for receipt in receipts_folder:
        for item in receipt["items"]:
            name = item["name"]
            qty = item["quantity"]

            if name not in item_counts:
                item_counts[name] = 0
            
            item_counts[name] += qty
    
    for k,v in item_counts.items():
        if v > best_seller_counter:
            best_seller = k
            best_seller_counter = v
    
    print("\n--- Daily Stats ---")
    print("Total Orders:", orders)
    print("Gross Revenue: ${:.2f}".format(gross_revenue))
    print("Net Revenue: ${:.2f}".format(net_revenue))
    print("Best Seller: {} ({})".format(best_seller, best_seller_counter))

def cafe_flow():
    receipts_folder = []
    
    while True:
        cart = cafe()

        subtotal, order_data = calc_subtotal(cafe_menu(), cart)

        receipts_folder.append(print_receipt(calc_tax(calc_disc(subtotal, order_data))))

        while True:
            new_order = input("New customer? (y/n):\n").strip().lower()
            if new_order not in ("y","n"):
                print("Invalid entry. Please enter 'y' or 'n'.")
                continue
            break
        if new_order == "n":
            break  
    
    track_kpis(receipts_folder)

def main():
    while True:
        open_cafe = disp_main_menu(main_menu())
        if open_cafe:
            cafe_flow()
        else:
            print("Closing application. Goodbye!")
            return

if __name__=="__main__":
    main()

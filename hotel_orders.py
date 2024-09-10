MENU = {
    "Fries masala and Sausage": 350,
    "Full chicken": 700,
    "Mukimo and Beef": 850,
    "Kienyeji fry and Ugali": 1100,
    "Samosa": 50,
    "Pilau Beef": 550,
    "Chapati quarter Chicken": 950,
    "Taco": 300,
    "Smocha": 100
    "Smoothie": 300
    "Githeri" : 80
}


def main():
    orders = []
    while True:
        try:
            order = input("Place an order (one at a time or ctrl Z to finish): ").strip().title() 
            if order in MENU:
                orders.append(order)
            else:
                print("The item you entered is not in menu!")
        except EOFError:
            print(f"Your order: {orders} ")
            break
        finally:
          total = compute_total(orders)
          print(f"Your total bill is ksh.{total}")
    
def compute_total(orders):
    total = 0
    for order in orders:
        total += MENU[order]
    return total




if __name__ == "__main__":
    main()
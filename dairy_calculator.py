def get_current_price():
    try:
        with open("price.txt","r")as f:
            return float(f.read().strip())
    except FileNotFoundError:
        return 44.0

def calculate_payment(litres, price_per_litre):
    return litres*price_per_litre

def run():
    print("Kiambu Dairy Co-op Payment Calculator")
    print("-------------------------------------")        
    print(f"Current buying price: KES {get_current_price():.2f} per litre")
    print()

    name = input("Farmer name: ").strip()
    if not name:
        print("Name is required.")
        return
    try:
        litres = float(input("Litres supplied today: "))
        if litres <= 0:
            print("litres must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number for litres.")    
        return

    price = get_current_price()
    total = calculate_payment(litres, price)

    print()
    print(f"Farmer  :{name}")
    print(f"Litres  :{litres}")
    print(f"Price   :KES {price:.2f}/litre")
    print(f"Total   :KES {total:,.2f}")

run()    
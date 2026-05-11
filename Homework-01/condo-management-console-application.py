condos = []

def setup_condo():
    floor = input("Enter floor number: ")
    room = input("Enter room number: ")
    condo = {
        "floor": floor,
        "room": room,
        "status": "Available",
        "owner": None,
        "price": float(input("Enter condo price: "))
    }
    condos.append(condo)
    print("Condo added successfully!")

def show_condos():
    if not condos:
        print("No condos found.")
        return
    print("\n--- Condo List ---")
    for i, condo in enumerate(condos, start=1):
        print(
            f"{i}. Floor: {condo['floor']} | "
            f"Room: {condo['room']} | "
            f"Price: ${condo['price']} | "
            f"Status: {condo['status']} | "
            f"Owner: {condo['owner']}"
        )

def buy_condo():
    show_condos()
    room = input("Enter room number to buy: ")
    for condo in condos:
        if condo["room"] == room:
            if condo["status"] == "Sold":
                print("This condo is already sold.")
                return
            owner = input("Enter owner name: ")
            condo["owner"] = owner
            condo["status"] = "Sold"
            print("Condo bought successfully!")
            return
    print("Condo not found.")

def sell_condo():
    room = input("Enter room number to sell: ")
    for condo in condos:
        if condo["room"] == room:
            if condo["status"] == "Available":
                print("This condo is already available.")
                return
            condo["owner"] = None
            condo["status"] = "Available"
            print("Condo sold/cleared successfully!")
            return
    print("Condo not found.")


def search_owner():
    owner = input("Enter owner name to search: ")
    found = False
    for condo in condos:
        if condo["owner"] and condo["owner"].lower() == owner.lower():
            print(
                f"Floor: {condo['floor']} | "
                f"Room: {condo['room']} | "
                f"Price: ${condo['price']} | "
                f"Status: {condo['status']}"
            )
            found = True
    if not found:
        print("Owner not found.")

def main():
    while True:
        print("\n===== Condo Management System =====")
        print("1. Setup Condo")
        print("2. Show Condos")
        print("3. Buy Condo")
        print("4. Sell Condo")
        print("5. Search Condo Owner")
        print("6. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            setup_condo()
        elif choice == "2":
            show_condos()
        elif choice == "3":
            buy_condo()
        elif choice == "4":
            sell_condo()
        elif choice == "5":
            search_owner()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
main()
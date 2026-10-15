import csv
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to continue...")

def print_header(title):
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50 + "\n")

def file_check():
    if not os.path.exists("products.csv"):
        with open("products.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Product ID", "Name", "Price", "Stock"])

def add_product():
    print_header("ADD PRODUCT")
    file_check()
    with open("products.csv", "a", newline='') as f:
        writer = csv.writer(f)
        pid = input("Enter Product ID: ").strip()
        name = input("Enter Product Name: ").strip()
        price = input("Enter Price: ").strip()
        stock = input("Enter Stock Quantity: ").strip()
        if not pid or not name or not price or not stock:
            print("Error: All fields are required.")
            return
        writer.writerow([pid, name, price, stock])
        print("Product added successfully.")

def view_products():
    print_header("VIEW PRODUCTS")
    file_check()
    with open("products.csv", "r") as f:
        reader = csv.reader(f)
        data = list(reader)
        if len(data) <= 1:
            print("No products available.")
            return
        for i, row in enumerate(data):
            if i == 0:
                print(f"{' | '.join(row)}")
                print("-" * 50)
            else:
                print(f"{' | '.join(row)}")

def search_product():
    print_header("SEARCH PRODUCT")
    file_check()
    name = input("Enter product name to search: ").lower()
    found = False
    with open("products.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 1 and row[1].lower() == name:
                print("Product Found:")
                print(f"ID: {row[0]} | Name: {row[1]} | Price: {row[2]} | Stock: {row[3]}")
                found = True
                break
    if not found:
        print("Product not found.")

def buy_product():
    print_header("BUY PRODUCT")
    file_check()
    pid = input("Enter Product ID to buy: ").strip()
    try:
        qty = int(input("Enter Quantity: "))
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        return
    rows = []
    bought = False
    with open("products.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0 and row[0] == pid:
                if row[0].lower() != "product id":
                    if int(row[3]) >= qty:
                        row[3] = str(int(row[3]) - qty)
                        print(f"Purchase successful. Amount: {int(row[2]) * qty}")
                        bought = True
                    else:
                        print("Not enough stock.")
                        bought = True
            rows.append(row)
    if not bought:
        print("Product not found.")
    else:
        with open("products.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

def main_menu():
    while True:
        print("\n1. Add Product\n2. View Products\n3. Search Product\n4. Buy Product\n5. Exit")
        ch = input("Enter choice: ")
        if ch == '1':
            add_product()
        elif ch == '2':
            view_products()
        elif ch == '3':
            search_product()
        elif ch == '4':
            buy_product()
        elif ch == '5':
            print("Exiting program...")
            time.sleep(1)
            break
        else:
            print("Invalid choice.")

file_check()
main_menu()

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item = input("Enter the name of the item to be added: ")
            shopping_list.append(add_item)
            print("Item added:", add_item)
        elif choice == '2':
            remove_item = input("Enter the name of the item to be removed: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print("Item removed:", remove_item)
            else:
                print("Item not found in the shopping list.")
        elif choice == '3':
            print("Shopping List:")
            i=1
            for items in shopping_list:
                print(f"{i}, {items}")
                i+=1
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()











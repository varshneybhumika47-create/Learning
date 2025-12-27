queue = []
token = 1

while True:
    print("\n!! Token Queue System !!")
    print("1. Add Customer")
    print("2. Serve Customer")
    print("3. Show Waiting Customers")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        queue.append(token)
        print("Costumer Added with Token Numbers:", token)
        token += 1

    elif choice == 2:
        if len(queue) == 0:
            print("No customer to serve")
        else:
            served = queue.pop(0)
            print("Serving customer with Token Number:",{served})

    elif choice == 3:
        print("Waiting customers:", {len(queue)})
        print("Queue:", queue)

    elif choice == 4:
        print("Thank You! Program Ended.")
        break

    else:
        print("Invalid choice")

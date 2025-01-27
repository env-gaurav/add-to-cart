basket=[]
shopping_mall='''
1. Apple    2. Banana   
3. Litchi   4. Grapes
5. Exit
'''
print(shopping_mall)
while True:
    choice= input("Enter your choice: ")
    if choice== "5":
        print("Exiting the program")
        break
    elif choice == "1":
        basket.append("Apple")
        print("Apple added to cart")
    elif choice == "2":
        basket.append("Banana")
        print("Banana added to cart")
    elif choice == "3":
        basket.append("Litchi")
        print("Litchi added to cart")
    elif choice == "4":
        basket.append("Grapes")
        print("Grapes added to cart")
    else:
        print("provide correct input")

print(basket)
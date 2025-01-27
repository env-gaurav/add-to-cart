basket=[]
quantity=[]
amount=[]
total= 0.0
shopping_mall='''
1. Apple        10   
2. Banana       20   
3. Litchi       30   
4. Grapes       40
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
        qty=int(input("Enter quantity: "))
        quantity.append(qty)
        sub_total = qty*10
        amount.append(sub_total)
        total += sub_total
        print(f"{qty} Apple added to cart")
    elif choice == "2":
        basket.append("Banana")
        qty=int(input("Enter quantity: "))
        quantity.append(qty)
        sub_total = qty*20
        amount.append(sub_total)
        total += sub_total
        print(f"{qty} Banana added to cart")
    elif choice == "3":
        basket.append("Litchi")
        qty=int(input("Enter quantity: "))
        quantity.append(qty)
        sub_total = qty*30
        amount.append(sub_total)
        total += sub_total
        print(f"{qty} Litchi added to cart")
    elif choice == "4":
        basket.append("Grapes")
        qty=int(input("Enter quantity: "))
        quantity.append(qty)
        sub_total = qty*40
        amount.append(sub_total)
        total += sub_total
        print(f"{qty} Grapes added to cart")
    else:
        print("provide correct input")

print(basket)
print(quantity)
print(amount)
print( "Grand Total: " , total)
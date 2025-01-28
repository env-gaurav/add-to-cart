basket = []
quantity = []
sub_total = []
gt = 0.0
cafe=f'''
{"*"*25}
        RAMESHWARAM CAFE
{"*"*25}

1. MASALA DOSA      100
2. GHEE IDLI        50
3. PLAIN IDLI       20
4. EXIT

'''
print(cafe)
while True:
    choice=int(input("ENTER YOUR CHOICE: "))
    if choice == 1:
        basket.append("MASALA DOSA")
        qty = int(input("ENTER QUANTITY: "))
        quantity.append(qty)
        sub_total.append(qty*100)
        gt = gt + (qty*100)
        
        print(f"{qty} MASALA DOSA ADDED TO CART")
    elif choice == 2:
        basket.append("GHEE IDLI")
        qty = int(input("ENTER QUANTITY: "))
        quantity.append(qty)
        sub_total.append(qty*50)
        gt = gt + (qty*50)
        print(f"{qty} GHEE IDLI ADDED TO CART")
    elif choice == 3:
        basket.append("PLAIN IDLI")
        qty = int(input("ENTER QUANTITY: "))
        quantity.append(qty)
        sub_total.append(qty*20)
        gt = gt + (qty*20)
        print(f"{qty} PLAIN IDLI ADDED TO CART")
    elif choice == 4:
        print("EXITING THE PROGRAM")
        break
    else:
        print("PLEASE PROVIDE CORRECT INPUT")
        
print(basket)        
print(quantity)
print(sub_total)
print("GRAND TOTAL", gt)
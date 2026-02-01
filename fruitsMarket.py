##list = [23,56,78,21,24,67,87,98,0]
##list.append('swamy')
##list.remove(78)
##print(list[1:7])
##list[3] =2942702727
##list.extend([4,7,89,67,89])
##list.pop()
##del list[0]
##list.clear()
##print(list)
##names= ["ramu","ista","ravi","swamy"]
##for name in names:
##        print(name)
fruits = ['apple','banana','grapes','water melon']
fruits.append('orange')
attempts = 3
while attempts>0:
    name = input("enter a name:")
    psd = input("enter a password:")
    if name == "swamy" and psd == "123":
            print("login successfull ")
            print("which fruit price you want per kg")
            print("1.apple: \n2.banana: \n3.grapes: \n4.water melon: \n5.orange: \n6Exit: ")
            def calculate_price(price, quantity):
                return price * quantity
choice = int(input("Enter choice: "))
n = int(input("Enter quantity (kg): "))

if choice == 1:
    print("Apple price is 150 per kg")
    total = calculate_price(150, n)

elif choice == 2:
    print("Banana price is 90 per kg")
    total = calculate_price(90, n)

elif choice == 3:
    print("Grapes price is 100 per kg")
    total = calculate_price(100, n)

elif choice == 4:
    print("Watermelon price is 80 per kg")
    total = calculate_price(80, n)

elif choice == 5:
    print("Orange price is 60 per kg")
    total = calculate_price(60, n)

else:
    print("Fruit not available")
    exit()

print("Total price:", total)
else:
        attempts -= 1
        if attempts == 0:
               print("you attempt multiple times so your account is blocked \nplease try again later")
               else:
               print("wrong name or password please try again",attempts,"attempts are there")
        
    

    
        

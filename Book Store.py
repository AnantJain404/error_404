totalp = 0

def samaan():
    print("\n\t\t\t\tBooks ka Bhandar")
    print("1.Mathematics\n2.Science\n3.Hindi\n4.English\n5.Social Studies")
    a = int(input("\nEnter your choice : "))

    if a==1:
        print("Name : Mathematics\nPrice : Rs.100")
        b = int(input("Quantity : "))
        price = (b*100)
        print(f"\nThe price is {price}")
        global totalp
        totalp = totalp+price
        c = input("Do you want any other book(y for yes,n for no): ")
        if c=='y':
            samaan()
        elif c=='n':
            print(f"\nYour total bill is {totalp}")
            exit()
        else:
            exit()
    elif a==2:
        print("Name : Science\nPrice : Rs.120")
        b = int(input("Quantity : "))
        price = (b*120)
        print(f"\nThe price is {price}")
        totalp = totalp+price
        c = input("Do you want any other book(y for yes,n for no): ")
        if c=='y':
            samaan()
        elif c=='n':
            print(f"\nYour total bill is {totalp}")
            exit()
        else:
            exit()
    elif a==3:
        print("Name : Hindi\nPrice : Rs.75")
        b = int(input("Quantity : "))
        price = (b*75)
        print(f"\nThe price is {price}")
        totalp = totalp+price
        c = input("Do you want any other book(y for yes,n for no): ")
        if c=='y':
            samaan()
        elif c=='n':
            print(f"\nYour total bill is {totalp}")
            exit()
        else:
            exit()
    elif a==4:
        print("Name : English\nPrice : Rs.80")
        b = int(input("Quantity : "))
        price = (b*80)
        print(f"\nThe price is {price}")
        totalp = totalp+price
        c = input("Do you want any other book(y for yes,n for no): ")
        if c=='y':
            samaan()
        elif c=='n':
            print(f"\nYour total bill is {totalp}")
            exit()
        else:
            exit()
    elif a==5:
        print("Name : Social Science\nPrice : Rs.100")
        b = int(input("Quantity : "))
        price = (b*100)
        print(f"\nThe price is {price}")
        totalp = totalp+price
        c = input("Do you want any other book(y for yes,n for no): ")
        if c=='y':
            samaan()
        elif c=='n':
            print(f"\nYour total bill is {totalp}")
            exit()
        else:
            exit()
    else:
        print("Invalid Choice")
   

if __name__ == "__main__":
    samaan()
    

    

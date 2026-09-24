# Project-for-Python-essential-course
#Inventory management system by achyutam sharma 26bce10159
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print()
print("INVENTORY MANAGEMENT SYSTEM")
print()
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print()
i=0
E = {}
print("1. Add new product")
print("2. View all products")
print("3. Search a product")
print("4. Update product")
print("5. Sell a product")
print("6. Delete a product")
print("7. Exit")
print()
X = int(input("enter your choice:"))
print()
while(X<8):
  if(X==1):
    print("Adding new product")
    print()
    A = input("enter product's name:")
    B = int(input("enter product's quantity:"))
    C = int(input("enter product's price:"))
    D = {"name":A, "quantity":B, "price":C}
    E[i]=D
    i=i+1
    print()
    X = int(input("enter your choice:"))
    print()
  if(X==2):
    print("Viewing all products")
    print()
    for j in range(0, len(E)):
      print(E[j])
      print()
    X = int(input("enter your choice:"))
    print()

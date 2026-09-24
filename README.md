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
  if(X==3):
    print("searching a product")
    print()
    N = int(input("enter index:"))
    if N<len(E):
      print(E[N])
    else:
      print("No product on this index")
    print()
    X = int(input("enter your choice:"))
    print()
  if(X==4):
    print("updating the product")
    print()
    a = int(input("enter index of product:"))
    print("what do you want to update?")
    print("1.Name, 2.Quantity, 3.price")
    b = int(input("enter your choice"))
    t = E[a]
    if(b==1):
      x = input("enter new name:")
      t["name"] = x
    if(b==2):
      x = int(input("enter new quantity:"))
      t["quantity"] = x
    if(b==3):
      x = input("enter new price:")
      t["price"] = x
    print("change is updated!")
    print()
    X = int(input("enter your choice:"))
    print()
  if(X==5):
    print("selling the product")
    print()
    print("which product do you want to sell?")
    a = int(input("enter index of product:"))
    t = E[a]
    t["quantity"] = t["quantity"] - 1
    print("product is sold")
    print()
    X = int(input("enter your choice:"))
    print()
  if(X==6):
    print("deleting a product")
    print()
    print("which product do you want to delete?")
    a = int(input("enter index of product:"))
    E.pop(a)
    print("product is deleted")
    print()
    X = int(input("enter your choice:"))
    print()

def update():
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

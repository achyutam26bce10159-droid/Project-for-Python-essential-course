def delete():
  print("which product do you want to delete?")
  a = int(input("enter index of product:"))
  E.pop(a)
  print("product is deleted")
  print()

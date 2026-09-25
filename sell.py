def selling():
  print("which product do you want to sell?")
  a = int(input("enter index of product:"))
  t = E[a]
  t["quantity"] = t["quantity"] - 1
  print("product is sold")
  print()

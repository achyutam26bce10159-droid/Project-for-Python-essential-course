def viewing():
  for j in range(0, len(E)):
    print(E[j])
    print()

def searching():
  N = int(input("enter index:"))
  if N<len(E):
    print(E[N])
  else:
    print("No product on this index")
  print()

def currency_converter(rate,euros):
  dollars=euros*rate
  return dollars
  print(dollars)

r=input("enter rate: ")
e=input("enter euros:")
print(currency_converter(float(r),float(e)))

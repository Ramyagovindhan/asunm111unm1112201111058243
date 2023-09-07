def islepyer(y):
 if(year%4==0):
  return True 
 else: 
  return False
year=int(input("enter tha year:"))
print("leap year",islepyer(year))
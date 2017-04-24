def cel_to_Far(CTemp):
    FTemp = CTemp * 9/5 + 32
    return FTemp

#CInpTemp = int(input("Enter a Celsius Temp: "))

TempList = [10,-20,-289, 100]
with open('c2f.txt','a+') as file:
    for temp in TempList:
        if temp < -273.15:
            print("your temperature is way too low")
        else:
            file.write(str(cel_to_Far(temp))+'\n')

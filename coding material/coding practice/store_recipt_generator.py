sum=0
list_1item=[]
item_values=[]
values=0
while True:
    item=input("Enter the item or q for quit  ")
    if item=='q':
        for i in range(len(item_values)):
            print(f"{i+1}. {list_1item[i]} = {item_values[i]}")
        print("Your total bill is",sum,"Thankes for shopping ") 
        break   
    values=int(input("Enter the item values: "))
    list_1item.append(item)
    item_values.append(values)
    sum+=values


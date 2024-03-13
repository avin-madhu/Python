# Prompt the user for a list of integers for all values > 100 store "Over"

lst = []
while(True):
    num = int(input("Enter the number: "))
    if num>100:
        lst.append("Over")
    else:
        lst.append(num)
    if input("Do you want to continue? (y/n): ") == 'n':
        break
print(lst)
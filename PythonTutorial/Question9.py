fileName = input("Enter the File Name: ")
for i in range(len(fileName)-1,0,-1 ):
    if fileName[i] == '.':
        print(fileName[i+1:])
        break

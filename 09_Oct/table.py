# Printing tables of ODD Numbers From 1 to 10-

for table in range(1,11,2):     # Getting Odd Nos from 1 to 10
    print("Table of ",table)
    for i in range(1,11):       # Printing the table
        print(table,"*",i,"=",i*table)
    print()
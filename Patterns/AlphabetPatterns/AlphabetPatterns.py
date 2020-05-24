# Patterns for every letter of the alphabet
print_A = [ [" " for i in range(6)] for j in range(6) ]

# Defining the patterns for the letters
for raw in range(6):
    for col in range(6):
        if ((col == 0 or col == 5) and (raw!=0 )) or (raw==0 and (col!=0 and col!=5)) or (raw==3 and (col!=0 and col!=5)):
            print_A[raw][col] = "A"
            

# Printing the patterns
for i in range(6):
    
    for j in range(6):
        print(print_A[i] [j], end = "")
        
    print()
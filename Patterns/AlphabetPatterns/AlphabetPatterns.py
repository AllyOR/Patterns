# Patterns for every letter of the alphabet
print_A = [ [" " for i in range(6)] for j in range(6) ]
print_B = [ [" " for i in range(6)] for j in range(6) ]
print_C = [ [" " for i in range(6)] for j in range(6) ]
print_D = [ [" " for i in range(6)] for j in range(6) ]
print_E = [ [" " for i in range(6)] for j in range(6) ]

# Defining the patterns for the letters
for raw in range(6):
    for col in range(6):
        if ((col == 0 or col == 5) and (raw!=0 )) or (raw==0 and (col!=0 and col!=5)) or (raw==3 and (col!=0 and col!=5)):
            print_A[raw][col] = "A"

for raw in range(6):
    for col in range(6):
        if col == 0 or ((raw==0 or raw==5)and (col!=0 and col!=5)) or (raw==3 and col<5) or (col==5 and (raw==1 or raw==2 or raw==4)):
            print_B[raw][col] = "B"

for raw in range(6):
    for col in range(6):
        if ((raw !=0 and raw!=5) and col==0) or ((raw==0 or raw ==5) and col!=0):
            print_C[raw][col] = "C"

for raw in range(6):
    for col in range(6):
        if col == 0 or ((raw==0 or raw==5)and (col!=0 and col!=5)) or (col==5 and (raw!=0 and raw!=5)):
            print_D[raw][col] = "D"

for raw in range(6):
    for col in range(6):
        if col == 0 or ((raw==0 or raw==5)and (col!=0 and col!=5)) or (raw==3 and col<4):
            print_E[raw][col] = "E"
            

# Printing the patterns
for i in range(6):
    
    for j in range(6):
        print(print_A[i] [j], end = "")
    print(end="  ")
    
    for j in range(6):
        print(print_B[i] [j], end = "")
    print(end="  ")
    
    for j in range(6):
        print(print_C[i] [j], end = "")
    print(end="  ")
    
    for j in range(6):
        print(print_D[i] [j], end = "")
    print(end="  ")
    
    for j in range(6):
        print(print_E[i] [j], end = "")
        
    print()
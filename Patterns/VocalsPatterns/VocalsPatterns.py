# string "NO"
print_N = [ [" " for i in range(6)] for j in range(6) ]
print_O = [ [" " for i in range(6)] for j in range(6) ]
print_A = [ [" " for i in range(6)] for j in range(6) ]
print_U = [ [" " for i in range(6)] for j in range(6) ]
print_C = [ [" " for i in range(6)] for j in range(6) ]
print_B = [ [" " for i in range(6)] for j in range(6) ]
print_E = [ [" " for i in range(6)] for j in range(6) ]
print_I = [ [" " for i in range(6)] for j in range(6) ]

for raw in range(6):
    for col in range(6):
        if ((col == 0 or col == 5) and (raw!=0 )) or (raw==0 and (col!=0 and col!=5)) or (raw==3 and (col!=0 and col!=5)):
            print_A[raw][col] = "A"
            
for raw in range(6):
    for col in range(6):
        if col == 0 or ((raw==0 or raw==5)and (col!=0 and col!=5)) or (raw==3 and col<4):
            print_E[raw][col] = "E"

for raw in range(6):
    for col in range(6):
        if col == 3 or ((raw==0 or raw==5)and col!=0):
            print_I[raw][col] = "I"

    
for raw in range(6):
    for col in range(6):
        if ( (raw==0 or raw==5) and (col!=0 and col!=5) ) or ( (col==0 or col==5) and (raw!=0 and raw!=5) ):
            print_O[raw][col] = "0"

for raw in range(6):
    for col in range(6):
        if ( (raw==5) and (col!=0 and col!=5) ) or ( (col==0 or col==5) and (raw!=5) ):
            print_U[raw][col] = "U"
            
for i in range(6):
    for j in range(6):
        print(print_A[i] [j], end = "")
    print(end="  ")

    for j in range(6):
        print(print_E[i] [j], end = "")
    print(end="  ")
    
    for j in range(6):
        print(print_I[i] [j], end = "")
    print(end="  ")
    
    for j in range(6):
        print(print_O[i] [j], end = "")
    print(end="  ")
    
    for j in range(6):
        print(print_U[i] [j], end="")
    print()

# Patterns for every letter of the alphabet
print_A = [ [" " for i in range(6)] for j in range(6) ]
print_B = [ [" " for i in range(6)] for j in range(6) ]
print_C = [ [" " for i in range(6)] for j in range(6) ]
print_D = [ [" " for i in range(6)] for j in range(6) ]
print_E = [ [" " for i in range(6)] for j in range(6) ]
print_F = [ [" " for i in range(6)] for j in range(6) ]
print_G = [ [" " for i in range(6)] for j in range(6) ]
print_H = [ [" " for i in range(6)] for j in range(6) ]
print_I = [ [" " for i in range(6)] for j in range(6) ]
print_J = [ [" " for i in range(6)] for j in range(6) ]
print_K = [ [" " for i in range(6)] for j in range(6) ]
print_L = [ [" " for i in range(6)] for j in range(6) ]
print_M = [ [" " for i in range(6)] for j in range(6) ]
print_N = [ [" " for i in range(6)] for j in range(6) ]
print_O = [ [" " for i in range(6)] for j in range(6) ]
print_P = [ [" " for i in range(6)] for j in range(6) ]
print_Q = [ [" " for i in range(6)] for j in range(6) ]
print_R = [ [" " for i in range(6)] for j in range(6) ]
print_S = [ [" " for i in range(6)] for j in range(6) ]
print_T = [ [" " for i in range(6)] for j in range(6) ]
print_U = [ [" " for i in range(6)] for j in range(6) ]
print_V = [ [" " for i in range(6)] for j in range(6) ]
print_W = [ [" " for i in range(6)] for j in range(6) ]
print_X = [ [" " for i in range(6)] for j in range(6) ]
print_Y = [ [" " for i in range(6)] for j in range(6) ]
print_Z = [ [" " for i in range(6)] for j in range(6) ]

# Defining the patterns for the letters
for raw in range(6):
    for col in range(6):
        if ((col==0 or col==5) and (raw!=0)) or (raw==0 and (col!=0 and col!=5)) or (raw==3 and (col!=0 and col!=5)):
            print_A[raw][col] = "A"

for raw in range(6):
    for col in range(6):
        if col==0 or ((raw==0 or raw==5)and (col!=0 and col!=5)) or (raw==3 and col<5) or (col==5 and (raw==1 or raw==2 or raw==4)):
            print_B[raw][col] = "B"

for raw in range(6):
    for col in range(6):
        if ((raw!=0 and raw!=5) and col==0) or ((raw==0 or raw==5) and col!=0):
            print_C[raw][col] = "C"

for raw in range(6):
    for col in range(6):
        if col == 0 or ((raw==0 or raw==5)and (col!=0 and col!=5)) or (col==5 and (raw!=0 and raw!=5)):
            print_D[raw][col] = "D"

for raw in range(6):
    for col in range(6):
        if col==0 or ((raw==0 or raw==5)and (col!=0 and col!=5)) or (raw==3 and col<4):
            print_E[raw][col] = "E"
            
for raw in range(6):
    for col in range(6):
        if col==0 or (raw==0 and (col!=0 and col!=5)) or (raw==3 and (col!=0 and col!=5)):
            print_F[raw][col] = "F"

for raw in range(6):
    for col in range(6):
        if ((raw!=0 and raw!=5) and col==0) or (raw==4 and col==5) or ((raw==0 or raw==5) and col!=0) or (raw==3 and col>2):
            print_G[raw][col] = "G"
            
for raw in range(6):
    for col in range(6):
        if (col==0 or col==5) or (raw==3 and (col!=0 and col!=5)):
            print_H[raw][col] = "H"

for raw in range(6):
    for col in range(6):
        if col == 3 or ((raw==0 or raw==5)and col!=0):
            print_I[raw][col] = "I"

for raw in range(6):
    for col in range(6):
        if col==4 or raw==0 or (raw==5 and col<4) or (col==0 and (raw>2 and raw<5)):
            print_J[raw][col] = "J"

for raw in range(6):
    for col in range(6):
        if col==0 or (raw==3 and col<4) or (col==4 and (raw==2 or raw==4)) or (col==5 and (raw<2 or raw==5)):
            print_K[raw][col] = "K"
            
for raw in range(6):
    for col in range(6):
        if raw==5 or (col==0 and raw!=5):
            print_L[raw][col] = "L"
            
for raw in range(6):
    for col in range(6):
        if (col==0 or col==5) or (raw==3 and (col==2 or col==3)) or (raw==2 and (col==1 or col==4)):
            print_M[raw][col] = "M"
            
for raw in range(6):
    for col in range(6):
        if col == 0 or col == 5 or raw == col:
            print_N[raw][col] = "N"
            
for raw in range(6):
    for col in range(6):
        if ( (raw==0 or raw==5) and (col!=0 and col!=5) ) or ( (col==0 or col==5) and (raw!=0 and raw!=5) ):
            print_O[raw][col] = "0"

for raw in range(6):
    for col in range(6):
        if col==0 or (raw==0 and (col!=0 and col!=5)) or (raw==3 and (col!=0 and col!=5)) or (col==5 and (raw>0 and raw<3)):
            print_P[raw][col] = "P"

for raw in range(6):
    for col in range(6):
        if (raw==0 and (col!=0 and col!=5)) or (raw==5 and (col>0 and col<4)) or (col==0 and (raw!=0 and raw!=5)) or (col==5 and raw!=0) or (col==3 and raw==3) or (col==4 and raw==4):
            print_Q[raw][col] = "Q"

for raw in range(6):
    for col in range(6):
        if col==0 or (raw==3 and col<4) or (col==4 and (raw==2 or raw==4)) or (col==5 and (raw==1 or raw==5)) or (raw==0 and col!=5):
            print_R[raw][col] = "R"

for raw in range(6):
    for col in range(6):
        if ((raw==1 or raw ==2) and col==0) or ((raw==4) and col==5) or (raw==0  and col!=0) or (raw==3 and (col!=0 and col!=5)) or (raw==5 and col!=5):
            print_S[raw][col] = "S"

for raw in range(6):
    for col in range(6):
        if col == 3 or (raw==0 and col!=0):
            print_T[raw][col] = "T"

for raw in range(6):
    for col in range(6):
        if ( (raw==5) and (col!=0 and col!=5) ) or ( (col==0 or col==5) and (raw!=5) ):
            print_U[raw][col] = "U"

for raw in range(6):
    for col in range(6):
        if ( (raw==5) and (col>1 and col<4) ) or ( (raw==4) and (col==1 or col==4) ) or ( (col==0 or col==5) and (raw<4) ):
            print_V[raw][col] = "V"

for raw in range(6):
    for col in range(6):
        if (col==0 or col==5) or (raw==3 and (col==2 or col==3)) or (raw==4 and (col==1 or col==4)):
            print_W[raw][col] = "W"

for raw in range(6):
    for col in range(6):
        if (col==0 and raw==5) or (col==raw) or (col==5 and raw==0) or (col==1 and raw==4) or (col==4 and raw==1) or (col==2 and raw==3) or (col==3 and raw==2):
            print_X[raw][col] = "X"

for raw in range(6):
    for col in range(6):
        if ((raw < 2 and col ==0) or (raw!=5 and col == 5)) or (raw==5 and (col!=0 and col!=5)) or (raw==2 and (col!=0 and col!=5)):
            print_Y[raw][col] = "Y"

for raw in range(6):
    for col in range(6):
        if (raw==0 or raw==5) or (col==1 and raw==4) or (col==4 and raw==1) or (col==2 and raw==3) or (col==3 and raw==2):
            print_Z[raw][col] = "Z"
            

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
    print(end="  ")
    
    for j in range(6):
        print(print_F[i] [j], end = "")
    print(end="  ")
    
    for j in range(6):
        print(print_G[i] [j], end = "")
    print(end="  ")

    for j in range(6):
        print(print_H[i] [j], end = "")
    print(end="  ")

    for j in range(6):
        print(print_I[i] [j], end = "")
    print(end="  ")
    
    for j in range(6):
        print(print_J[i] [j], end = "")
    print(end="  ")
    
    for j in range(6):
        print(print_K[i] [j], end = "")
    print(end="  ")
    
    for j in range(6):
        print(print_L[i] [j], end = "")
    print(end="  ")
    
    for j in range(6):
        print(print_M[i] [j], end = "")
    print(end="  ")
    
    for j in range(6):
        print(print_N[i] [j], end = "")
    print(end="  ")

    for j in range(6):
        print(print_O[i] [j], end = "")
    print(end="  ")

    for j in range(6):
        print(print_P[i] [j], end = "")
    print(end="  ")
    
    for j in range(6):
        print(print_Q[i] [j], end = "")
        
    print()
print("\n")
for i in range(6):
    
    for j in range(6):
        print(print_R[i] [j], end = "")
    print(end="  ")

    for j in range(6):
        print(print_S[i] [j], end = "")
    print(end="  ")

    for j in range(6):
        print(print_T[i] [j], end = "")
    print(end="  ")

    for j in range(6):
        print(print_U[i] [j], end = "")
    print(end="  ")

    for j in range(6):
        print(print_V[i] [j], end = "")
    print(end="  ")

    for j in range(6):
        print(print_W[i] [j], end = "")
    print(end="  ")

    for j in range(6):
        print(print_X[i] [j], end = "")
    print(end="  ")

    for j in range(6):
        print(print_Y[i] [j], end = "")
    print(end="  ")

    for j in range(6):
        print(print_Z[i] [j], end = "")
        
    print()

# Patterns of numbers

print_0 = [ [" " for i in range(6)] for j in range(6) ]
print_1 = [ [" " for i in range(6)] for j in range(6) ]
print_2 = [ [" " for i in range(6)] for j in range(6) ]
print_3 = [ [" " for i in range(6)] for j in range(6) ]
print_4 = [ [" " for i in range(6)] for j in range(6) ]
print_5 = [ [" " for i in range(6)] for j in range(6) ]

for raw in range(6):
    for col in range(6):
        if ( (raw==0 or raw==5) and (col!=0 and col!=5) ) or ( (col==0 or col==5) and (raw!=0 and raw!=5) ):
            print_0[raw][col] = "0"

for raw in range(6):
    for col in range(6):
        if col == 3 or (raw==5 and (col!=0 and col!=5)) or (raw==2 and col==0) or (raw==1 and col==1) or (raw==0 and col==2):
            print_1[raw][col] = "1"

for raw in range(6):
    for col in range(6):
        if ((raw==0 or raw==5)and col!=5) or (col==1 and raw==4) or (col==4 and raw==1) or (col==2 and raw==3) or (col==3 and raw==2) or(col==0 and raw==1):
            print_2[raw][col] = "2"

for raw in range(6):
    for col in range(6):
        if (col==5 and (raw!=2 and raw!=5)) or ((raw==0 or raw==5) and (col!=0 and col!=5)) or (raw==2 and (col>1 and col!=5)):
            print_3[raw][col] = "3"

for raw in range(6):
    for col in range(6):
        if col == 4 or (raw==2 and (col!=0 and col!=5)) or (col==0 and raw<3):
            print_4[raw][col] = "4"

for raw in range(6):
    for col in range(6):
        if ((raw<3) and col==0) or ((raw==3 or raw==4) and col==5) or (raw==0  and col!=0) or (raw==2 and (col!=0 and col!=5)) or (raw==5 and col!=5):
            print_5[raw][col] = "5"


for i in range(6):

    for j in range(6):
        print(print_0[i] [j], end = "")
    print(end="  ")

    for j in range(6):
        print(print_1[i] [j], end = "")
    print(end="  ")

    for j in range(6):
        print(print_2[i] [j], end = "")
    print(end="  ")

    for j in range(6):
        print(print_3[i] [j], end = "")
    print(end="  ")

    for j in range(6):
        print(print_4[i] [j], end = "")
    print(end="  ")
    
    for j in range(6):
        print(print_5[i] [j], end="")
    print()

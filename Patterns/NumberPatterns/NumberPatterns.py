# Patterns of numbers

print_0 = [ [" " for i in range(6)] for j in range(6) ]
print_1 = [ [" " for i in range(6)] for j in range(6) ]

for raw in range(6):
    for col in range(6):
        if ( (raw==0 or raw==5) and (col!=0 and col!=5) ) or ( (col==0 or col==5) and (raw!=0 and raw!=5) ):
            print_0[raw][col] = "0"


for i in range(6):
    for j in range(6):
        print(print_0[i] [j], end="")
    print()

import sys


def forward_substitution(l,b,n):
    x = [None] * n
    for j in range(n):
        if l[j][j] == 0:
            print("It's a singular matrix you entered", file=sys.stderr)
            break

        
        x[j] = b[j]/l[j][j]
        for i in range(j+1, n):
            b[i] = b[i] - ( l[i][j] * x[j] )

        #end of second for

    #end of first for


    return x


n = int(input("Enter the dimension of your matrix:\n"))
print(f"you are testing the forward-substitution for a {n} * {n} matrix ")
l = []

for i in range(n):
    print(f"Enter Row:{i+1}'s elements, separate by comma(,):")
    row = list(map(int,input().split(",")))
    l.append(row)

print("You entered: \n")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in l]))

print(f"Enter your b value, there is going to be {n} of them, separated by comma(,): \n")
b = list(map(int,input().split(",")))

x = forward_substitution(l,b,n)

print("Here are the Xs processed by the forward_substitution algorithm: \n")

for i in range(len(x)):
    print(f"x[{i}] = {x[i]} ")


import sys


def backward_substitution(u,b,n):
    x = [None] * n
    for j in reversed(range(n)):
        if u[j][j] == 0:
            print("It's a singular matrix you entered", file=sys.stderr)
            break

        
        x[j] = b[j]/u[j][j]
        for i in range(0,j):
            b[i] = b[i] - ( u[i][j] * x[j] )

        #end of second for

    #end of first for


    return x


n = int(input("Enter the dimension of your matrix:\n"))
print(f"you are testing the backward-substitution for a {n} * {n} matrix ")
u = []

for i in range(n):
    print(f"Enter Row:{i+1}'s elements, separate by comma(,):")
    row = list(map(int,input().split(",")))
    u.append(row)

print("You entered: \n")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in u]))

print(f"Enter your b value, there is going to be {n} of them, separated by comma(,): \n")
b = list(map(int,input().split(",")))

x = backward_substitution(u,b,n)

print("Here are the Xs processed by the backward_substitution algorithm: \n")

for i in range(len(x)):
    print(f"x[{i}] = {x[i]} ")

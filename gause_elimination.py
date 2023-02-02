from forward import forward_substitution
from backward import backward_substitution
import sys


def gaussian_elimination(a,b,n):
    m = [None] * n
    l = [None] * n
    u = [None] * n
    for k in range(0,n-1):
        if a[k][k] == 0:
            print("It's a singular matrix you entered", file=sys.stderr)
            break

        for i in range(k+1,n):
            m[i][k] = a[i][k]/a[k][k]
            #Lik = Mik
            l[i][k] = m[i][k]
        
        for j in range(k+1,n):
            for i in range(k+1,n):
                a[i][j] = a[i][j] = ( m[i][k]* a[k][j])
        
    
    u = a

    print("The original matrix M you entered is: \n")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in m]))
    print("After Gaussian Elimination,the subdiagonal entries of L are:")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in l]))
    print("After Gaussian Elimination,the superdiagonal entries of U are:")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in u]))


n = int(input("Enter the dimension of your matrix:\n"))
print(f"you are testing the Gaussian Elimination for a {n} * {n} matrix ")
a = []

for i in range(n):
    print(f"Enter Row:{i+1}'s elements, separate by comma(,):")
    row = list(map(int,input().split(",")))
    a.append(row)

print("You entered: \n")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in a]))

print(f"Enter your b value, there is going to be {n} of them, separated by comma(,): \n")
b = list(map(int,input().split(",")))

x = gaussian_elimination(a,b,n)







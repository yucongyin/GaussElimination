from forward import forward_substitution
from backward import backward_substitution
import sys
import numpy as np


def gaussian_elimination(a,b,n):
    #m =np.zeros((n,n))
    #define subdiagonal entry's diagonal to 1 and the rest place to 0 to fulfill
    l = np.eye(n)
    u = np.zeros((n,n))
    print("The original matrix M you entered is: \n")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in a]))
    print("Step 1: LU decomposition of A into A= LU (This step is done using Gauss Elimination)")
    for k in range(n-1):
        if a[k,k] == 0:
            print("It's a singular matrix you entered", file=sys.stderr)
            break

        for i in range(k+1,n):
            m = float(a[i][k])/float(a[k][k])
            #Lik = Mik
            l[i][k] = m
            for j in range(k,n):
                a[i][j] -= m * a[k][j]
                print(f"R{i+1} = R{i+1} - {int(m)}*R{k+1}: \n")
                print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in a]))
            
    u = a    
        
    

    print("Step 2: Ax = b is now LUx = b or Ly = b where y = Ux")
    print("After Gaussian Elimination,the subdiagonal entries of L are:")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in l]))
    print("After Gaussian Elimination,the superdiagonal entries of U are:")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in u]))
    
    print("Step 3: Solve for y in Ly = b, using forward substitution.")
    y = forward_substitution(l,b,n)
    print("y: ")
    print(*y)

    print("Step 4: Solve for x in Ux = y using back-substitution.")
    x = backward_substitution(u,y,n)
    


    print("Here are the Xs processed by the forward_substitution algorithm: \n")

    for i in range(len(x)):
        print(f"x[{i}] = {x[i]} ")

def main():
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
    a = np.array(a)
    gaussian_elimination(a,b,n)

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()





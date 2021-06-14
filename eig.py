import numpy

def eigenvector(mat):# mat =[[-6,3],[4,5]]  example 2x2 matrix 
    eig= []
    first = []
    summ=0
    c=0
    var=[]
    for i in range(len(mat)):
        eig.append(mat[i][i])
        print(eig)
    for i in range(len(eig)):
        summ = summ - eig[i]
    c=numpy.linalg.det(mat)
    eigenvalues = quadratic(1,summ, c)
    print(summ)
    print(eigenvalues)
    xvar=0
    y=0
    xs=0
    for x in eigenvalues:
        for i in range(len(mat)):
            if i==0:
                xvar= x - mat[i][0]
                y= mat[i][1]
                xs=  xvar / y
                return [1,xs]
                
            
            
    
def quadratic(a,b,c):
    roots=[]
    discriminant = b**2 - 4*a*c
    roots.append((-b + discriminant**(1/2))/(2*a))
    roots.append((-b - discriminant**(1/2))/(2*a))
    return roots

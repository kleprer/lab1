print('Ax^2 + Bx + C = 0')
a = float(input())
b = float(input())
c = float(input())
def roots(a,b,c):
    d = b**2 - 4*a*c
    if d>0:
        x1 = (-b + d**0.5)/(2*a)
        x2 = (-b - d**0.5)/(2*a)
        return "x1, x2 =  ", x1, x2
    if d<0:
        return "There're no roots."
    x = (-b)/(2*a)
    return "Single root: ", x
print(roots(a,b,c))
import  math

a = float(input('введите ваше число- '))

z1 = (1 - (0.25 * (math.sin(2*a) ** 2))) + (math.cos(2*a))
z2 = (math.cos(a) ** 2) + (math.cos(a) ** 4)

print(z1)
print(z2)
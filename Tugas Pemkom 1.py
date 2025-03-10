a=input(int("a="))
b=input(int("b="))
c=input(int("c="))
d=b**2-4*a*c
x1=(-b+(d)**(1/2))/(2*a)
x2=(-b-(d)**(1/2))/(2*a)
print("-------------------------------------------")
if a==0 :
    print("selesai")
elif d>0 :
    print("akar beda")
elif d==0:
        print("akar sama")
if d<0:
        print("imajiner")
else:
        print("-------------------------------------------")
        print(f"a={a},b={b},c={c},x1={x1},x2={x2}")
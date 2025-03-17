import random
u=random.randint(0,120)
print(f"ukuran yang dihasilkan: {u}")
if u>=100:
    ukuran="u1"
elif u>=80:
    ukuran="u2"
elif u>=50:
    ukuran="u3"
else:
    ukuran="u4"

w=random.randint(0,120)
print(f"ukuran yang dihasilkan: {w}")
if w>=75: 
    warna="w1"
elif w>=40:
    warna="w2"
else:
    warna="w3"

if ukuran=="u4" or warna=="w3":
    pasar="reject"
    print(f"tomat tidak layak didistribusikan dan akan {pasar}")
else:
    if warna=="w1":
        if ukuran== "u1" or ukuran =="u2":
            pasar="Ekspor"
        else:
            pasar="Supermarket"
    else:
        if warna=="w2":
            if ukuran=="u3" or ukuran=="u2":
                pasar="Pasar lokal"
            else:
                pasar="Supermarket"
    print (f"Ukuran tomat  dikategorikan ke: {ukuran},dan warna dikategorikan ke: {warna},sehingga didistibusikan ke {pasar} ")
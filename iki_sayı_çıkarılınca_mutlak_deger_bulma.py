x = int(input("Birinci sayıyı giriniz : "))
y = int(input("İkinci sayıyı giriniz : "))

mutlak_deger = abs(x-y)

print(f"İşlemin mutlak değerli sonucu : {mutlak_deger}")

def mutlak_deger():
    x = int(input("Birinci sayıyı giriniz : "))
    y = int(input("İkinci sayıyı giriniz : "))
    return abs(x-y)
print(f"Oluşan mutlak değerli sayı : {mutlak_deger()}")
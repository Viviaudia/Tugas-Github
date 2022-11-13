print("Program Menghitung Berat Badan Ideal")
#Berat badan kita termasuk dalam kategori yang mana
#BMI = Berat(kg) : Tinggi (m) x Tinggi (m)

p = int(input("berat badan :"))
q = int(input("tinggi badan :")) / 100 #harus dibagi 100 agar menjadi (m)
r = (p / (q*q))
print(p, "/", q*q, "=", r)

if r < 18.5:
    print("Underweight")
elif 18.5 < r < 24.9:
    print("Normalweight")
elif 25.0 < r < 29.9:
    print("Overweight")
elif 30.0 < r < 34.9:
    print("Obesity Class I")
elif 35.0 < r < 39.9:
    print("Obesity Class II")
elif 40.0 < r :
    print("Obesity class III")
import moduleku as math

input = float(input("Masukkan Diameter (cm) untuk menghitung Luas Lingkaran & Volume Bola: "))

hasil = round(math.circle(input), 2)

volume = round(math.ball(input), 2)
print(" ")
print(f"Luas Lingkaran: {hasil} cm²")

print(" ")
print(f"Volume Bola: {volume} cm³")

# Exercise 5 PCINU Belanda
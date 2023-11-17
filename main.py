#F1 = Kelvin to Celcius
def F1(K):
    f1 = K - 273
    return f1

suhu_kelvin = 300
suhu_celsius = F1(suhu_kelvin)
print("Function pertama ====")
print(f"{suhu_kelvin} Kelvin sama dengan {suhu_celsius:} Celsius\n")

#F2 = Celcius to Kelvin
def F2(C):
    f2 = C + 273
    return f2

suhu_celsius = 27
suhu_kelvin= F2(suhu_celsius)
print("Function kedua ===")
print(f"{suhu_celsius} Celcius sama dengan {suhu_kelvin:} Kelvin\n")

#F3 = Celcius/Kelvin to Fahrenheit
def F3_1(C):
    f3_1 = C*1.8 + 32
    return f3_1

def F3_2(K):
    f3_2 = (K-273)*1.8 + 32
    return f3_2

suhu_celsius = 0
suhu_kelvin = 273
suhu_fahrenheit= F3_1(suhu_celsius)
suhu_f1 = round(suhu_fahrenheit)
suhu_fahrenheit= F3_2(suhu_kelvin)
suhu_f2 = round(suhu_fahrenheit)
print("Function ketiga ===")
print(f"{suhu_celsius} Celcius sama dengan {suhu_f1:} Fahrenheit")
print(f"{suhu_kelvin} Kelvin sama dengan {suhu_f2:} Fahrenheit\n")


#F4 = Fahrenheit to Celcius/Kelvin 
def F4_1(F1):
    f4_1 = (F1-32)*1.8
    return f4_1

def F4_2(F2):
    f4_2 = (F2-32)*1.8 + 273
    return f4_2

suhu_F1 = 32
suhu_F2 = 32
suhu_celsius= F4_1(suhu_F1)
suhu_c = round(suhu_celsius)
suhu_kelvin= F4_2(suhu_F2)
suhu_k = round(suhu_kelvin)
print("Function keempat ===")
print(f"{suhu_F1} Fahrenheit sama dengan {suhu_c:} Celcius")
print(f"{suhu_F2} Fahrenheit sama dengan {suhu_k:} Kelvin\n")
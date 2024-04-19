language = {
    "name": "Python",
    "creator": "Guido Van Rossum"
}

"""for element in language.keys():
    print(element)

for element in language.values():
    print(element)

for key, value in language.items():
    print(key,value)

for key in language:
    print("key", key)
    print("value:", language[key])"""
frutas = {"fresa": "roja", "manzana": "verde", "plátano" : "amarillo"}
for fruta in frutas:
    x = 0
    for letra in fruta:
        x += 1
    print("fruta: ", fruta)
    print("tiene: ", x, " letras")



print(x, " x ", y, " = ", x*y)

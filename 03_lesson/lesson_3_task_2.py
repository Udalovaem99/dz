from smartphone import Smartphone

catalog = [
    Smartphone("Iphone", "15", "+79658436937"),
    Smartphone("Iphone", "12", "+79658345679"),
    Smartphone("Iphone", "11", "+79658332345"),
    Smartphone("Iphone", "7", "+79658335333"),
    Smartphone("Iphone", "5", "+79658338886")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")

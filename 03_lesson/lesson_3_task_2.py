from smartphone import Smartphone

catalog = []
catalog.append(Smartphone("Apple", "iPhone 11", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S20", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 9", "+79345678901"))
catalog.append(Smartphone("OnePlus", "8 Pro", "+79456789012"))
catalog.append(Smartphone("Google", "Pixel 4a", "+79567890123"))

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")
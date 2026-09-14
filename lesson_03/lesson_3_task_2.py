from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Samsung", "galaxy s24", "+79088900988"))
catalog.append(Smartphone("Apple", "iPhone15", "+79111199119"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13", "+79012727227"))
catalog.append(Smartphone("Huawei", "P60 Pro", "+79918388383"))
catalog.append(Smartphone("Google", "Pixel 8", "+79656556556"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")

from address import Adress
from mailing import Mailing

from_addr = Adress("123009", "Москва", "Тверская", "10", "5")
to_addr = Adress("630000", "Новосибирск", "Красный проспект", "20", "12")

shipment = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=350.50,
    track="RU123456789XX"
)

result = (
    f"Отправление {shipment.track} из {shipment.from_address.index}, "
    f"{shipment.from_address.city}, {shipment.from_address.street}, "
    f"{shipment.from_address.house} - {shipment.from_address.apartment}, "
    f"в {shipment.to_address.index}, {shipment.to_address.city}, "
    f"{shipment.to_address.street}, {shipment.to_address.house} "
    f"- {shipment.to_address.apartment}. Стоимость {shipment.cost} рублей."
)

print(result)

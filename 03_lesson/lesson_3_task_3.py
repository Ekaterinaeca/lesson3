from address import Address
from mailing import Mailing

to_address = Address("123456", "Moscow", "Lenin street", "10", "15")
from_address = Address("654321", "Saint Petersburg", "Pushkin street", "20", "25")
mailing = Mailing(to_address, from_address, 100, "12345")

print(f"Отправление {mailing.track} из {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house} - {to_address.apartment} \
в {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house} - {from_address.apartment}. Стоимость {mailing.cost} рублей.")

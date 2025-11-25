from address import Address
from mailing import Mailing

to_addr = Address("191025", "Санкт-Петербург", "Невский проспект", "Дом №30", "Квартира №12")
from_addr = Address('191010', 'Москва', 'Тверская улица', 'Дом №14', 'Квартира №3')

mailing = Mailing(
    to_address = to_addr,
    from_address = from_addr,
    cost = 350,
    track = "1234567890"
)

print(mailing)

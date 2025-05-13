from address import Address

from mailing import Mailing

to_address = Address("341244", "Ижевск", "Нижняя", "2", "11")
from_address = Address("109240", "Москва", "Набережная", "21", "23")

mailing = Mailing(to_address, from_address, 1500, "QW1234567654321")

print(mailing)

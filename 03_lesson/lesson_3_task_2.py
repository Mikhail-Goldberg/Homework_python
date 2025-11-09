from smartphone import Smartphone

catalog = [
    Smartphone('Nokia', '3310', '+79112223344'),
    Smartphone('Samsung', 'galaxy', '+79211234567'),
    Smartphone('Xiaomi', '13', '+79657265610'),
    Smartphone('Apple', '17 pro', '+79111199119'),
    Smartphone('Huawei', 'p60', '+79360521344')
]

for items in catalog:
    print(f'{items.brand} - {items.model}. {items.number}')
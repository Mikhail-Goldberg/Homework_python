class User:

    def __init__(self, first_name, last_name):
        self.name = first_name 
        self.surname = last_name

    def sayName(self):
        print('Меня зовут', self.name)
    
    def saySurname(self):
        print('Моя фамилия', self.surname)

    def sayFullname(self):
        print('Меня зовут', self.name, self.surname)
class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory


    @property
    def cpu(self):
        return self.__cpu


    @cpu.setter
    def cpu(self, value):
        self.__cpu = value


    @property
    def memory(self):
        return self.__memory


    @memory.setter
    def memory(self, value):
        self.__memory = value


    def make_computations(self):
        return f'Результат арифметического вычисления: {self.__memory * self.__cpu}'


    def __str__(self):
        return f'Computer CPU: {self.__cpu}, Computer memory: {self.__memory}'


    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory



class Phone:
    __sim_cards_list = ['O!', 'Mega']


    @property
    def sim_cards_list(self):
        return self.__sim_cards_list


    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value


    def call(self, sim_card_number, call_to_number):
        return f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number}'


    def __str__(self):
        return f'sim_cards_list:{self.__sim_cards_list}'



class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self)


    def use_gps(self, location):
        return f'Построен маршрут до: {location}'


    def __str__(self):
        return f'Phone CPU: {self.cpu} \n' \
               f'Phone memory: {self.memory} \n'

asus = Computer(16, 2048)
phone = Phone()
samsung = SmartPhone(8, 1024)
iphone = SmartPhone(6, 1014)



print(asus)
print('*' * 50)
print(phone)
print('*' * 50)
print(samsung)
print(iphone)
print(asus.make_computations())
sim_1 = 'Mega'
sim_2 = 'O!'

print(phone.call(sim_1, 996777889900))
print(SmartPhone.use_gps(samsung, 'Geeks'))
print('*' * 50)
print(iphone == samsung)
print(asus != iphone)
print(asus < asus)
print(asus > samsung)
print(asus >= iphone)
print(iphone <= iphone)


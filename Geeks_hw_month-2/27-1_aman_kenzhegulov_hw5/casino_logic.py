from random import randint
from casino import money
num = [randint(1, 31)]
bank = int(money)
def game():
    global bank
    while True:
            print(f'Ваш баланс: {bank}')
            action = input('Сделать ставку? ')
            if action == 'да':
                slot = int(input('Выберите слот от 1 до 30: '))
                bet = int(input('Сумма ставки: '))
                if slot == num and bet <= bank:
                    bank += (bet * bet)
                    print('Вы выиграли!')
                elif num != slot and bet <= bank:
                    if bank > 0 and bet <= bank:
                        bank -= bet
                        print('Вы не выиграли!')
                elif bet > bank:
                    print('У вас не хватает средств!')
                con = input('Продолжить игру? ')
                if con == 'да':
                    continue
                elif con == 'нет':
                    if bank >= 1000:
                        print(f'Вы в выигрыше\nваш баланс: {bank}')
                    elif bank <= 1000:
                        print(f'Вы в проигрыше\nваш баланс: {bank}')
                        break
                    elif bank == 0:
                        break

            elif action == 'нет':
                print('Игра окончена!')
                break


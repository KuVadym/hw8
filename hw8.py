from datetime import datetime, timedelta
users = [{"name": "Ivan", "birthday":  datetime(year=1986, month=2, day=5)},      # список словарей users, каждый словарь в нём обязательно имеет ключи name и birthday.
         {"name": "John", "birthday":  datetime(year=1976, month=2, day=7)}, 
         {"name": "Jan", "birthday":  datetime(year=1966, month=2, day=11)},
         {"name": "Juan", "birthday":  datetime(year=1956, month=2, day=12)},
         {"name": "Johann", "birthday":  datetime(year=1996, month=2, day=19)},
         {"name": "Giovanni", "birthday":  datetime(year=2006, month=2, day=27)},
         {"name": "Sean", "birthday":  datetime(year=2000, month=3, day=3)},]  

now = datetime.now()                                                              # Дейттайм обьект текущей даты
delta_two = now - timedelta (days = 2)                                            # Дейт тайм обьекты с разницей в -2 и + 7 дней (диапазон выходных и недели
delta_seven = now + timedelta (days = 7)

def get_birthdays_per_week (users):                                               # Функция принимает список словарей
    birthday_people = {}                                                          # Создание пустого словаря для вывода именинников
    for el in users:                                                              # Перебор словарей в списке
        date_val = (el.get("birthday")).replace(year = now.year)                  # создание переменной с выравниванием дат рождения на текущий год
        if now.weekday() == 0:                                                    # Условие если сегодня понедельник
            if delta_two < date_val < delta_seven:                                # Условие если дата рождения в диапазоне между субботой и воскресеньем
                birthday_people[el.get("name")]=(date_val).strftime("%A")         # Если условие правда добавляем имя как ключ, а дату рождения переведенную в строку в виде как день недели в значение
                #print (date_val.weekday(), el.get("name") )
        elif now.weekday() > 0:                                                   # Условие если сегодня не понедельник
            if now <= date_val < delta_seven:                                     # Условие если дата рождения сегодня или не более чем через семь дней
                birthday_people[el.get("name")]=(date_val).strftime("%A")
                #print (date_val.weekday(), el.get("name") )
    for key, val in birthday_people.items():                                      # Цикл выбора ключа и значения с Словаря
        print (val + ": " + key)                                                          # Печать значения и ключа

get_birthdays_per_week (users)

from datetime import datetime

def determine_quarter(date_str):
    """
    Функція визначає квартал року за вказаною датою.

    Параметри:
        date_str (str): Дата у форматі 'YYYY-MM-DD'.

    Повертає:
        int: Номер кварталу (1, 2, 3 або 4).
    """
    try:
        # Перетворюємо строку у об'єкт дати
        date = datetime.strptime(date_str, '%Y-%m-%d')
        month = date.month

        # Визначаємо квартал
        if 1 <= month <= 3:
            return 1
        elif 4 <= month <= 6:
            return 2
        elif 7 <= month <= 9:
            return 3
        elif 10 <= month <= 12:
            return 4
    except ValueError:
        return "Невірний формат дати. Введіть дату у форматі 'YYYY-MM-DD'."

# Приклад використання
if __name__ == "__main__":
    date_input = input("Введіть дату у форматі YYYY-MM-DD: ")
    result = determine_quarter(date_input)
    print(f"Квартал: {result}")

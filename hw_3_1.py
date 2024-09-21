from datetime import datetime

def get_days_from_today(date_string):

    try:
        # перетворюємо рядок в дату
        date = datetime.strptime(date_string, '%Y-%m-%d').date()
    except ValueError:
        # Якщо формат дати неправильний
        return "Error: Invalid date format. Please use 'YYYY-MM-DD'."

    # відображаємо поточну дату 
    current_date = datetime.today().date()

    # різниця в днях
    days_difference = (current_date - date).days
    
    # повертаємо результат 
    return days_difference



print(get_days_from_today("2024-09-20"))
print(get_days_from_today("2024-10-20"))
print(get_days_from_today("2024/10/20"))

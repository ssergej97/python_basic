user_input_num = int(input("Введіть число для конвертації в дату від 0 до 8640000, наприклад 224930 "))

user_input_days = user_input_num // (24 * 60 * 60)

user_input_days_in_sec = 24 * 60 * 60 * user_input_days

user_input_hours_in_sec = user_input_num - user_input_days_in_sec

user_input_hours = user_input_hours_in_sec // (60 * 60)

user_input_minutes_in_sec = 60 * 60 * user_input_hours

user_input_minutes_in_sec_rest = user_input_hours_in_sec - user_input_minutes_in_sec

user_input_minutes = user_input_minutes_in_sec_rest // 60

user_input_minutes_in_sec = 60 * user_input_minutes

user_input_seconds = user_input_minutes_in_sec_rest - user_input_minutes_in_sec

if user_input_days % 10 == 1 and user_input_days % 100 != 11:
    day_text = "день"
elif 2 <= user_input_days % 10 <= 4 and (user_input_days % 100 < 10 or user_input_days % 100 >= 20):
    day_text = "дні"
else:
    day_text = "днів"

print(f'{user_input_days} {day_text}, {str(user_input_hours).zfill(2)}:{str(user_input_minutes).zfill(2)}:{str(user_input_seconds).zfill(2)}')

user_input_num = 7948799

user_input_days = user_input_num // (24 * 60 * 60)

user_input_days_in_sec = 24 * 60 * 60 * user_input_days

user_input_hours_in_sec = user_input_num - user_input_days_in_sec

user_input_hours = user_input_hours_in_sec // (60 * 60)

user_input_minutes_in_sec = 60 * 60 * user_input_hours

user_input_minutes_in_sec_rest = user_input_hours_in_sec - user_input_minutes_in_sec

user_input_minutes = user_input_minutes_in_sec_rest // 60

user_input_minutes_in_sec = 60 * user_input_minutes

user_input_seconds = user_input_minutes_in_sec_rest - user_input_minutes_in_sec

print(f'{user_input_days} днів, {str(user_input_hours).zfill(2)}:{str(user_input_minutes).zfill(2)}:{str(user_input_seconds).zfill(2)}')

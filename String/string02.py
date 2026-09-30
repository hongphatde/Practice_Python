# Exercise 1: Smart Log Formatter
def smart_log_formatter(logs):
    if not logs:
        return []
    
    result = []
    current = logs[0]
    count = 1
    
    for index in logs[1:]:
        if index == current:
            count += 1
        else:
            if count > 1:
               result.append(f"{current} (x{count})")
            else:
                result.append(current)
            current = index
            count = 1
    
    if count > 1:
        result.append(f"{current} (x{count})")
    else:
        result.append(current)
    
    return result
'''
# Test case
print(smart_log_formatter(
                [
                    "INFO Connected",
                    "WARNING Low battery",
                    "INFO Connected"
                ]
            ))

print(smart_log_formatter(
                [
                    "INFO Start",
                    "INFO Start"
                ]
            ))
'''

# Exercise 2: 
def cat_mouse(x):
    # Create a count variable of character '.'
    number_character = x.count('.')
    # If '.' more than three characters between
    if number_character > 3:
        return "Escaped!"
    # If there are three characters between the two, the cat can jump
    return "Caught!"

'''
# Test case
print(cat_mouse('C...m'))
print(cat_mouse('C....m'))
print(cat_mouse('C.m'))
print(cat_mouse('Cm'))
'''

# Exercise 3: AGE In days
from datetime import date, timedelta
def age_in_days(year, mon, days):
    out = date.today() - date(year,mon, days)
    return f'You are  {out.days} days old'

today = date.today()
bday = today - timedelta(days=2)
print(age_in_days(bday.year, bday.month, bday.day))
bday = today - timedelta(days=365)
print(age_in_days(bday.year, bday.month, bday.day))


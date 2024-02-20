from collections import defaultdict
from datetime import datetime


def get_birthdays_per_week(users):
    # Create a dictionary to store users
    birthdays_per_week = defaultdict(list)

    # Get current date
    today = datetime.today().date()

    # Iterate
    for user in users:
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            print()
        if today <= birthday <= today + timedelta(days=7):
            day_of_week = birthday.strftime("%A")
            birthdays_per_week[day_of_week].append(user["name"])
    

    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 21)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)}
]

get_birthdays_per_week(users)

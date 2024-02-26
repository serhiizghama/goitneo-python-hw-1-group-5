from collections import defaultdict, OrderedDict
from datetime import datetime, timedelta


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
            birthday_this_year = birthday.replace(year=today.year+1)

        if today <= birthday_this_year <= today + timedelta(days=7):
            day_of_week = birthday_this_year.strftime("%A")
            if day_of_week == "Saturday" or day_of_week == "Sunday":
                day_of_week = "Monday"
            birthdays_per_week[day_of_week].append(user["name"])

    ordered_birthdays_per_week = OrderedDict(
        (day, birthdays_per_week[day]) for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    )

    for day, names in ordered_birthdays_per_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 2, 25)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 2, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 28)},
    {"name": "Bob Bobing", "birthday": datetime(1956, 2, 28)},
    {"name": "Omen Roment", "birthday": datetime(1986, 2, 26)},
    {"name": "Alex Muller", "birthday": datetime(1976, 2, 26)}
]

get_birthdays_per_week(users)

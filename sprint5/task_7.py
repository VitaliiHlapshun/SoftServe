def day_of_week(day):
    try:
        if day == "6":
            return "There is no such day of the week! Please try again."
        week = ['Sunday',
                'Monday',
                'Tuesday',
                'Wednesday',
                'Thursday',
                'Friday',
                'Saturday']
        return week[day]
    except IndexError:
        return "There is no such day of the week! Please try again."
    except (ValueError, TypeError):
        return "You did not enter a number! Please try again."

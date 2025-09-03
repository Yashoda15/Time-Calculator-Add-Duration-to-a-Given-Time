def add_time(start, duration, day=None):
    # Days of the week for indexing, all lowercase
    days_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    # Split start and duration
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Convert start time to 24-hour clock
    if period == "PM" and start_hour != 12:
        start_hour += 12
    if period == "AM" and start_hour == 12:
        start_hour = 0

    # Add duration
    total_minutes = start_minute + duration_minute
    extra_hours = total_minutes // 60
    new_minutes = total_minutes % 60

    total_hours = start_hour + duration_hour + extra_hours
    days_later = total_hours // 24
    new_hour_24 = total_hours % 24

    # Calculate new period and hour for output
    if new_hour_24 == 0:
        new_hour = 12
        new_period = "AM"
    elif new_hour_24 < 12:
        new_hour = new_hour_24
        new_period = "AM"
    elif new_hour_24 == 12:
        new_hour = 12
        new_period = "PM"
    else:
        new_hour = new_hour_24 - 12
        new_period = "PM"

    # Compose the new time string
    new_time_str = f"{new_hour}:{new_minutes:02d} {new_period}"

    # Handle day of week
    if day:
        day_index = days_list.index(day.lower())
        new_day_index = (day_index + days_later) % 7
        new_day = days_list[new_day_index].capitalize()
        new_time_str += f", {new_day}"

    # Handle days later annotation
    if days_later == 1:
        new_time_str += " (next day)"
    elif days_later > 1:
        new_time_str += f" ({days_later} days later)"

    return new_time_str

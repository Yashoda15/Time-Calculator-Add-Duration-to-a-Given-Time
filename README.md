# Time Calculator

## Description
The Time Calculator is a Python function that adds a duration to a given start time and returns the resulting time. It can handle 12-hour clock format inputs with AM/PM, compute the day of the week if provided, and indicate if the resulting time is on the next day or several days later.

This project is useful for scheduling, time-based calculations, or learning about time arithmetic in Python.

---

## Features
- Adds hours and minutes to a given start time.
- Handles AM/PM format correctly.
- Calculates the day of the week when an optional day parameter is provided.
- Indicates if the resulting time is the next day or multiple days later.
- Returns time in 12-hour format.

---

## Usage

```python
from time_calculator import add_time

# Add duration without specifying day
print(add_time("3:00 PM", "3:10"))  
# Output: "6:10 PM"

# Add duration with specifying day
print(add_time("11:30 AM", "2:32", "Monday"))  
# Output: "2:02 PM, Monday"

# Add duration that results in next day
print(add_time("11:43 PM", "24:20", "tuesday"))  
# Output: "12:03 AM, Thursday (2 days later)"

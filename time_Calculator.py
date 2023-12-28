def add_time(time, hrs, day=None):
    
    # get hours, minutes and format(PM or AM)
    hr1, frm, hr2 = int(time.split()[0].split(":")[0]), time.split()[
        1], int(hrs.split(":")[0])
    min1, min2 = int(time.split()[0].split(":")[1]), int(hrs.split(":")[1])
    # Operations
    total_hours = hr1+hr2
    total_minutes = min1+min2
    total_day = 0
    change_day = False

    # Format AM-PM
    if total_hours > 12 and hr2 % 2 != 0 and min2 != 0 and frm == "PM":
        frm = "AM"
        change_day = True
    elif total_hours > 12 and hr2 % 2 != 0 and min2 != 0 and frm == "AM":
        frm = "PM"
    elif total_hours > 12 and hr2 % 2 == 0 and min2 != 0 and frm == "AM":
        frm = "PM"
    elif total_hours > 12 and hr2 % 2 == 0 and min2 != 0 and frm == "PM":
        frm = "AM"
        change_day = True
    elif total_hours == hr1 and total_hours+(total_minutes - 60) >= 12 and frm == "AM":
        frm = "PM"
    elif total_hours == hr1 and total_hours+(total_minutes - 60) >= 12 and frm == "PM":
        frm = "AM"
        change_day = True
    # Total days
    if total_hours > 24 and total_minutes > 59 and change_day == True:
        total_day = round((total_hours+1)/24)
    elif total_hours > 24 and total_minutes <= 59 and change_day == True:
        total_day = round(total_hours/24)
    elif total_hours >= 24 and total_hours < 48:
        total_day = 1
    elif total_hours > 12 and change_day == True:
        total_day = 1
    # Conditions-format of  hours and minutes
    if total_hours > 12 and total_minutes > 59:
        total_hours = total_hours % 12 + 1
        total_minutes = total_minutes - 60
    elif total_hours > 12 and total_minutes < 60:
        total_hours = total_hours % 12
    elif total_hours < 12 and total_minutes > 60:
        total_hours += 1
        total_minutes = total_minutes - 60
    else:
        pass
    # Day of the week
    day_Week = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    after_day = 0
    if total_day >= 1 and day:
        for i in range(len(day_Week)):
            if day_Week[i].lower() == day.lower():
                after_day = i
        for i in range(total_day):
            after_day += 1
            if after_day > 6:
                after_day = 0
    # Format data
    total_minutes = str(total_minutes)
    if day is None and total_day == 0:
        if len(total_minutes) == 1:
            return f'{total_hours}:0{total_minutes} {frm}'
        else:
            return f'{total_hours}:{total_minutes} {frm}'
    if day and total_day == 0:
        if len(total_minutes) == 1:
            return f'{total_hours}:0{total_minutes} {frm}, {day}'
        else:
            return f'{total_hours}:{total_minutes} {frm}, {day}'
    if day is None and total_day == 1:
        if len(total_minutes) == 1:
            return f'{total_hours}:0{total_minutes} {frm} (next day)'
        else:
            return f'{total_hours}:{total_minutes} {frm} (next day)'
    if day and total_day == 1:
        if len(total_minutes) == 1:
            return f'{total_hours}:0{total_minutes} {frm}, {day_Week[after_day]} (next day)'
        else:
            return f'{total_hours}:{total_minutes} {frm}, {day_Week[after_day]} (next day)'
    if day is None and total_day > 1:
        if len(total_minutes) == 1:
            return f'{total_hours}:0{total_minutes} {frm} ({total_day} days later)'
        else:
            return f'{total_hours}:{total_minutes} {frm} ({total_day} days later)'
    if day and total_day > 1:
        if len(total_minutes) == 1:
            return f'{total_hours}:0{total_minutes} {frm}, {day_Week[after_day]} ({total_day} days later)'
        else:
            return f'{total_hours}:{total_minutes} {frm}, {day_Week[after_day]} ({total_day} days later)'


print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "Tuesday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)


def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
	calendar1_with_unavailable_times = add_unavailable_times(calendar1, dailyBounds1)
    calendar2_with_unavailable_times = add_unavailable_times(calendar2, dailyBounds2)
    calendar1_parsed = list(map(lambda m: [time_to_minutes(m[0]), time_to_minutes(m[1])], calendar1_with_unavailable_times))
    calendar2_parsed = list(map(lambda m: [time_to_minutes(m[0]), time_to_minutes(m[1])], calendar2_with_unavailable_times))
    merged_calendars = merge_calendars(calendar1_parsed, calendar2_parsed)
    non_overlapping_times = combine_overlapping_times(merged_calendars)
    available_slots = get_available_slots(non_overlapping_times, meetingDuration)
    available_slots_to_minutes = map(lambda m: [minutes_to_time(m[0]), minutes_to_time(m[1])], available_slots)
    return list(available_slots_to_minutes)

def minutes_to_time(minutes):
    hours = minutes // 60
    mins = minutes % 60
    hour_string = str(hours)
    min_string = '0' + str(mins) if mins < 10 else str(mins)
    return hour_string + ':' + min_string

def get_available_slots(cal, duration):
    available_slots = []
    for i in range(1, len(cal)):
        slot_start_time = cal[i-1][1]
        slot_end_time = cal[i][0] 
        if slot_end_time - slot_start_time >= duration:
            available_slots.append([slot_start_time, slot_end_time])
    return available_slots

def combine_overlapping_times(cal):
    non_overlapping_times = []
    non_overlapping_times.append(cal[0])
    for i in range(1, len(cal)):
        combine_time = []
        if cal[i][0] <= non_overlapping_times[-1][1]:
            prev_start_time, prev_end_time = non_overlapping_times.pop()
            combine_time.append(prev_start_time)
            combine_time.append(max(prev_end_time, cal[i][1]))
            non_overlapping_times.append(combine_time)
        else:
            non_overlapping_times.append(cal[i])
    return non_overlapping_times


def time_to_minutes(time):
    hour, minutes =  list(map(int, time.split(':'))) 
    return hour * 60 + minutes

def merge_calendars(c1, c2):
    merged_calendar = []
    i = 0
    j = 0
    while i < len(c1) and j < len(c2):
        if c1[i][0] <= c2[j][0]:
            merged_calendar.append(c1[i])
            i += 1
        else:
            merged_calendar.append(c2[j])
            j += 1
    
    while i < len(c1):
        merged_calendar.append(c1[i])
        i += 1

    while j < len(c2):
        merged_calendar.append(c2[j])
        j += 1
    return merged_calendar

def add_unavailable_times(calendar, bounds):
    first_available_time = bounds[0]
    start_of_day = '00:00'
    calendar.insert(0, [start_of_day, first_available_time])
    last_available_time = bounds[1]
    end_of_day = '23:59'
    calendar.append([last_available_time, end_of_day])
    return calendar

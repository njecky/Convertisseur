def convert_time_in_seconds(time_string: str) -> int:
    if time_string.count(':') == 1:
        time_string = "00:" + time_string 
    hours,minutes, seconds =map(int, time_string.split(':'))
    # parts = list(map(int, time_string.split(':')))

    # if len (parts) == 3:
    #     hours = parts[0]
    #     minutes = parts[1]
    #     seconds = parts[2]
    # elif len(parts) == 2:
    #     hours = 0
    #     minutes = parts[0]
    #     seconds = parts[1]

    # hours,minutes, seconds =map(int, time_string.split(':'))
    return hours * 3600 + minutes * 60  + seconds


if __name__== '__main__':
    assert convert_time_in_seconds('04:45:23') == 17123
    assert convert_time_in_seconds('01:00:00') == 3600
    assert convert_time_in_seconds('01:00') == 60
    assert convert_time_in_seconds('05:30') == 330
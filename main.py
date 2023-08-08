def convert_time_in_seconds(time_string: str) -> int:
    hours,minutes, seconds =map(int, time_string.split(':'))
    return hours * 3600 + minutes * 60  + seconds


if __name__== '__main__':
    assert convert_time_in_seconds('04:45:23') == 17123
    assert convert_time_in_seconds('01:00:00') == 3600
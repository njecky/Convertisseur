# permet de convertir le temps du format "H:M:S" ou au format "M:S"
def convert_time_in_seconds(time_string: str) -> int:
    if time_string.count(':') == 1:
        time_string = "00:" + time_string 
    hours,minutes, seconds =map(int, time_string.split(':'))

    return hours * 3600 + minutes * 60  + seconds


if __name__== '__main__':
    assert convert_time_in_seconds('04:45:23') == 17123
    assert convert_time_in_seconds('01:00:00') == 3600
    assert convert_time_in_seconds('01:00') == 60
    assert convert_time_in_seconds('05:30') == 330
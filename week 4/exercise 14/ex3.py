'''
 Define a dict whose keys are dates (represented by strings) from the most recent
week and whose values are temperatures. Ask the user to enter a date, and display the temperature on that date, as well as the previous and subsequent dates,
if available.
'''

# Date format: "YYYY-MM-DD"
TEMPS = {
    '2024-01-29': 20,
    '2024-01-30': 25,
    '2024-02-01': 22,
    '2024-02-02': 20,
    '2024-02-03': 18,
    '2024-02-04': 15,
    '2024-02-05': -2,
}

def temp_check():
    dates = list(TEMPS.keys())
    date = input("What day should we check?(Date format: 'YYYY-MM-DD'): ")

    if date in TEMPS:
        print(f'The temperature on {date} was {TEMPS[date]}° degrees')
        try:
            yesterday = dates[dates.index(date)-1] if dates.index(date) > 0 else None
            print(f'The temperature on {yesterday} was {TEMPS[yesterday]}° degrees')
        except:
            pass
        try:
            tomorrow = dates[dates.index(date)+1]
            print(f'The temperature on {tomorrow} was {TEMPS[tomorrow]}° degrees')
        except:
            pass


if __name__ == "__main__":
    temp_check()
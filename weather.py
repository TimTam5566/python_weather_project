import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"



def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    #date_object hold the data from the converted iso string
    #datetime is a module that assists in managing date and time
    #fromisoformat is a class that converts from iso format to a proper date time object
    #date_object is then used to access information including year, month, day etc
    #strftime stands for string format time, (%A %d %B %Y) = Weekday, Date, Month, Year
    
    date_object = datetime.fromisoformat(iso_string) 
    return date_object.strftime("%A %d %B %Y")
    

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    # round, rounds the converted temp, the 1 at the end of the equation rounds to 1 decimal place
    # float-allows decimal places
    # temp_in_farenheit - imports the temp in F into the equation
    # (F-32) * 5/9 is the equation to convert F to c
    return round((float(temp_in_fahrenheit)- 32) * 5 / 9, 1)



def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # weather_data - expected to be a list of numbers or strings
    # total = 0 count = 0, are initialising variables to keep track of
            # total - the sum of all values in the list, converted to floats
            # count - the number of valid entries we’ve added
    # for value in weather_data: loop that goes through each value in the waether_data list one at a time
    # total += float(value) - converts each item to a float and adds it to a running total
    # count += 1 - everytime a value is processed it bumps the count by one to keep track of how many values we are averaging across
    # return total / count - calculates mean of all values added divided by count of values

    total = 0
    count = 0

    for value in weather_data:
        total += float(value)
        count += 1

    return total / count
    

def load_data_from_csv(csv_file):

    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header row

            for row in reader:
                if row and all(row[1:]): #makes sure all temperature columns are present
                    try:
                        parsed_row = [row[0]] + [int(val) for val in row[1:]]
                        data.append(parsed_row)
                    except ValueError:
                        continue #
                
    return data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # use weather_data list to find minimum value and its position in the list
    # if multiple matches return index of the last example in the list
    # may need to be a loop to go through the weather_data list 
    # will need to calculate the mimimum value 
    # incase of multiple mimimum return index of the last example in the list
    
    if not weather_data:
        return ()

    min_val = float(weather_data[0])
    min_index = 0

    for i, val in enumerate(weather_data):
        if float(val) <= min_val:
            min_val = float(val)
            min_index = i

    return min_val, min_index

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
     
    if not weather_data:
        return ()

    max_val = float(weather_data[0])
    max_val_index = 0

    for i, val in enumerate(weather_data):
        if float(val) >= max_val:
            max_val = float(val)
            max_index = i

    return max_val, max_index

    data = load_data_from_csv("tests/data/example_one.csv")
    generate_summary(data)

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    num_days = len(weather_data)
    min_temps = []
    max_temps = []

    for day in weather_data:
        min_temp_c = convert_f_to_c(day[1])
        max_temp_c = convert_f_to_c(day[2])
        min_temps.append(min_temp_c)
        max_temps.append(max_temp_c)

    min_value, min_index = find_min(min_temps)
    max_value, max_index = find_max(max_temps)

    min_date = convert_date(weather_data[min_index][0])
    max_date = convert_date(weather_data[max_index][0])
    
    average_low = calculate_mean(min_temps)
    average_high = calculate_mean(max_temps)

    summary = (
        f"{num_days} Day Overview\n"
        f"  The lowest temperature will be {format_temperature(min_value)}, and will occur on {min_date}.\n"
        f"  The highest temperature will be {format_temperature(max_value)}, and will occur on {max_date}.\n"
        f"  The average low this week is {format_temperature(round(average_low, 1))}.\n"
        f"  The average high this week is {format_temperature(round(average_high, 1))}.\n"
    )
    print("SUMMARY OUTPUT:\n", summary)
    return summary



    

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
    summary_lines = []

    for day in weather_data:
        date = convert_date(day[0])
        min_temp = convert_f_to_c(day[1])
        max_temp = convert_f_to_c(day[2])

        line = (
            f"---- {date} ----\n"
            f"  Minimum Temperature: {format_temperature(min_temp)}\n"
            f"  Maximum Temperature: {format_temperature(max_temp)}\n"
        )
        summary_lines.append(line)

    return "\n".join(summary_lines) + "\n"

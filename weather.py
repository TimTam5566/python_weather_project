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
    #strftime
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
    pass


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

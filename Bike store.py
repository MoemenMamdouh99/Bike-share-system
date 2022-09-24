import datetime as dt
import numpy as np
import pandas as pd
from pandas.io.parsers import read_csv

cities = {"chicago":r"C:\Users\lenovo\OneDrive\Desktop\python\my projects\Bike store\chicago.csv"
        ,"nyc":r"C:\Users\lenovo\OneDrive\Desktop\python\my projects\Bike store\new_york_city.csv"
        ,"washington":r"C:\Users\lenovo\OneDrive\Desktop\python\my projects\Bike store\washington.csv"}
print("Hello! let's explore the bike share system of USA".title())

print("*"*50)


def get_data():
    """this is function to get data from the user 
    requires the name of the city, month , day  or all of them """

    city = str(input('which city you wanna apply the filter : "chicago - nyc - washington"')).lower().strip()
    while city not in cities:
        city = input('Enter the right name of the city')
        print("###")
    month = str(input('which month you wanna filter (january, february,march,april,may, or june?) or you wanna "all" ')).lower()
    print("###")
    day = str(input('which day ( monday,tuesday,Wednesday,Thursday,Friday,Saturday, or Sunday?) or you wanna "all" ')).lower() 
    print("###")
    return city , month , day
# print('#'*50)


def loading_data(city,month,day):
    '''this function load data to dataframe 
    and it returns the data '''

    df = pd.read_csv(cities[city])
    
    df['Start Time']= pd.to_datetime(df['Start Time'])
    
    df['month']= df['Start Time'].dt.month
    
    df['day']= df['Start Time'].dt.day_name()
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df
# print('#'*50)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    # print('\nCalculating The Most Frequent Times of Travel...\n')
    # start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = df['month'].mode()[0]
    print(f'The most common month is: {months[month-1]}')

    # display the most common day of week
    day = df['day'].mode()[0]
    print(f'The most common day of week is: {day}')

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f'The most common start hour is: {popular_hour}')

    # print("\nThis took %s seconds." % (time.time() - start_time))
    # print('-'*40)

# print('#'*50)


def most_common_stations (df):
    '''function finds out the most popular station start or end 
    also finds out the most popular trip '''

    common_start =  df['Start Station'].mode()[0]
    common_end =  df['End Station'].mode()[0]
    common_trip = df["Start Station"]+ ' to ' + df['End Station']

    print(f'the most common start station =>  {common_start}')
    print("###")
    print(f'the most common end station is => {common_end}')
    print("###")
    print(f"the most frequent trip is => from {common_trip.mode()[0]}")

# print('#'*50)


def travel_time (df):
    '''function finds out the trip duration in average and total '''
    total_travel_duration= (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    print(f'Total travel duration is => {total_travel_duration}')
    average_travel_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    print(f'Average travel duration is => {average_travel_duration}')
# print('#'*50)
def User_types(df,city):
    '''functions define the User type , gender and birth year '''
    data = read_csv(cities[city])
    if city != 'washington':
        user_type = data['User Type'].value_counts()
        gender = data['Gender'].value_counts()
        earliest = data['Birth Year'].min()
        most_recent = data['Birth Year'].max()
        most_common = data['Birth Year'].mode()[0]
        print(f'The count of user type is {user_type}')
        print("###")
        print(f"Gender count is {gender}")
        print("###")
        print(f"count of Birth year is {earliest:.0f} for earliest ### {most_recent:.0f} for most recent ### {most_common:.0f} for the most common")
        print("###")
    else:
        user_type = data['User Type'].value_counts()
        print(f'The count of user type is {user_type}')
# print('#'*50)

def main():
    while True:
        city , month , day  = get_data()
        
        df = loading_data(city,month,day)
        
        time_stats(df)
        
        print('#'*50)

        most_common_stations (df)
        print('#'*50)

        travel_time (df)
        print('#'*50)
        
        User_types(df,city)
        
        print('#'*50)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

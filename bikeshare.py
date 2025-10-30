# read the README file before changing sth

import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new_york_city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input("From which city do you want to see the data from?\n").lower()
        if city in valid_cities:
                break
        else:
                print("Invalid city. Please choose from Chicago, New York City, or Washington.")


    # get user input for month (all, january, february, ... , june)
    valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("From which month do you want to see the data from?\n").lower()
        if month in valid_months:
            break
        else:
             print("Invalid month. Please choose from january, february, march, april, may, june or all.")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("From which day do you want to see the data from?\n").lower()
        if day in valid_days:
            break
        else:
             print("Invalid day. Please choose from monday, tuesday, wednesday, thursday, friday, saturday, sunday or all.")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    ###City   
    df = pd.read_csv(CITY_DATA[city]) 
                     
    

    ###Month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]


    ###Day
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]
 
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most common month: ', df['month'].mode()[0])

    # display the most common day of week
    print('Most common day of week: ', df['day_of_week'].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('Most common hour: ', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most commonly used start station: ', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('Most commonly used end station: ', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip: ', df[['Start Station', 'End Station']].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #df['Trip Duration'] = pd.to_timedelta(df['Trip Duration'])

    # display total travel time
    print('Total travel time in minutes: ', df['Trip Duration'].sum() / 60)

    # display mean travel time
    print('Mean travel time in minutes: ', df['Trip Duration'].mean() / 60)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    # Display counts of gender
    
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    else:
        print("Gender data not available.")

    # Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' in df.columns:
        print('Earliest birth year: ', df['Birth Year'].min())
        print('Most recent birth year: ', df['Birth Year'].max())
        print('Most common birth year: ', df['Birth Year'].mode()[0])
    else:
        print("Birth year data not available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    valid_answers = ['yes', 'no']
    i = 0

    while True:
        answer = input("Do you want to see five rows of data?\n").lower()
        if answer == 'yes':
            while answer == 'yes':
                print(df.iloc[i:i+5])
                i += 5
                break
        elif answer == 'no':
            break        
        else:
                print("Invalid answer. Please choose from yes or no.")

              
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('city to analyze: ').lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print('invalid input')
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('input a month (january, february, ... , june) or all: ').lower()
        if month not in ('january','february','march','april','may','june','all'):
            print('invalid input')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('input a day of week (all, monday, tuesday, ... sunday): ').lower()
        if day not in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'):
            print('invalid input')
        else:
            break

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
    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    months = ['january','february','march','april','may','june']
    print('the most common month is {}'.format(months[common_month - 1].title()))

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('the most common day of the week is {}'.format(common_day_of_week.title()))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular start hour: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station: ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End Station'] = df['Start Station'] + '-' + df['End Station']
    common_start_end_station = df['Start-End Station'].mode()[0]
    print('The most frequent combination of start station and end station trip: ', common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    seconds_input = df['Trip Duration'].sum()
    sum_conversion = time.strftime('%H:%M:%S', time.gmtime(seconds_input))
    print('The total travel time is: ', sum_conversion)

    # TO DO: display mean travel time
    mean_input = df['Trip Duration'].mean()
    mean_conversion = time.strftime('%H:%M:%S', time.gmtime(mean_input))
    print('The mean travel time is: ', mean_conversion)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    df['User Type New'] = df['User Type'].str.strip()
    print('/n', df.groupby(['User Type New']).size())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        df['Gender New'] = df['Gender'].str.strip()
        print('/n', df.groupby(['Gender New']).size())
    else:
        print('\nNo Gender column in chosen city csv')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth' in df.columns:
        print('The earliest year of birth: ', df['Birth Year'].min())
        print('\nThe most recent year of birth: ', df['Birth Year'].max())
        print('\nThe most common year of birth: ', df['Birth Year'].mode()[0])
    else:
        print('\nNo Birth column in chosen city csv')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

print('check this')

def display_data(df):
    while True:
        view_data = input("\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n").lower()
        if view_data not in ('yes', 'no'):
            print('invalid input')
        else:
            break
    start_loc = 0
    view_display = 'yes'
    while (view_data == 'yes' and view_display == 'yes'):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        while True:
            view_display = input("\nDo you wish to continue? Enter yes or no.\n").lower()
            if view_display not in ('yes', 'no'):
                print('invalid input')
            else:
                break
        if view_display != 'yes':
            break


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

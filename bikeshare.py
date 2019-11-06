import time
import pandas as pd
import numpy as np

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

    while True:
        try:
            city = input('Enter a city(chicago, new york city, washington): ').lower()
        except:
            print('That is not a valid input')
        break

    while True:
        try:
            month = input('Enter a month (all, january, february ...): ').lower()
        except:
            print('That is not a valid input')
        break
    while True:
        try:
            day = input('Enter a day of week(all, monday, tuesday, ... sunday): ').lower()
        except:
            print('That is not a valid input')
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
    df['day'] = df['Start Time'].dt.day


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    common_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    df['day']=df['Start Time'].dt.weekday_name
    common_dayofweek = df['day'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    total_travel_time = df['Trip Duration'].mean()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()

    if "Gender" in df.columns:
        gender = df['Gender'].value_counts()
    else:
        print("Gender column does not exists")

    if "Birth Year" in df.columns:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()
    else:
        print("Birth year column does not exists")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays raw bikeshare data."""

    while True:
        raw_data = input('\nWould you like to view 5 lines of raw bikeshare data? Enter yes or no.\n')
        lower_bound=0
        upper_bound=5

        if raw_data.lower() != 'yes':
            break
        else:
            print('df[df.columns[0:]].iloc[lower_bound:upper_bound]')
            lower_bound += 5
            upper_bound += 5
            return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while restart.lower() not in ['yes', 'no']:
            print("Invalid input. Please type 'yes' or 'no'.")
            restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

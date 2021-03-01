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
    print('\n\nHello! We will explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nWould you like to see data for, Chicago, New York City, or Washington ?\n')
    while city.title() not in ('Chicago', 'New York City', 'Washington'):
        city = input('\nYou should choose one of the three cities: Chicago, New York, or Washington.\n')

    # asking user to choice filter
    choice = input('\nWould you like to filter the data by month, day, both, or not at  all? type "none" for no time filter.\n')
    while choice.lower() not in ('month', 'day', 'both','none'):
        choice = input('\nYou should choose one of the filtring choices month, day, both, or none (for no time filtring).\n')
    if choice.lower() == 'month':
        # TO DO: get user input for month (all, january, february, ... , june)
        month = input('\nWhich month ? january, February, March, April, May, or June.\n')
        while month.lower() not in ('january', 'February', 'March', 'April', 'May','June') :
            month = input('\nPlease enter month name correctly, january, February, March, April, May, or June.\n')
        day = 'all'
    elif choice.lower() == 'day' :
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('\nWhich day ? Sun, Mon, Tue, Wed, Thu, Fri, Sat \n')
        while day.title() not in ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'):
            day = input('\nPlease enter the the day abbreviation, Sun, Mon, Tue, Wed, Thu, Fri, or Sat \n')
        month = 'all'
    elif choice.lower() == 'both':
        month = input('\nWhich month ? january, February, March, April, May, or June.\n')
        while month.lower() not in ('january', 'February', 'March', 'April', 'May','June') :
            month = input('\nPlease enter month name correctly, january, February, March, April, May, or June.\n')
        day = input('\nWhich day ? Sun, Mon, Tue, Wed, Thu, Fri, Sat \n')
        while day.title() not in ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'):
            day = input('\nPlease enter the the day abbreviation, Sun, Mon, Tue, Wed, Thu, Fri, or Sat \n')
    else:
        month = 'all'
        day = 'all'
        print('No Filtring.')


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
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month #return the number of the month
    df['day_of_week'] = df['Start Time'].dt.weekday #return the number of the day where monday is 0

    # filtering by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1
        df = df[df['month'] == month]

    # filtering by day of week
    if day != 'all':
        days = {'Sun': 6, 'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5}
        day = days[day.title()]
        df = df[df['day_of_week'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    month_name = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June'}
    print('Most Popular month:', month_name[popular_month])

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    day_name = {6:'Sunday', 0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday' }
    print('Most Popular day:', day_name[popular_day])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_sstation = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_sstation)

    # TO DO: display most commonly used end station
    popular_estation = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_estation)

    # TO DO: display most frequent combination of start station and end station trip
    comp_station = pd.DataFrame((df['Start Station'] + ' \ ' + df['End Station']), columns=['mobin_station'])
    popular_comp_station = comp_station['mobin_station'].mode()[0]
    print('Most Frequent Combination Of Start Station And End Station Trip:', popular_comp_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total Travel time: ', total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean Travel time: ', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts Of User Types:\n', user_types)

    # TO DO: Display counts of gender
    if city.lower() == 'chicago' or city.lower() == 'new york city':
        user_gender = df['Gender'].value_counts()
        print('\nCounts Of User Gender:\n', user_gender)
        # TO DO: Display earliest, most recent, and most common year of birth
        print('\nDisplay earliest, most recent, and most common year of birth...')
        recent_year = df['Birth Year'].max()
        earliest_year = df['Birth Year'].min()
        common_year = df['Birth Year'].mode()[0]
        print('Most Recent Year: ',recent_year)
        print('Earliest Year: ',earliest_year)
        print('Most Common Year: ',common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df,city):
    """ Dispaly raw data upon requested by the user, 5 raw at a time"""
    decision = input('\nWould you like to represent the First 5 Rwa data? "Yes" or "No"\n')
    skiprows = 0

    while decision.lower() == 'yes' :
        print(pd.read_csv(CITY_DATA[city.lower()], skiprows=skiprows ,nrows=4))
        skiprows += 5
        decision = input('\nWould you like to represent the Next 5 Rwa data? "Yes" or "No"\n')



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while restart.lower() not in ('yes','no'):
            restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()

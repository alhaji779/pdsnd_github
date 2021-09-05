import time
import sys
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
    print('Hello! Welcome to my first python project. Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print('\nPlease Enter the city you like to view')
        citi = input('\nChicago, New York City or Washington:?\n')
        city = citi.lower()
        if city not in ('chicago','new york city','washington'):
            print("Sorry, check your spelling and remember You can only filter for Chicago, New York City or Washington ")
            continue
        else:
            break
        


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        print('\nPlease Enter the month you like to view')
        mont = input("\nJanuary - June, you can type 'all' if you want to view all\n")
        month = mont.title()
        if month not in ('All','January','February','March','April','May','June'):
            print("Sorry, check your spelling, seems your entry is invalid")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print('\nPlease Enter the day of week you like to view')
        da = input("\nEnter Monday - Sunday, you can type 'all' if you want to view all\n")
        day = da.title()
        if day not in ('All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'):
            print("Sorry, check your spelling, seems your entry is invalid")
            continue
        else:
            break

    print('-'*80)
    print('*'*40)
    print('-'*80)
    print("Preparing info for {} on {} of {} 2017 ".format(city.title(),day,month))
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
    #print(df.head(2))
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create new columns called month and day_of_week

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("Most Common Month is {}".format(common_month))


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("Most Common Day of Week is {}".format(common_day))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print("Most Common Start Hour is {}".format(common_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)
    print('/'*40)
    print('-'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_st = df['Start Station'].mode()[0]
    print("Most Commonly Used Start Station is {}".format(common_start_st))


    # TO DO: display most commonly used end station
    common_end_st = df['End Station'].mode()[0]
    print("Most Commonly Used End Station is {}".format(common_end_st))


    # TO DO: display most frequent combination of start station and end station trip
    frequent_com = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).head(1)
    print("Most commonly used frequent combination are \n {}".format(frequent_com))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)
    print('/'*40)
    print('-'*80)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
          
    total_travel_time = df['Trip Duration'].sum()      
    print("The Total Travel time is {}".format(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The Mean Travel time is {}".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)
    print('/'*40)
    print('-'*80)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print("User Types\n {}".format(user_type))


    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("Gender Count\n {}".format(gender))
    except Exception as e:
        print("Sorry there is no data on Gender available for this selection")
          

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_com_yr = df['Birth Year'].mode()[0]
        print("The Earliest Year of Birth is {}".format(earliest))
        print("The Most Recent Year of Birth is {}".format(most_recent))
        print("The Most Common Year of Birth is {}".format(most_com_yr))
    except Exception as e:
        print("Sorry, There is no data available earliest,most recent and most common year of birth to display for your selection")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40 + '/'*20 + '-'*40)
    
def raw_data(df):
    """ This function allows the user view raw data from the df file. On request, the user can continously view more raw data
    """
    extra = 0
    x_data = None
    while True:
        print("\nWould you like to view some raw data?\n")
        data = input("\nEnter Yes or No\n").lower()
        if data == 'yes':
            x_data = data
            print(df.head())
            while True:
                print("\nDo you want to view more raw data?\n")
                extra += 5
                data = input("\nEnter yes or no\n").lower()
                if data == 'yes':
                    print(df[extra:extra+5])
                else:
                    break
        elif data not in ('yes','no'):
            print("\nPlease Enter a valid input, yes or no:\n")
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        animation = "|/-\\"
        for i in range(50):
            time.sleep(0.1)
            sys.stdout.write("\r"+ animation[i % len(animation)])
            sys.stdout.flush()

        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

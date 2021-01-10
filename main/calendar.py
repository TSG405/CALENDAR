# Dict. For -- Months
ls = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

leap_to_reg_key_forward = {8:3, 13:1, 11:6, 9:4, 14:2, 12:7, 10:5}
reg_to_leap_key_forward = {7:8, 5:13, 3:11, 1:9, 6:14, 4:12, 2:10}
leap_to_reg_key_backward = {8:7, 13:5, 11:3, 9:1, 14:6, 12:4, 10:2}
reg_to_leap_key_backward = {3:8, 1:13, 6:11, 4:9, 2:14, 7:12, 5:10}


# HELPER-FUNCTIONS ..
def is_num(input_num):
    num = '0123456789'
    status = True
    for char in input_num:
        if char not in num:
            return False
    return status

def is_month(month):
    if is_num(month):
        month = int(month)
        return month >= 1 and month <= 12
    else:
        return False

def is_date(date):
    if is_num(date):
        date = int(date)
        return date >= 1 and date <= 31
    else:
        return False

def is_year(year):
    return is_num(year)

def is_correct_date_format(date):
    return is_month(date[0:2]) and is_date(date[3:5]) and is_year(date[6::]) and date[2] == '/' and date[5] == '/'

def find_key(year):
    key = 2
    
    if year > 1990:
        for i in range(1990, year):
            if is_leap_year(i):
                key = leap_to_reg_key_forward[key]
            else:
                if is_leap_year(i + 1):
                    key = reg_to_leap_key_forward[key]
                else:
                    if key <= 6:
                        key += 1
                    else:
                        key = 1
   
   elif year < 1990:
        for i in range(1990, year, -1):
            if is_leap_year(i):
                key = leap_to_reg_key_backward[key]
            else:
                if is_leap_year(i - 1):
                    key = reg_to_leap_key_backward[key]
                else:
                    if key >= 2:
                        key -= 1
                    else:
                        key = 7
    return key    

def days_from_start(month, date, key):
    days = 0
    
    if key >= 8:
        if month >= 2:
            for i in range(0, month - 1):
                days += ls[i + 1]
            days += date
        elif month == 1:
            days = date
            
    elif key <= 7:
        if month >= 3:
            for i in range(0, month - 1):
                days += ls[i + 1]
            days += date - 1
        elif month == 2:
            days = ls[1] + date
        else:
            days = date            
    return days

def find_start_day_in_january(key):
    start_day = key % 7
    return start_day

def day_in_num_to_letters(day_in_num):
    conversion_table = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    return conversion_table[day_in_num]

def find_start_day_of_month(month, year):
    key = find_key(year)
    days_til_previous_month = 0
    
    if key >= 8:
        if month >= 2:
            for i in range(0, month - 1):
                days_til_previous_month += ls[i + 1]
        elif month == 1:
            days_til_previous_month = 0
    
    elif key <= 7:
        if month >= 3:
            for i in range(0, month - 1):
                days_til_previous_month += ls[i + 1]
            days_til_previous_month -= 1
        elif month == 2:
            days_til_previous_month = ls[1] 
        else:
            days_til_previous_month = 0

    start_day_in_jan = find_start_day_in_january(key)
    this_month_start_day_in_num = (days_til_previous_month + start_day_in_jan - 1) % 7

    return (this_month_start_day_in_num)
    
    
    
# UTILZABLE FUNCTIONS ..
def is_leap_year(year):
    year_div_4 = year % 4
    year_div_100 = year % 100
    year_div_400 = year % 400

    is_leap_year = False
    
    if year_div_4 == 0:
        if year_div_100 == 0:
            if year_div_400 == 0:
                is_leap_year = True
            else:
                is_leap_year = False
        elif year_div_100 != 0:
            is_leap_year = True
    
    return is_leap_year


def is_valid_date(month, date, year):
    month = int(month)
    date = int(date)
    year = int(year)

    if year < 1000 or year > 9999:
        return False

    if month != 2 and month < 13:
        return ls[month] >= date
    
    elif month == 2 and month < 13:
        if is_leap_year(year):
            return ls[month] >= date
        elif not is_leap_year(year):
            return ls[month] - 1 >= date     

    else:
        return False

            
def get_days_in_month(month, year):
    if month != 2:
        return ls[month]
    
    elif month == 2:
        if is_leap_year(year):
            return ls[month]
        else:
            return ls[month] - 1


def determine_day(detailed_date):
    if is_correct_date_format(detailed_date):
        month = int(detailed_date[0:2])
        date = int(detailed_date[3:5])
        year = int(detailed_date[6:10])
        
        if is_valid_date(month, date, year):
            key = find_key(year)
            days = days_from_start(month, date, key)
            start_day = find_start_day_in_january(key)
            day_in_num = (days + start_day - 2) % 7
            return(day_in_num_to_letters(day_in_num))
                
        else:
            print("The date you entered is invalid.")
    
    else:
        print("Please enter your date in correct format.")


def find_start_day_of_month_2(month, year):
    start_day_in_num = find_start_day_of_month(month, year)
    print(day_in_num_to_letters(start_day_in_num))


def draw_month(month, year):
    days_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    months_of_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    days_of_week_str = '   '.join(days_of_week)
    start_day = find_start_day_of_month(month, year)
    last_day = get_days_in_month(month, year)
    print(months_of_year[month - 1], year)
    print(days_of_week_str)
    print((start_day)*6 * ' ', end = '')
    for i in range(1, get_days_in_month(month, year) + 1):

        if i <= 9:
            print('  ' + str(i), end = '   ')

        elif i >= 10:
            print(' ' + str(i), end = '   ')

        if (start_day + 1) % 7 == 0 and i != last_day:
            print('\n')

        start_day += 1
    print('\n')    


def draw_year(year):
    for i in range(0, 12):
        draw_month(i + 1, year)
        print('\n')
        print('\n')


# DRIVER FUNCTION
def temp():
    
    
    try:
        
        print("\n\n-----------------------------------------------------------------------------")
        print("LIST OF AVAILABLE UTILITIES: --\n")
        print("* ENTER 1  --->  CHECK A GIVEN YEAR, TO BE A 'LEAP' OR NOT! [FORMAT: YYYY]")
        print("* ENTER 2  --->  CHECK A DATE VALID OR NOT! [FORMAT: MM/DD/YYYY]")
        print("* ENTER 3  --->  CHECK THE NUMBER OF DAYS IN A GIVEN MONTH, OF A YEAR! [FORMAT: MM/YYYY]")
        print("* ENTER 4  --->  CHECK / DETERMINE THE DAY OF A PARTICULAR DATE! [FORMAT: MM/DD/YYYY]")
        print("* ENTER 5  --->  CHECK / DETERMINE THE STARTING DAY OF A PARTICULAR MONTH! [FORMAT: MM/YYYY]")
        print("* ENTER 6  --->  DISPLAY A PARTICULAR MONTH OF A YEAR! [FORMAT: MM/YYYY]")
        print("* ENTER 7  --->  DISPLAY THE ENTIRE YEAR GIVEN! [FORMAT: YYYY]")
        print("-----------------------------------------------------------------------------")

       
        U = int(input())
        if (U == 1):
            try:
                ij = int(input("ENTER YEAR [FORMAT: YYYY] --\t"))
                print(is_leap_year(ij))
            except:
                print("\nINVALID INPUT! PLEASE TRY AGAIN!")
                temp()

        elif (U == 2):
            try:
                ik = input("ENTER DATE [FORMAT: MM/DD/YYYY] --\t").split('/')
                print(is_valid_date(int(ik[0]), int(ik[1]), int(ik[2])))
            except:
                print("\nINVALID INPUT! PLEASE TRY AGAIN!")
                temp()

        elif (U == 3):
            try:
                ii = input("ENTER - MONTH & YEAR [FORMAT: MM/YYYY] --\t").split('/')
                print(get_days_in_month(int(ii[0]), int(ii[1])))
            except:
                print("\nINVALID INPUT! PLEASE TRY AGAIN!")
                temp()

        elif (U == 4):
            try:
                iq = input("ENTER DATE [FORMAT: MM/DD/YYYY] --\t")
                print(determine_day(iq))
            except:
                print("\nINVALID INPUT! PLEASE TRY AGAIN!")
                temp()

        elif (U == 5):
            try:
                ia = input("ENTER - MONTH & YEAR [FORMAT: MM/YYYY] --\t").split('/')
                find_start_day_of_month_2(int(ia[0]), int(ia[1]))
            except:
                print("\nINVALID INPUT! PLEASE TRY AGAIN!")
                temp()

        elif (U == 6):
            try:
                ic = input("ENTER - MONTH & YEAR [FORMAT: MM/YYYY] --\t").split('/')
                print("\n")
                draw_month(int(ic[0]),int(ic[1]))
            except:
                print("\nINVALID INPUT! PLEASE TRY AGAIN!")
                temp()
        
        elif (U == 7):
            try:
                iz = int(input("ENTER YEAR [FORMAT: YYYY] --\t"))
                print("\n")
                print(draw_year(iz))
            except:
                print("\nINVALID INPUT! PLEASE TRY AGAIN!")
                temp()
        
        else:
            print("\nINVALID INPUT! PLEASE TRY AGAIN!")
            temp()
    
    except:   
        print("\nENTER THE OPTION CORRECTLY!!")
        temp()
    
    
    U = input("\nWANT TO TRY AGAIN? PLEASE TYPE -- [YES/Y    OR    NO/N] :--\t").lower()
    
    if (U == 'yes' or U == 'y'):
        temp()
    else:
        print("\n\n~THANK YOU! ")
        exit()

print("\n                               THE CALENDAR SHOP\n                           -------------------------\n")
temp()


@ CODED BY TSG405, 2021

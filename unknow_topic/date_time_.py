import datetime

"""
d = datetime.datetime(2022, 4, 19, 12, 34)
print(d)
print(d.year, d.month, d.day)
print(d.hour, d.minute)

# d.year = 2023
# print(d.year)

######################################################################################

date_ = datetime.date(2022, 4, 19)
print(date_)

time_ = datetime.time(16, 20)
print(time_)

#####################################################################################

today = datetime.datetime.now()
print(today)

today_ = datetime.datetime.today()
print(today_)

####################################################################################

today_date = datetime.date.today()

date_time = datetime.date(2022, 5, 19)

diff = date_time - today_date
print(diff)

##################################################################################3

today_date = datetime.date.today()
t_delta = datetime.timedelta()

# print(today_date + t_delta)

####################################################################################
today = datetime.datetime.today()
b_day = datetime.datetime(2022, 5, 12)
print(b_day - today)

#####################################################################################

date_str = "12/08/2023"
day, month, year = date_str.split("/")

print(datetime.date(int(year), int(month), int(day)))
"""
#######################################################################################

date_ = "12 July 2022"

c_date = datetime.datetime.strptime(date_, "%d %B %Y")
print(c_date)

date_ = "12 Jul, 22"
c_date = datetime.datetime.strptime(date_, "%d %b, %y").date()
print(c_date)

time_ = "2:43:52"
c_time = datetime.datetime.strptime(time_, "%H:%M:%S").time()
print(c_time)

time_ = "2:43:52 PM"
c_time = datetime.datetime.strptime(time_, "%I:%M:%S %p").time()
print(c_time)

###############################################################################################

td = datetime.datetime.today()
c_date = datetime.datetime.strftime(td, "%Y %B, %d %A")
print(c_date)

c_date = datetime.date.strftime(td, "%y %b %d, %a")
print(c_date)


c_time = datetime.datetime.strftime(td, "%I - %M - %S")
print(c_time)


td = datetime.datetime.today().time()
c_time = datetime.time.strftime(td, "%H:%M:%S %p")
print(c_time)

#############################################################################################
# class Employee - name, date of birth, salary, joining date

# check if the employee has his birthday today
# check if the employee is eligible for annual hike



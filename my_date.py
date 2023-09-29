def is_leap_year(year: int) -> bool:
    """Return True if year is a leap year, False otherwise"""
    if (year % 400 == 0):
      return True
    elif(year%4==0 and year%100!=0):
      return True
    else:
      return False

def ordinal_date(year:int , month: int, day: int) -> int:
   nonLeap=[0,31,59,90,120,151,181,212,243,273,304,334]
   leap=[0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
   days=0
   
   if(is_leap_year(year)):
    days=day+leap[month-1]
   else:
    days=day+nonLeap[month-1]

   return days


def days_elapsed(year1: int, month1: int, day1: int, year2: int, month2: int, day2:int ) -> int:
  numberdays=0

  if(year1==year2):
     if(month1==month2):
        numberdays += day2 - day1
     else:
        numberdays += ordinal_date(year2,month2,day2) - ordinal_date(year1,month1,day1) 
     return numberdays


  if(month1<month2):
    while(year1<=year2-1):
        if(is_leap_year(year1)):
              numberdays+=366
        else:
              numberdays+=365
        year1+=1

    numberdays+=ordinal_date(year2,month2,day2)-ordinal_date(year1,month1,day1)

  else:
              
    while(year1<=year2-2):
        if(is_leap_year(year1)):
            numberdays+=366
        else:
            numberdays+=365
        year1+=1
          
    if(is_leap_year(year1)):
        numberdays+=366-ordinal_date(year1,month1,day1)+ordinal_date(year2,month2,day2)
    else:
        numberdays+=365-ordinal_date(year1,month1,day1)+ordinal_date(year2,month2,day2)      

        
  return numberdays




# This is a tuple. It is immutable so that users can't accidentally modify it.
DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def day_of_week(year: int, month: int, day: int) -> str:
   
   y1 = 1753
   m1 = 1
   d1 = 1
   daysTill=days_elapsed(y1,m1,d1,year,month,day)
   index = (daysTill+0)%7
   return DAYS_OF_WEEK[index]



def to_str(year: int, month: int, day: int) -> str:
   
   months=["January","February","March","April","May","June","July","August","September","October","November","December"]
   presentDay=day_of_week(year,month,day)
   presentMonth=months[month-1]
   if(day>=1 and day<=9):
      day1="0"+str(day)
   else:
      day1=str(day)

   return presentDay + ", " + day1 + " " + presentMonth + " " + str(year)

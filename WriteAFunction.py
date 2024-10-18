"""
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
In the Gregorian calendar, three conditions are used to identify leap years:
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source:https://www.timeanddate.com/date/leapyear.html

Task
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

Input Format
Read year, the year to test.

Constraints
1900<= year <= 10^5
Output Format
The function must return a Boolean value (True/False). Output is handled by the provided code stub.

Sample Input 0
1990

Sample Output 0
False

Explanation 0
1990 is not a multiple of 4 hence it's not a leap year.


Gregoryen takviminde, normal bir yıl 365 günden oluşur. Bir yıldız yılının gerçek uzunluğu (Dünya'nın Güneş hakkında bir kez dönmesi için gereken süre) aslında 365.2425 gün olduğundan, üç normal (ama kısa) yılın neden olduğu hatayı ortadan kaldırmak için her dört yılda bir 366 günlük bir "artık yıl" kullanılır. 4 ile eşit bölünebilen herhangi bir yıl artık yıldır: örneğin, 1988, 1992 ve 1996 artık yıllardır.

Ancak, yine de hesaba katılması gereken küçük bir hata vardır. Bu hatayı ortadan kaldırmak için, Gregoryen takvimi, 100 ile eşit olarak bölünebilen bir yılın (örneğin, 1900) artık yıl olduğunu, ancak 400 ile de eşit olarak bölünebilir olmasını şart koşar.

Bu nedenle, aşağıdaki yıllar artık yıl değildir:

1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600

Bunun nedeni, 100 ile eşit olarak bölünebilmeleri, ancak 400 ile bölünememeleridir.

Aşağıdaki yıllar artık yıllardır: 1600, 2000, 2400

Bunun nedeni, 100 ve 400 ile eşit olarak bölünebilmeleridir.
"""
def is_leap(year):
    leap = False
    
    if((year % 4 == 0) and (year % 100 != 0)):
        leap = True
    elif(year % 400 == 0):
        leap=True
   
    return leap
year = int(input())
print(is_leap(year))
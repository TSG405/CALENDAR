<h1>PYTHON -- CALENDAR Module 📅</h1>

<h2>Compatibility </h2>
  Python (3.x)+

<H2>Usage Ex -------- :</h2>


The Utility Functions are already clarified inside the main scipt. These illustrations will, further help in utilzing the functions seperately, using -- command line / python-shell.

<h4>is_leap_year(year)</h4>
<pre>
>>> is_leap_year(2008) 
True
>>> is_leap_year(1601)
False 
</pre>

<h4>is_valid_date(month, date, year)</h4>
<pre>
>>> is_valid_date(2, 31, 2019)
False
>>> is_valid_date(7, 31, 2039)
True
</pre>

<h4>get_days_in_month</h4>
<pre>
>>> get_days_in_month(2, 2015)
29
>>> get_days_in_month(10, 1909)
31
</pre>

<h4>determine_day('mm/dd/yyyy')</h4>
<pre> 
>>> determine_day('07/06/1990')  
Friday
>>> determine_day('01/01/2039')
Saturday
</pre>

<h4>find_start_day_of_month(month, year)</h4>
<pre>
>>> find_start_day_of_month(12, 1964)  # The first day of December in 1964 was the 2nd.
2  
</pre>

<h4>find_start_day_of_month_2(month, year)</h4>
<pre>
>>> find_start_day_of_month_2(12, 1964)  # same functionality as find_start_day_of_month(month, year) but faster & Optimal
2
</pre>

<h4>draw_month(month, year)</h4>
Note: This function does NOT return a value. It just prints a user-friendly visual of the specified month in the command line.
<pre>
>>> draw_month(7, 1995)



July 1995
Sun   Mon   Tue   Wed   Thu   Fri   Sat
                                      1   

  2     3     4     5     6     7     8   

  9    10    11    12    13    14    15   

 16    17    18    19    20    21    22   

 23    24    25    26    27    28    29   

 30    31  
</pre>

<h4>draw_year(year)</h4>
Note: This function does NOT return a value. It just prints a user-friendly visual of the specified year's calendar in the command line.
<pre>
>>> draw_year(2009)



January 2009
Sun   Mon   Tue   Wed   Thu   Fri   Sat
                          1     2     3   

  4     5     6     7     8     9    10   

 11    12    13    14    15    16    17   

 18    19    20    21    22    23    24   

 25    26    27    28    29    30    31   



February 2009
Sun   Mon   Tue   Wed   Thu   Fri   Sat
  1     2     3     4     5     6     7   

  8     9    10    11    12    13    14   

 15    16    17    18    19    20    21   

 22    23    24    25    26    27    28   



March 2009
Sun   Mon   Tue   Wed   Thu   Fri   Sat
  1     2     3     4     5     6     7   

  8     9    10    11    12    13    14   

 15    16    17    18    19    20    21   

 22    23    24    25    26    27    28   

 29    30    31   



April 2009
Sun   Mon   Tue   Wed   Thu   Fri   Sat
                    1     2     3     4   

  5     6     7     8     9    10    11   

 12    13    14    15    16    17    18   

 19    20    21    22    23    24    25   

 26    27    28    29    30   



May 2009
Sun   Mon   Tue   Wed   Thu   Fri   Sat
                                1     2   

  3     4     5     6     7     8     9   

 10    11    12    13    14    15    16   

 17    18    19    20    21    22    23   

 24    25    26    27    28    29    30   

 31   



June 2009
Sun   Mon   Tue   Wed   Thu   Fri   Sat
        1     2     3     4     5     6   

  7     8     9    10    11    12    13   

 14    15    16    17    18    19    20   

 21    22    23    24    25    26    27   

 28    29    30   



July 2009
Sun   Mon   Tue   Wed   Thu   Fri   Sat
                    1     2     3     4   

  5     6     7     8     9    10    11   

 12    13    14    15    16    17    18   

 19    20    21    22    23    24    25   

 26    27    28    29    30    31   



August 2009
Sun   Mon   Tue   Wed   Thu   Fri   Sat
                                      1   

  2     3     4     5     6     7     8   

  9    10    11    12    13    14    15   

 16    17    18    19    20    21    22   

 23    24    25    26    27    28    29   

 30    31   



September 2009
Sun   Mon   Tue   Wed   Thu   Fri   Sat
              1     2     3     4     5   

  6     7     8     9    10    11    12   

 13    14    15    16    17    18    19   

 20    21    22    23    24    25    26   

 27    28    29    30   



October 2009
Sun   Mon   Tue   Wed   Thu   Fri   Sat
                          1     2     3   

  4     5     6     7     8     9    10   

 11    12    13    14    15    16    17   

 18    19    20    21    22    23    24   

 25    26    27    28    29    30    31   



November 2009
Sun   Mon   Tue   Wed   Thu   Fri   Sat
  1     2     3     4     5     6     7   

  8     9    10    11    12    13    14   

 15    16    17    18    19    20    21   

 22    23    24    25    26    27    28   

 29    30   



December 2009
Sun   Mon   Tue   Wed   Thu   Fri   Sat
              1     2     3     4     5   

  6     7     8     9    10    11    12   

 13    14    15    16    17    18    19   

 20    21    22    23    24    25    26   

 27    28    29    30    31   
</pre>

<h2>How leap years are calculated :</h2>
<blockquote>"The Gregorian calendar, the current standard calendar in most of the world, adds a 29th day to February in all years evenly divisible by 4, except for centennial years (those ending in -00) which are not evenly divisible by 400. Thus 1600, 2000 and 2400 area leap years but 1700, 1800, 1900, 2200 and 2300 are not." - Roger C.</blockquote>
 
 
### TSG405

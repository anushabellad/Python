# -*- coding: utf-8 -*-
"""Python 1_Anusha Bellad.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15YneN8DrwAdHCukU89JN_S9wCDpQo9k-
"""

#Temperature conversion.

temperature = 15
temp_in_F = temperature*(9/5) + 32
print(temp_in_F)


#function to find if the year is leap or not.

def leap_year(year):
       if ((year%4 == 0  and year% 100 != 0) or year%400 ==0 ):
              print ('Its a leap year.')
       else :
              print ('Its not a leap year.')

year = int( input('Please enter the year to be checked.'))
leap_year(year)



#function to convert height from inches to cm.

def height_cm (height_in):
  print ('Height in cm =', height_in*2.54)

height_cm(height_in = int(input('Please enter the height in inch.')))
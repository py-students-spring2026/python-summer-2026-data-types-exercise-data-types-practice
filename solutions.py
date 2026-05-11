"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""

def calculate_profit():
  """
  Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales. 
  Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.  
  You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
  The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
  """
  sales = input("Enter projected total sales: ")
  try:
    profit = float(sales) * 0.23
    profit = format(profit, ',.2f')
    print(f'Profit: ${profit}')
  except ValueError:
    print("Invalid input. Only numeric values accepted.")

def calculate_quotient_and_remainder():
  """
  Complete this function so that it asks the user to input two integers. 
  You program should calculate and output the quotient and remainder when the first number is divided by the second.
  Here's an example run of the function: 
    Enter number #1: 5
    Enter number #2: 2
    2 goes into 5 a total of 2 times with a remainder of 1
  """
  num1 = input('Enter number #1: ')
  num2 = input('Enter number #2: ')
  try:
    num1 = int(num1)
    num2 = int(num2)
    quotient = int(num1 / num2)
    remainder = int(num1 % num2)
    print(f'{num2} goes into {num1} a total of {quotient} times with a remainder of {remainder}')
  except ValueError:
    print("Invalid input. Only integer values accepted.")

def calculate_miles_per_gallon():
  """
  A car's Miles Per Gallon (MPG) can be calculated using the following formula: 
    MPG = Miles driven / Gallons of Gas Used
  Complete this function so that it asks the user for the number of miles driven and the gallons of gas used. 
  It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

    Miles driven: 100
    Gas used (gallons): 25
    Miles per gallon: 2.2
  """
  miles = input('Enter miles driven: ')
  gas = input('Enter gallons of gas used: ')
  try:
    miles = int(miles)
    gas = int(gas)
    mpg = miles / gas
    mpg = format(mpg, '.1f')
    print(f'Miles per gallon: {mpg}')
  except ValueError:
    print("Invalid input. Only integer values accepted.")

def align_text():
  """
  Complete this function such that it asks the user to enter in 3 price values (as floating point numbers). 
  The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
  Here's a sample running of the program:

    Enter price #1: 1.55
    Enter price #2: 10
    Enter price #3: 9532.6

    Here are your prices!

    Price #1: $    1.55
    Price #2: $   10.00
    Price #3: $ 9532.60
  """
  price1 = input('Enter price #1: ')
  price2 = input('Enter price #2: ')
  price3 = input('Enter price #3: ')
  try:
    price1 = float(price1)
    price2 = float(price2)
    price3 = float(price3)
    price1 = format(price1, '>8.2f')
    price2 = format(price2, '>8.2f')
    price3 = format(price3, '>8.2f')
    print('\nHere are your prices!')
    print(f'Price #1: ${price1}')
    print(f'Price #2: ${price2}')
    print(f'Price #3: ${price3}')
  except ValueError:
    print("Invalid input. Only numeric values accepted.")

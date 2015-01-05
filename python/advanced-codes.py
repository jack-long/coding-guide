## -- char in string --
phrase = "A bird in the hand..."

for char in phrase:
    if char in ['A', 'a']:
        print 'X',
    else:
        print char ,
print

## -- string.format -- ##
parents, babies = (1, 1)
while babies < 100:
    print 'This generation has {0} babies'.format(babies)
    parents, babies = (babies, parents + babies)

## -- enumerate --
'''
A weakness of using this for-each style of iteration is that 
you don't know the index of the thing you're looking at. 
At times it is useful to know how far into the list you are. 
Thankfully the built-in enumerate function helps with this.

enumerate works by supplying a corresponding index to 
each element in the list that you pass it. (starts from 0 )
Each time you go through the loop, index will be one greater, 
and item will be the next item in the sequence. 
It's very similar to using a normal for loop with a list, 
except this gives us an easy way to count how many items we've seen so far.
'''
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index + 1, item
    
## -- zip --
'''
It's also common to need to iterate over two lists at once. 
This is where the built-in zip function comes in handy.

zip will create pairs of elements when passed two lists, 
and will stop at the end of the shorter list.

zip can handle three or more lists as well!
'''
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    if a > b:
        print a
    else:
        print b

## -- while-else / for-else -- ##

## LuckyNumbers
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"

'''       
Just like with while, for loops may have an else associated with them.
The else statement is executed after the for, but only if the for ends 
normally — that is, not with a break. 
This code will break when it hits 'tomato', so the else block won't be 
executed.
'''
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'
    
## -- get reverse --
>>> text
'this@is#a$sentence!'
>>> text[::-1]
'!ecnetnes$a#si@siht'

## -- List Buildup --
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

## -- lambda --
garbled = '''IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt \
mXXeXsXXXsXaXXXXXXgXeX!XX'''
message = filter(lambda x: x != 'X', garbled)
print message

## -- command-line arguements --
# This program adds up integers in the command line
import sys
try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print 'sum =', total
except ValueError:
    print 'Please supply integer argument'

## time, localtime, time.tm_hour ##
from time import localtime

activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting'}

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print activities[activity_time]
        break
    else:
        print 'Unknown, AFK for sleeping!'

## --- Bitwise Operations --- ##
'''
Note that you can only do bitwise operations on an integer. 
Trying to do them on strings or floats will result in nonsensical output!
'''
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT

print 0b1001
print 0B1001

print 0o11
print 0O11

print 0x11
print 0X11

'''
Python has an int() function that can turn non-integer input into an integer.
When given a string containing a number and the base that number is in, 
the function will return the value of that number converted to base 10.

bin() takes an integer as input and returns the binary representation of that 
integer in a string. (Keep in mind that after using the bin function, 
you can no longer operate on the value like a number.)

You can also represent numbers in base 8 and base 16 using the oct() and hex() 
functions.
'''

'''
In the example below, we want to see if the third bit from the right is on.

First, we first create a variable num containing the number 12, or 0b1100.
Next, we create a mask with the third bit on.
Then, we use a bitwise-and operation to see if the third bit from the right 
of num is on.
If desired is greater than zero, then the third bit of num must have been one.
'''
num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
    print "Bit was on"
    
'''
Turn a bit ON 
You can also use masks to turn a bit in a number on using |.
'''
a = 0b110 # 6
mask = 0b1 # 1
desired =  a | mask # 0b111, or 7

'''Flip

Using the XOR (^) operator is very useful for flipping bits. 
Using ^ on a bit with the number one will return a result where that bit is 
flipped.
'''
a = 0b110 # 6
mask = 0b111 # 7
desired =  a ^ mask # 0b1

'''
You can also use the left shift (<<) and right shift (>>) operators to slide 
masks into place.
'''
def flip_bit(number, n):
    result = number ^ 0b1 << (n-1)
    return bin(result)

## --- File I/O --- ##

'''File I/O

You may not know this, but file objects contain a special pair of built-in 
methods: __enter__() and __exit__(). The details aren't important, but 
what is important is that when a file object's __exit__() method is invoked, 
it automatically closes the file. How do we invoke this method? 
With with and as.
'''
with open("text.txt", "w") as textfile:
    textfile.write("Success!")
    

## --- Web 2.0 --- ##

'''RESTful

For an API or web service to be RESTful, it must do the following:
1) Separate the client from the server
2) Not hold state between requests (meaning that all the information 
    necessary to respond to a request is available in each individual request; 
    no data, or state, is held by the server from request to request)
3) Use HTTP and HTTP methods.
'''

from urllib2 import urlopen

kittens = urlopen("http://placekitten.com/")
response = kittens.read()
print response[559:1000]

'''
# GET: retrieves information from the specified source.
# POST: sends new information to the specified source.
# PUT: updates existing information of the specified source.
# DELETE: removes existing information from the specified source.
'''

import requests

kittens = requests.get("http://placekitten.com/")
print kittens.text[559:1000]


########## Example request #############
# POST /learn-http HTTP/1.1
# Host: www.codecademy.com
# Content-Type: text/html; charset=UTF-8
# Name=Eric&Age=26

import requests

body = {'Name': 'Eric', 'Age': '26'}
response = requests.post("http://codecademy.com/learn-http/", data=body)

'''
HTTP Status Codes work like this:

1xx: You won't see these a lot. The server is saying, 
     "Got it! I'm working on your request."

2xx: These mean "okay!" 
     The server sends these when it's successfully responding to your request.

3xx: These mean "I can do what you want, but I have to do something else first." 
     You might see this if a website has changed addresses and you're using the old one; 
     the server might have to reroute the request before it can get you the resource you asked for.

4xx: These mean you probably made a mistake. 
     The most famous is "404," meaning "file not found": you asked for a 
     resource or web page that doesn't exist.

5xx: These mean the server goofed up and can't successfully respond to your request.
'''
## -- class -- ##
class BankAccount(object):
    def __init__(self, initial_balance = 0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def overdrawn(self):
        return self.balance < 0
my_account = BankAccount(15)
my_account.withdraw(5)
print my_account.balance

## -- re -- ##
def patten_check(test_string)
    """re demo
    
    r'^\d{3}-\d{4}$'
    """
    import re
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print test_string, 'is a valid US local phone number'
    else:
        print test_string, 'rejected'

## -- formatted print --##

prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {'apple': 1, 'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit] for fruit in my_purchase)
print 'I owe the grocer $%.2f' % grocery_bill

REFRAIN = '''
%d bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!
'''
bottles_of_beer = 99
while bottles_of_beer > 1:
    print REFRAIN % (bottles_of_beer, bottles_of_beer, bottles_of_beer - 1)
    bottles_of_beer -= 1

## -- Conditionals & Control Flow -- ##
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower() #lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()        ## !!!

''' Boolean operators

not is evaluated first;
and is evaluated next;
or is evaluated last.
'''
# -- Function Arguments --
def biggest_number(*args):      # list
    print max(args)
    return max(args)

def distance_from_zero(arg):
    if type(arg) == int or type(arg) == float:  # type()
        return abs(arg)
    else:
        return "Nope"

biggest_number(-10, -5, 5, 10)
distance_from_zero(-10)


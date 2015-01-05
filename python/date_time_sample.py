#! /usr/bin/env python
# coding=utf-8

'''Memo for date and time.

There are two modules for time management: time and datetime.
If you need to Wait seconds, use time.sleep(seconds).
'strftime' is used to convert Time to String.
'strptime' is used to convert String to Time.

The format rule is as follows:
%a: Weekday as locale’s abbre- viated name. Example:Sun, Mon, ..., Sat (en_US)
%A: Weekday as locale’s full name.
%w: Weekday as a decimal number, where 0 is Sunday.
%d: Day of the month as a zero-padded decimal num- ber. Example: 02.
%b: Month as locale’s abbrevi- ated name. Example: Jan, Feb, ..., Dec (en_US)
%B: Month as locale’s full name.
%m: Month as a zero-padded decimal number. Example: 02
%y: Year without century as a zero-padded decimal num- ber.
%Y: Year with century as a dec- imal number.
%H: Hour (24-hour clock) as a zero-padded decimal num- ber.
%I: Hour (12-hour clock) as a zero-padded decimal num- ber.
%p: Locale’s equivalent of ei- ther AM or PM. Example: AM, PM (en_US)
%M: Minute as a zero-padded decimal number.
%S: Second as a zero-padded decimal number.
%j: Day of the year as a zero-padded decimal number.
'''

import time
import datetime

print "dir(time):"
print dir(time), '\n'
print "dir(datetime):"
print dir(datetime), '\n'

print "date \n======================"
print "time.localtime():", time.localtime(), '\n'
print "strftime():", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print "datetime.date.today():", datetime.date.today(),
print "type:", type(datetime.date.today())
print "datetime.date.today().isoformat():", datetime.date.today()
print "datetime.date.today().strftime('%Y年%m月%d日'):",
print datetime.date.today().strftime('%Y年%m月%d日')
print
print "Convert String to Time.struct_time (a tuple):"
print "time.strptime(string, format):",
print time.strptime("2014-5-1", "%Y-%m-%d")
print 
print "Convert String to Datetime.datetime Object:"
print "datetime.datetime.strptime(string, format):",
print datetime.datetime.strptime("2014-5-1", "%Y-%m-%d")
print
print "datetime \n=================="
now = datetime.datetime.now()
print "now = datetime.datetime.now()"
print "now:",type(now)
print "now.time():", type(now.time())
print "now.date():", type(now.date())

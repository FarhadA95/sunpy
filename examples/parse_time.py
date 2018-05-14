"""
================================================
Parsing times with sunpy.time.parse_time
================================================

Example to show some example usage of parse_time
"""
##############################################################################
# Import the required modules
from datetime import datetime, date
import time

import numpy as np
import pandas

# Import parse_time
from sunpy.time import parse_time


##############################################################################
# Suppose you want to parse of strings, parse_time can do that.
t1 = parse_time('1995-12-31 23:59:60')

##############################################################################
# Ofcourse you could do the same with astropy Time.
# But SunPy parse_time can parse even more time formats
t2 = parse_time('1995-Dec-31 23:59:60')
# As you see from the above examples, thanks to astropy Time, parse_time
# can handle leap seconds too.

##############################################################################
# You can mention the scale of the time as keyword parameter if you need
# Similar to scale you can pass in any astropy Time compatible keywords to
# parse_time. See all arguments here: http://docs.astropy.org/en/stable/time/#creating-a-time-object
t3 = parse_time('2012:124:21:08:12', scale='tai')


##############################################################################
# Now that you are done with strings, let's see other type parse_time handles,
# tuples
# astropy Time doesnot handle tuples but parse_time does
t4 = parse_time((1998, 11, 14))
t5 = parse_time((2001, 1, 1, 12, 12, 12, 8899))

##############################################################################
# This also means that you can parse a time struct.
t6 = parse_time(time.localtime())

##############################################################################
# parse_time also parses datetime and date objects
t7 = parse_time(datetime.now())
t8 = parse_time(date.today())


##############################################################################
# parse_time can return Time objects for pandas.Timestamp, pandas.Series
# and pandas.DatetimeIndex
t9 = parse_time(pandas.Timestamp(datetime(1966, 2, 3)))

t10 = parse_time(
    pandas.Series([[datetime(2012, 1, 1, 0, 0),
                    datetime(2012, 1, 2, 0, 0)],
                   [datetime(2012, 1, 3, 0, 0),
                    datetime(2012, 1, 4, 0, 0)]]))

t11 = parse_time(
    pandas.DatetimeIndex([
        datetime(2012, 1, 1, 0, 0),
        datetime(2012, 1, 2, 0, 0),
        datetime(2012, 1, 3, 0, 0),
        datetime(2012, 1, 4, 0, 0)
    ]))


##############################################################################
# parse_time can parse numpy.datetime64 objects
t12 = parse_time(np.datetime64('2014-02-07T16:47:51.008288123-0500'))
t13 = parse_time(
    np.array(
        ['2014-02-07T16:47:51.008288123', '2014-02-07T18:47:51.008288123'],
        dtype='datetime64'))

##############################################################################
# Parse time returns astropy.time.Time object for every parsable input that
# you give to it
# parse_time can handle all formats that astropy.time.Time can handle
# That is,
# ['jd', 'mjd', 'decimalyear', 'unix', 'cxcsec', 'gps', 'plot_date', 'datetime',
# 'iso', 'isot', 'yday', 'fits', 'byear', 'jyear', 'byear_str', 'jyear_str']
# at the time of writing. This can be used by passing format keyword argument
# to parse_time
parse_time(1234.0, format='jd')
parse_time('B1950.0', format='byear_str')

# Creates a new user
# python cuser.py <days>

import os
import sys
import time

prefix 	= "premium"
days 	= sys.argv[1]
user 	= prefix + str( int( time.time()) )

os.system( "useradd -e `date -d '" + days + " days' " + "+%Y-%m-%d" + "` " + user )
os.system( "passwd " + user )

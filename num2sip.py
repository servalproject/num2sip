#!/usr/bin/env python

import sqlite3
import sys

dbfile = '/var/lib/asterisk/sqlite3dir/sqlite3.db'
myip = '1.2.3.4'

def main():
    try:
        db = sqlite3.connect(dbfile)
    except sqlite3.OperationalError, e:
        print >>sys.stderr, "Unable to open DB \'%s\'" % (dbfile)
        sys.exit(1)

    c = db.cursor()
    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            # EOF detection is broken :(
            break
        c.execute('SELECT dial FROM dialdata_table WHERE exten = ?', (line, ))
        for r in c:
            print "sip://%s@%s" % (r[0], myip)
        print "DONE"
        
if __name__ == "__main__":
    main()


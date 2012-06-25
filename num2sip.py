#!/usr/bin/env python

import ConfigParser
import sqlite3
import sys

def main():
    if len(sys.argv) != 2:
        print >>sys.stderr, "Bad usage"
        print >>sys.stderr, "%s conffile" % (sys.argv[0])
        sys.exit(1)

    conf = ConfigParser.ConfigParser()
    if len(conf.read([sys.argv[1]])) == 0:
        print >>sys.stderr, "Unable to read configuration"
        sys.exit(1)

    if not conf.has_option('general', 'ip') or not conf.has_option('general', 'dbpath'):
        print >>sys.stderr, "Configuration file doesn't have ip and dbpath"
        sys.exit(1)
    myip = conf.get('general', 'ip')
    dbpath = conf.get('general', 'dbpath')

    try:
        db = sqlite3.connect(dbpath)
    except sqlite3.OperationalError, e:
        print >>sys.stderr, "Unable to open DB \'%s\'" % (dbpath)
        sys.exit(1)

    c = db.cursor()
    print "STARTED"
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


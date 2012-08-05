Create a dummy database with...
rm -f test.db
sqlite3 test.db <<EOF
CREATE TABLE dialdata_table (
       dial TEXT,
       exten TEXT);

INSERT INTO dialdata_table VALUES ('IMSI87654321', '12341234');
EOF

Test with..
echo 'foo|12345678|' | ./num2sip.py ./num2sip.ini

Output should be as follows..
[Ur 14:07] ~/projects/serval/num2sip >echo 'foo|12341234|' | ./num2sip.py ./num2sip.ini
STARTED
foo|sip://IMSI87654321@1.2.3.4|12341234||
DONE

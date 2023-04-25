# Web-Vulnerabilities

These attacks were performed on websites and servers made for the purpose. Consent was given.

SQL Injection Attacks

The sql[012] files demonstrate sql injection attacks with varying levels of input sanitization, such as escaping single quotes. The server corresponding to the sql2 files escapes the username and hashes the password with md5.

POST Request Web Attacks

The bsf[0123] files create an HTML form with the desired login credentials. bsf 1-3 exploit the logged-in user’s token while bsf2 sends the user’s token to a remote spy server.

URL-Based Web Attacks

The XSS[0-3] files, only through links, send the user’s username and first search on the victim website to the spy server, each file completes this task with different levels of input sanitization, such as removing ‘script’ tags.

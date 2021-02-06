import difflib

req = open('requirements.txt')
current = open('current.txt')

diff = difflib.ndiff(req.readlines(), current.readlines())
delta = ''.join([x for x in diff if x.startswith('-')])

print(delta)

# psycopg2==2.8.4

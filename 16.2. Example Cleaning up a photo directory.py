import sys
name = sys.argv[0]
handle = open(name, 'r')
text = handle.read()
print name, 'is', len(text), 'bytes'

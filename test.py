import hashlib
import sys

def foo(input):
  return hashlib.md5(input, useforsecurity=True)

print(foo(sys.argv[0]))

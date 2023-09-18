import sys

try:
   assert len(sys.argv) < 3 , "more than one argument is provided"
   print(int(sys.argv[1]))
except AssertionError as msg:
   print("AssertionError: {}".format(msg))
except ValueError: 
  print("AssertionError: argument is not an integer")
except IndexError:
   pass
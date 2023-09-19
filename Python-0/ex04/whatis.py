import sys

try:
    assert len(sys.argv) < 3, "more than one argument is provided"
    print(f"I'm {'Even.' if int(sys.argv[1]) % 2 == 0 else 'Odd.' }")
except AssertionError as msg:
    print("AssertionError: {}".format(msg))
except ValueError:
    print("AssertionError: argument is not an integer")
except IndexError:
    pass
except KeyboardInterrupt:
    pass

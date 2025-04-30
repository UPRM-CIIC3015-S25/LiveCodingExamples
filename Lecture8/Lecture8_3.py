# UPRM CIIC 3015 Spring 2025
# Lecture 8: Files and Exceptions

# Live Coding Example 8_3


def file_open_exception_example():
  while True:
    filename = input('Enter filename: ')
    try:
      file = open(filename, 'r')
      break
    except FileNotFoundError:
      print("File not found")
      continue
    # Do something with file

# file_open_exception_example()

def f3():
  try:
    raise Exception('Raised by f3')
  except Exception as e:
    print(f'Catched in f3: {e.args}')
    raise Exception('Raised by f3')


def f2():
  # try:
    f3()
  # except Exception as e:
  #   print(f'Catched in f2: {e.args}')
  #   raise Exception('Raised by f2')


def f1():
  try:
    f2()
  except Exception as e:
    print(f'Catched in f1: {e.args}')

f1()
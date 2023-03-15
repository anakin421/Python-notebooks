import sys

sys.path.append("/home/abhishek/python notebooks/the_packages")

from package_b import b
# from package_b import *
# import sys

# print(sys.path)


def call_b():
    b.display()


call_b()

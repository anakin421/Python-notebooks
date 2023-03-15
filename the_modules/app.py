# import fibo

# import_fibo_imp_note = """
# This does not enter the names of the functions defined in fibo directly in the current symbol table;
# it only enters the module name fibo there.
# Using the module name you can access the functions:
# """

# print(
#     f"MOST IMP NOTE FOR import fibo: \n{import_fibo_imp_note.upper()}")

# print(f" calling the fib function from fibo module: {fibo.fib(100)}")

# print(f" calling the fib2 function from fibo module: {fibo.fib2(1000)}")

# print(f"The name of the fibo module is: {fibo.__name__}")

# print(f"Name of app module is: {__name__}")

# # If you intend to use a function often you can assign it to a local name
# fib = fibo.fib

# print(f" calling the fib function from fibo module with new name: {fib(1000)}")

# =========================================using from import============================================================
# from fibo import fib, fib2

# from_fibo_import_imp_note = """
# This does not introduce the module name from which the imports are taken in the local symbol table
# (so in the example, fibo is not defined).
# """

# print(
#     f"MOST IMP NOTE FOR from fibo import fib, fib2: \n{from_fibo_import_imp_note.upper()}")

# print(f" calling the fib function from fibo module: {fib(1000)}")

# print(f" calling the fib2 function from fibo module: {fib2(1000)}")


# ==========================================from fibo import *==========================================================

# from fibo import *

# import_star_imp_note = """
# This imports all names except those beginning with an underscore (_).
# In most cases Python programmers do not use this facility
# since it introduces an unknown set of names into the interpreter,
# possibly hiding some things you have already defined.
# """

# print(
#     f"MOST IMP NOTE FOR import fibo: \n{import_star_imp_note.upper()}")

# fib(500)

# =====================================import fibo as fib===============================================================

# import fibo as fib

# print("""
# This is effectively importing the module in the same way that import fibo will do,
# with the only difference of it being available as fib.
# """)

# fib.fib(500)

# Modules, packages and imports #######################################

# import calc as calculator
# a = 10
# b = 20
 
# addition = calculator.add(a,b)
# print(addition)

# from calc import *
# a = 100
# b = 30
 
# print(div(a,b))
# print(add(a,b))
# print(sub(a,b))
# print(prod(a,b))

# Python Module Path ########################################

# import sys 
# print(sys.path)

# help('modules')         # list of all the modules in python

# if __name__ == "__main__" magic ######################################
# code that should only run when your file is executed as a script.

# echo.py

# def echo(text: str, repetitions: int = 3) -> str:
#     """Imitate a real-world echo."""
#     echoed_text = ""
#     for i in range(repetitions, 0, -1):
#         echoed_text += f"{text[-i:]}\n"
#     return f"{echoed_text.lower()}."


# if __name__ == "__main__":

#     text = input("Yell something at a mountain: ")
#     print(echo(text))

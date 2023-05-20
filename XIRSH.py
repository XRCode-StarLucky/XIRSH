try:
    import os,sys,traceback
except ModuleNotFoundError:
    print("You must install os,sys and traceback Module!!!")
while True:
    pwd = os.getcwd()
    ui = input(pwd + ">")

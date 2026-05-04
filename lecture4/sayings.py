#my own module
def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":
    main()

"""
    __name__ : special sympol in python, whish is a special variable whose value is automatically
        set by python to be "main" when I run a file from the command line 
        as i running (python say2.py)
"""
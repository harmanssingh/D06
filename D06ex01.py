import os

def accesspython():
    os.chdir('C:\\Users\\Harman\\D05')
    filedir=os.listdir(os.getcwd())
    for s in filedir:
        if s.endswith('py'):
            print(s)

def main():
    accesspython()

if __name__ == '__main__':
    main()

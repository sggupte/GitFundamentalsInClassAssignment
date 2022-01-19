def interface():
    while(True):
        print("My Program")
        print("Options:")
        print("0 - HDL Analysis")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            return
        elif choice=='0':
            printHDLResults()
            return

def enterHDL():
    hdl = int(input("Please input your HDL: "))
    return hdl

def check_HDL(hdl):
    if hdl >= 60:
        return "Normal"
    elif hdl < 40:
        return "Low"
    else:
        return "Borderline Low"

def driver():
    hdl = enterHDL()
    status = check_HDL(hdl)
    return status

def printHDLResults():
    print(driver())

interface()
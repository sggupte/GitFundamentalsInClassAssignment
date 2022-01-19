def interface():
    while(True):
        print("My Program")
        print("Options:")
        print("0 - HDL Analysis")
        print("1 - LDL Analysis")
        print("2 - Total Analysis")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            return
        elif choice=='0':
            printHDLResults()
            return
        elif choice =='1':
            printLDLResults()
            return
        elif choice == '2':
            printTotalResults()
            return

def enter():
    value = int(input("Please input your values: "))
    return value

def check_HDL(hdl):
    if hdl >= 60:
        return "Normal"
    elif hdl < 40:
        return "Low"
    else:
        return "Borderline Low"

def driver_HDL():
    hdl = enter()
    status = check_HDL(hdl)
    return status

def printHDLResults():
    print(driver_HDL())

def check_LDL(ldl):
    if ldl < 130:
        return "Normal"
    elif ldl < 160 and ldl >= 130:
        return "Borderline High"
    elif ldl < 190 and ldl >= 160:
        return "High"
    else:
        return "Very High"

def driver_LDL():
    ldl= enter()
    status = check_LDL(ldl)
    return status

def printLDLResults():
    print(driver_LDL())

def check_total(total):
    if total < 200:
        return "Normal"
    elif total >= 240:
        return "High"
    else:
        return "Borderline High"

def driver_total():
    total = enter()
    status = check_total(total)
    return status

def printTotalResults():
    print(driver_total())

interface()
while True:
    millisec=input("This program converts milliseconds into hours, minutes, and seconds. Enter the milliseconds (should be greater than zero):")
    try:
        val = int(millisec)
        if val >= 0:
            break
        else:
            print("Millisec can't be negative, try again")
    except ValueError:
            print("Millisec must be a number, try again")
def millisecond_converter(millisec):
    value = int(millisec)
    if value < 1000:
        return f"just {value} millisecond/s"
    else:
        hour = value // 3600000
        
        minute = (value - (hour * 3600000)) // 60000
           
        second = (value - (hour * 3600000) - (minute * 60000)) // 1000
            
        if hour and minute and second:
            return f"{hour} hour/s {minute} minute/s {second} second/s"
        elif hour:
            return f"{hour} hour/s"
        elif minute and second:
            return f"{minute} minute/s {second} second/s"
        elif minute:
            return f"{minute} minute/s"
        elif second:
            return f"{second} second/s" 
            
print(millisecond_converter(millisec))
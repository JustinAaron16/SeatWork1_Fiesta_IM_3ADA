
while(True):
    str=input("Enter dollar($)(* to exit): ")

    if str=="*":
        print("Bye")
        break;
    
    dollar = [float(x) for x in str.split("@")]

    def convert(value):
        return(value, value*88.09, value*0.73, value* 7.12) 
            
    print("Dollar($)    Indian Rupee(R)     British(Pound)      China(Y)")

    for x in dollar:
        usd, rpe, pnd, yn = convert(x)
        print(f"{usd}            {rpe}               {pnd}               {yn}")
        print()
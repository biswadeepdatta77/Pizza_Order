print("Welcome to Python Pizza Deliveries")
size = input("What size do you want? Type S for small, M for medium and L for Large")
pep = input("Do you want extra pepporoni? Type Y for yes and N for no")
cheese = input("Do you want extra cheese? Type Y for yes and N for no")
if(size=='S'):
    if pep=='Y':
        if(cheese=='Y'):
            bill = 15+2+1
            print("Your bill is $ "+ str(bill))
        if cheese=='N':
            bill = 15+2
            print("Your bill is $ "+ str(bill))
    if pep=='N':
        if(cheese=='Y'):
            bill = 15+1
            print("Your bill is $ "+ str(bill))
        if(cheese=='N'):
            bill = 15
            print("Your bill is $ "+ str(bill))

if(size=='M'):
    if pep=='Y':
        if(cheese=='Y'):
            bill = 20+3+1
            print("Your bill is $ "+ str(bill))
        if cheese=='N':
            bill = 20+3
            print("Your bill is $ "+ str(bill))
    if pep=='N':
        if(cheese=='Y'):
            bill = 20+1
            print("Your bill is $ "+ str(bill))
        if(cheese=='N'):
            bill = 20
            print("Your bill is $ "+ str(bill))


if(size=='L'):
    if pep=='Y':
        if(cheese=='Y'):
            bill = 25+3+1
            print("Your bill is $ "+ str(bill))
        if cheese=='N':
            bill = 25+3
            print("Your bill is $ "+ str(bill))
    if pep=='N':
        if(cheese=='Y'):
            bill = 25+1
            print("Your bill is $ "+ str(bill))
        if(cheese=='N'):
            bill = 25
            print("Your bill is $ "+ str(bill))

             



year = int(input("Enter a year:    "))
#years b4 2000 formula (((all table years - input) /12) Check for whole num)
# years after 2011 formula (((input - all table years) /12) Check for whole num)
if year >= 2011:
    Dragon_Aft = (((year - 2000)/12)%1)
    Snake_Aft = (((year - 2001)/12)%1)
    Horse_Aft = (((year - 2002)/12)%1)
    Sheep_Aft = (((year - 2003)/12)%1)
    Monkey_Aft = (((year - 2004)/12)%1)
    Rooster_Aft = (((year - 2005)/12)%1)
    Dog_Aft = (((year - 2006)/12)%1)
    Pig_Aft = (((year - 2007)/12)%1)
    Rat_Aft = (((year - 2008)/12)%1)
    Ox_Aft = (((year - 2009)/12)%1)
    Tiger_Aft = (((year - 2010)/12)%1)
    Hare_Aft = (((year - 2011)/12)%1)
    if Dragon_Aft == 0:
        print("Dragon")
    elif Snake_Aft == 0:
        print("Snake")
    elif Horse_Aft == 0:
        print("Horse")
    elif Sheep_Aft == 0:
        print("Sheep")
    elif Monkey_Aft == 0:
        print("Monkey")
    elif Rooster_Aft == 0:
        print("Rooster")
    elif Dog_Aft == 0:
        print("Dog")
    elif Pig_Aft == 0:
        print("Pig")
    elif Rat_Aft == 0:
        print("Rat")
    elif Ox_Aft == 0:
        print("Ox")
    elif Tiger_Aft == 0:
        print("Tiger")
    elif Hare_Aft == 0:
        print("Hare")
elif(year<=2000):
    Dragon_B4 = (((2000 - year)/12)%1)
    Snake_B4 = (((2001 - year)/12)%1)
    Horse_B4 = (((2002 - year)/12)%1)
    Sheep_B4 = (((2003 - year)/12)%1)
    Monkey_B4 = (((2004 - year)/12)%1)
    Rooster_B4 = (((2005 - year)/12)%1)
    Dog_B4 = (((2006 - year)/12)%1)
    Pig_B4 = (((2007 - year)/12)%1)
    Rat_B4 = (((2008 - year)/12)%1)
    Ox_B4 = (((2009 - year)/12)%1)
    Tiger_B4 = (((2010 - year)/12)%1)
    Hare_B4 = (((2011 - year)/12)%1)
    if Dragon_B4 == 0:
        print("Dragon")
    elif Snake_B4 == 0:
        print("Snake")
    elif Horse_B4 == 0:
        print("Horse")
    elif Sheep_B4 == 0:
        print("Sheep")
    elif Monkey_B4 == 0:
        print("Monkey")
    elif Rooster_B4 == 0:
        print("Rooster")
    elif Dog_B4 == 0:
        print("Dog")
    elif Pig_B4 == 0:
        print("Pig")
    elif Rat_B4 == 0:
        print("Rat")
    elif Ox_B4 == 0:
        print("Ox")
    elif Tiger_B4 == 0:
        print("Tiger")
    elif Hare_B4 == 0:
        print("Hare")



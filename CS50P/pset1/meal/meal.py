def main():
    user_time = input("What time is it?")
    if user_time.endswith("p.m."):
        user_time = user_time.split(" ")
        print(user_time)
        hours, minutes = convert(user_time[0])
        hours = int(hours) + 12
    elif user_time.endswith("a.m."):
        user_time = user_time.split(" ")
        user_time = user_time[0]
        hours, minutes = convert(user_time[0])
    else:
        hours, minutes = convert(user_time)
    hours = int(hours)
    minutes = int(minutes)
    time = hours + (minutes / 60)
    time = round(time, 2)

#    match hours:
#        case 7:
#            print("breakfast time")
#        case 8 if minutes == 0:
#            print("breakfast time")
#        case 12:
#            print("lunch time")
#        case 13 if minutes == 0:
#            print("lunch time")
#        case 18:
#            print("dinner time")
#        case 19 if minutes == 0:
#            print("dinner time")
#        case _:
#            pass

    if 7 <= time <=8.01: 
        print("breakfast time")
    elif 12 <= time <= 13.01:
        print("lunch time")
    elif 18 <= time <= 19.01:
        print("dinner time")
    else:
        pass

def convert(time):
    hours, minutes = time.split(":")
    return hours, minutes

if __name__ == "__main__":
    main()

# A simple program to calculate swimmer's time to swim towards and against river stream

def print_menu():
    print("Select your choice:")
    print("1. Against Stream (Upstream) ")
    print("2. Towards Stream (Downstream)")
    print("0. Exit")
    choice = int(input())
    return choice

def upstream():
    swimmer_speed = int(input("Enter Swimmer's speed (km/h)"))
    stream_speed = int(input("Enter speed of river flow (km/h)"))
    dist = int(input("Enter distance to swim (km)"))
    effective_speed = swimmer_speed - stream_speed
    time_taken = dist/effective_speed
    print("===========RESULTS============")
    print("Effective Speed : ",effective_speed)
    print("Time needed to swim: ", time_taken)

def downstream():
    swimmer_speed = int(input("Enter Swimmer's speed (km/h)"))
    stream_speed = int(input("Enter speed of river flow (km/h)"))
    dist = int(input("Enter distance to swim (km)"))
    effective_speed = swimmer_speed + stream_speed
    time_taken = dist/effective_speed
    print("===========RESULTS============")
    print("Effective Speed : ",effective_speed," kmph")
    print("Time needed to swim: ", time_taken, "hours")

def main():
    choice =  print_menu()
    while choice !=0:
        if choice == 1:
            upstream()
        elif choice == 2:
            downstream()
        else:
            print("Invalid Choice")
        
        choice = print_menu()


if __name__ == "__main__":
    main()
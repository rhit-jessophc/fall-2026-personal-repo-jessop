import platloader

def main():
    print("Serial Menu")
    loader = plateloader.Plateloader("/dev/ttyUSB0")
    loader.connect() # 2 second timeout in this function
    print("0. Exit")
    print("1. reset")
    print("2. X - Axis")
    print("3. Gripper")
    print("4. Z-Axis")
    print("5. Move")
    print("6. Status")


while True:
    selection = int(input("Selection: "))
    if selection == 0:
        print("Exiting...")
        break
    elif selection == 1:
        pass
    elif selection == 2:
        pass
    elif selection == 3:
        pass
    elif selection == 4:
        pass
    elif selection == 5:
        pass
    elif selection == 6:
        pass


    main()

current_stav = "stav1"
print("Current stav is: ", current_stav)
while True:
    command = input("Enter a letter a/b or commands 'STOP' or 'RESET': ")
    if command == 'STOP':
        break
    if command == 'RESET':
        current_stav = "stav1"
        print("Current stav is: ", current_stav)

        continue
    match current_stav:
        case "stav1":
            if command == "a":
                print("Current stav is: ", current_stav)
                continue
            if command == "b":
                current_stav = "stav2"
                print("Current stav is: ", current_stav)
                continue
        case "stav2":
            if command == "a":
                current_stav = "stav3"
                print("Current stav is: ", current_stav)
                continue
            if command == "b":
                print("Current stav is: ", current_stav)
                continue
        case "stav3":
            if command == "a":
                current_stav = "stav1"
                print("Current stav is: ", current_stav)
                continue
            if command == "b":
                current_stav = "stav4"
                print("Current stav is: ", current_stav)
                continue
        case "stav4":
            if command == "a":
                current_stav = "stav3"
                print("Current stav is: ", current_stav)
                continue
            if command == "b":
                current_stav = "stav5"
                print("Current stav is: ", current_stav)
                continue
        case "stav5":
            if command == "a":
                current_stav = "stav6"
                print("Current stav is: ", current_stav)
                continue
            if command == "b":
                current_stav = "stav2"
                print("Current stav is: ", current_stav)
                continue
        case "stav6":
            if command == "a":
                current_stav = "stav1"
                print("Current stav is: ", current_stav)
                continue
            if command == "b":
                current_stav = "stav4"
                print("Current stav is: ", current_stav)
                continue

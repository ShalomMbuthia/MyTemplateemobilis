command=""
started=False
while True:
    command=input(" >>>").lower()
    if command=="start":
        if started:
            print("Car is already started")
        else:
         started=True
        print("Car started")
    elif command=="Stop":
        if not started:
            print("Car is already stopped!!!!")
        else:
            started=False
            print("Car Stopped")
    elif command=="help":
         print("""
        start- to start the car
        stop - to stop the car
        quit - to quit the car game
        """)
    elif command=="quit":
         break
    else:
        print("Sorry we do not understand that")

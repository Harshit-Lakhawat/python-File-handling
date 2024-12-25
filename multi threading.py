import threading
import time

def walk_dog(name):
    time.sleep(8)
    print(f"You finish walking {name}")

def take_out_trash():
    time.sleep(2)
    print("You take trash out")

def get_mail():
    time.sleep(4)
    print("You get the mail")

'''walk_dog()        # this take time as one task is done then it go to others
take_out_trash()
get_mail()'''

# here with help of multithreading this all function are working at same time
chore1 = threading.Thread(target=walk_dog, args=("tony",)) #we have used, in end so it reads as tuple
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

# use join as the last thing will print after the completion not at beginning
chore1.join()
chore2.join()
chore3.join()

print("All completed!")

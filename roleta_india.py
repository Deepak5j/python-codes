import random
import os

# single bullet loaded gun
gun = [0,0,0,0,1,0] 

while gun:
    path = input("Enter you OS system path: ")
    bullet = random.choice(gun)
    if bullet == 1:
        print("you dead")
        os.remove(path)
        break
    gun.remove(bullet)
    
        
    

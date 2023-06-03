import random
import os

# generates the numbers in sequence random times 
def generate_treasure_box():
    treasure_box = ""
    for i in range(10):
        counter = random.randint(1, 20)
        treasure_box += str(i) * counter
    treasure_box += "TREASURE"
    for i in range(9,-1,-1):
        counter = random.randint(1, 20)
        treasure_box += str(i) * counter
    print(treasure_box)
    return treasure_box

# checks if treasure_box.txt and deletes before creating a new one
def create_file():
    if os.path.exists("treasure_box.txt"):
        os.remove("treasure_box.txt")
        print("treasure_box.txt file deleted")
    else:
        print("no file treasure_box.txt to delete")
    with open("treasure_box.txt", "w+") as file:
        treasure_box = generate_treasure_box()
        file.write(treasure_box)
        print("treasure_box.txt file created")

# search for treasure in file
def index_treasure():
    with open("treasure_box.txt", "r+") as file:
        content = file.read()
        index = content.find("TREASURE")
        if index != -1:
            print("TREASURE found at index", index)
        else:
            print("TREASURE not found", index)

# search TREASURE moving forward and backwards
def search_treasure():
    with open("treasure_box.txt", "r+") as file:
        content = file.read()
        index = content.find("TREASURE")
        location = 0
        start = 1
        flag = 0
        
        while True:
            if start == 1 and flag == 1:
                start=0
            flag = 1
            print("location for file 4 testing: ", location)

            direction = input("Where you want to move? [1- forward 2-backwards]: ")
            if direction.strip().isdigit():
                direction = int(direction)
                if direction < 1 or direction > 2:
                    print("please enter to move [1- forward 2-backwards]")
                    continue
                else:
                    counter = input("enter a number of spaces to move to reach the TREASURE: ")
                    if counter.strip().isdigit():
                        counter = int(counter)
                    else:
                        print("you did not enter a number please enter a number")
                        continue
            else:
                print("you did not enter a number please enter a number")
                continue
            
            
            if direction == 1:
                location += counter
            else:
                location -= counter

            if start == 1 and direction == 2:
                print("you are at the starting point, move forward, location: ", content[location])
                continue
            elif location < 0 and start == 0:
                location = 0
                print("you reach the start point, move forward, you hit: ", content[location])
                continue
            elif location >= (len(content)-1):
                location = (len(content)-1)
                print("you reach the end point, try move backwards, you hit: ", content[location])
                continue

            if location >= index and location <= (index+7):
                print("TREASURE found at location: ", location)
                file.close()
                break
            else:
                print("TREASURE not found, you hit: ", content[location])
        
create_file()
index_treasure()
search_treasure()

import random as rd
def main():
    print("WELCOME TO THE PROFESSOR")
    try:
            lvl=get_level()
            point=0
            for i in range(10):
                attempt=0
                x,y=generate_int(lvl)   
                while attempt < 3:
                    try:
                        ans = int(input(f"{x} + {y} = "))
                        if ans == x + y:
                            point += 1
                            break
                        else:
                            print("EEE")
                            attempt += 1
                    except ValueError:
                        print("EEE")
                        attempt += 1
            print(f"Points:{point}")
               
    except ValueError:
            pass
             

    
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass  


def generate_int(lvl):
    if lvl==1:
        x=rd.randint(0,9)
        y=rd.randint(0,9)
    elif lvl==2:
        x=rd.randint(10,99)
        y=rd.randint(10,99)
    elif lvl==3:
        x=rd.randint(100,999)
        y=rd.randint(100,999)
    return x,y

    

if __name__=="__main__":
    main()

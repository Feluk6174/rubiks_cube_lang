import cube3x3

cube = cube3x3.cube()
stack = [[] for i in range(35)]
loaded = []


def to_int(val):
    temp = len(val)
    res = 0
    for i in range(temp):
        if val[-1*i-1] == "w":
            n_val = 0
        elif val[-1*i-1] == "y":
            n_val = 1
        elif val[-1*i-1] == "r":
            n_val = 2
        elif val[-1*i-1] == "o":
            n_val = 3
        elif val[-1*i-1] == "g":
            n_val = 4
        elif val[-1*i-1] == "b":
            n_val = 5

        if i == 0:
            res += n_val
        else:
            res += i*6*n_val

    return res

def to_char(num:int):
    if num == 0:
        return None
    if num >= 1 and num <= 28:
        return chr(96+num)
    if num == 29:
        return "\n"
    if num == 30:
        return "\'"
    if num == 31:
        return "."
    if num == 32:
        return ","
 

def load(num):
    global cube, stack, loaded
    loaded = stack[num]

def write_to_stack():
    global cube, stack
    #overwrite
    if cube.cube["w"]["edge"][1] == "w":
        length = to_int(cube.cube["w"]["corner"][2])
        print(length)
        pos = to_int(cube.cube["w"]["edge"][0]+cube.cube["w"]["edge"][2])
        print(pos)
        if length == 0:
            stack[pos] = []
        if length == 1:
            stack[pos] = []
            stack[pos].append(cube.cube["w"]["corner"][0])
        if length == 2:
            stack[pos] = []
            stack[pos].append(cube.cube["w"]["corner"][0])
            stack[pos].append(cube.cube["w"]["edge"][3])
        if length == 3:
            stack[pos] = []
            stack[pos].append(cube.cube["w"]["corner"][0])
            stack[pos].append(cube.cube["w"]["edge"][3])
            stack[pos].append(cube.cube["w"]["corner"][3])

    #append
    if cube.cube["w"]["edge"][1] == "y":
        length = to_int(cube.cube["w"]["corner"][2])
        print(length)
        pos = to_int(cube.cube["w"]["edge"][0]+cube.cube["w"]["edge"][2])
        print(pos)
        if length == 0:
            pass
        if length == 1:
            stack[pos].append(cube.cube["w"]["corner"][0])
        if length == 2:
            stack[pos].append(cube.cube["w"]["corner"][0])
            stack[pos].append(cube.cube["w"]["edge"][3])
        if length == 3:
            stack[pos].append(cube.cube["w"]["corner"][0])
            stack[pos].append(cube.cube["w"]["edge"][3])
            stack[pos].append(cube.cube["w"]["corner"][3])



def print_cube():
    global cube, stack
    
    if cube.cube["w"]["edge"][1] == "w":
        #data type
        if cube.cube["w"]["corner"][2] == "w":
            #int
            length = to_int(cube.cube["w"]["edge"][0])
            print(length)
            if length == 0:
                print("")
            elif length == 1:
                print(to_int(cube.cube["w"]["edge"][2]))
            elif length == 2:
                print(to_int(cube.cube["w"]["edge"][2]+cube.cube["w"]["corner"][0]))
            elif length == 3:
                print(to_int(cube.cube["w"]["edge"][2]+cube.cube["w"]["corner"][0]+cube.cube["w"]["edge"][3]))
            elif length == 4:
                print(to_int(cube.cube["w"]["edge"][2]+cube.cube["w"]["corner"][0]+cube.cube["w"]["edge"][3]+cube.cube["w"]["corner"][3]))

        if cube.cube["w"]["corner"][2] == "y":
            length = to_int(cube.cube["w"]["edge"][0])
            print(length)
            if length == 0:
                print("")
            if length == 2:
                print(to_char(to_int(cube.cube["w"]["edge"][2]+cube.cube["w"]["corner"][0])))
            if length == 4:
                print(to_char(to_int(cube.cube["w"]["edge"][2]+cube.cube["w"]["corner"][0])) + to_char(to_int(cube.cube["w"]["edge"][3]+cube.cube["w"]["edge"][3])))

def actions():
    global cube, stack
    if cube.cube["w"]["corner"][1] == "w":
        print_cube()
    if cube.cube["w"]["corner"][1] == "y":
        write_to_stack()
    if cube.cube["w"]["corner"][1] == "r":
        load()



def terminal():
    global cube
    print(cube)
    while True:
        action = input("    >> ")
        #print(action)
        if action == "e":
            break
        elif action == "s":
            cube.scramble()
        else:
            cube.move(action)
            if action == "u":
                actions()
        print(stack)
        print(cube)
        

terminal()
#print(to_int("yw"))
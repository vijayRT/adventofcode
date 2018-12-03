import numpy as np
def Day3():
    fabric = np.zeros((1000, 1000))
    inputdict = []
    overlapcount = 0
    
    # Process input data
    with open("day3input.txt", "r") as f:
        input = f.readlines()
        for line in input:
            linelist = line.split(" ")
            left_pos, top_pos = linelist[2].split(",")[0], linelist[2].split(",")[1].replace(":", "")
            width, height = linelist[3].split("x")[0], linelist[3].split("x")[1].replace("\n", "")
            id = linelist[0].lstrip("#")
            inputdict.append({
                "id": id,
                "left_pos": int(left_pos),
                "top_pos": int(top_pos),
                "width": int(width),
                "height": int(height)
            })
    
    # Generate fabric matrix and get Part 1 solution
    for i in range(len(inputdict)):
        top_pos = inputdict[i]["top_pos"]
        bottom_pos = inputdict[i]["top_pos"] + inputdict[i]["height"]
        left_pos = inputdict[i]["left_pos"]
        right_pos = inputdict[i]["left_pos"] + inputdict[i]["width"]
        for j in range(top_pos, bottom_pos):
            for k in range(left_pos, right_pos):
                fabric[j][k] += 1
    for i in range(1000):
        for j in range(1000):
            if(fabric[i][j]) > 1:
                overlapcount += 1
    
    # Extract submatrices from fabric matrix and get Part 2 solution
    for i in range(len(inputdict)):
        top_pos = inputdict[i]["top_pos"]
        bottom_pos = inputdict[i]["top_pos"] + inputdict[i]["height"]
        left_pos = inputdict[i]["left_pos"]
        right_pos = inputdict[i]["left_pos"] + inputdict[i]["width"]
        patch = fabric[top_pos:bottom_pos, left_pos:right_pos]
        flag = True
        for x in range(inputdict[i]["height"]):
            for y in range(inputdict[i]["width"]):
                if patch[x][y] != 1:
                    flag = False
        if flag == True:
            nooverlapid = inputdict[i]["id"]

    return overlapcount, nooverlapid

print(Day3())

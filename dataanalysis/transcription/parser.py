from pathlib import Path

data_folder = Path("textfiles/")
file_to_open = data_folder / "vg09.txt"

with open(file_to_open) as tscript:
    words = tscript.read()
words = words.replace("\n"," ").split(" ")
print(len(words))

def remAll(L, item):
    answer = []
    for i in L:
        if i!=item:
            answer.append(i)
    return answer

words = remAll(words, '')
print(words)
print(len(words))

def condsplit(transcript):
    AVL1 = []
    AOL1 = []
    AVL2 = []
    AOL2 = []
    AVL3 = []
    AOL3 = []
    AVL4 = []
    AOL4 = []
    AVL5 = []
    AOL5 = []
    AVL6 = []
    AOL6 = []
    AVL1e = []
    AOL1e = []
    AVL2e = []
    AOL2e = []
    AVL3e = []
    AOL3e = []
    AVL4e = []
    AOL4e = []
    AVL5e = []
    AOL5e = []
    AVL6e = []
    AOL6e = []
    switch = "base"
    for spot in transcript:
        if "[AVLV1]" in spot:
            switch = spot
            print(switch)
            continue
        if "[AOLV1]" == spot:
            switch = spot
            continue
        if "[AVLV2]" == spot:
            switch = spot
            continue
        if "[AOLV2]" == spot:
            switch = spot
            continue
        if "[AVLV3]" == spot:
            switch = spot
            continue
        if "[AOLV3]" == spot:
            switch = spot
            continue
        if "[AVLV4]" == spot:
            switch = spot
            continue
        if "[AOLV4]" == spot:
            switch = spot
            continue
        if "[AVLV5]" == spot:
            switch = spot
            continue
        if "[AOLV5]" == spot:
            switch = spot
            continue
        if "[AVLV6]" == spot:
            switch = spot
            continue
        if "[AOLV6]" == spot:
            switch = spot
            continue
        if "END" in spot:
            if "AV" in spot:
                if "LV1" in spot:
                    switch = spot
                    print(switch)
                    continue
                if "LV2" in spot:
                    switch = spot
                    continue
                if "LV3" in spot:
                    switch = spot
                    continue
                if "LV4" in spot:
                    switch = spot
                    continue
                if "LV5" in spot:
                    switch = spot
                    continue
                if "LV6" in spot:
                    switch = spot
                    continue
            if "AO" in spot:
                if "LV1" in spot:
                    switch = spot
                    continue
                if "LV2" in spot:
                    switch = spot
                    continue
                if "LV3" in spot:
                    switch = spot
                    continue
                if "LV4" in spot:
                    switch = spot
                    continue
                if "LV5" in spot:
                    switch = spot
                    continue
                if "LV6" in spot:
                    switch = spot
                    continue
        if switch == "[AVLV1]":
            AVL1.append(spot)
        if switch == "[AOLV1}":
            AOL1.append(spot)
        if switch == "[AVLV2]":
            AVL2.append(spot)
        if switch == "[AOLV2]":
            AOL2.append(spot)
        if switch == "[AVLV3]":
            AVL3.append(spot)
        if switch == "[AOLV3]":
            AOL3.append(spot)
        if switch == "[AVLV4]":
            AVL4.append(spot)
        if switch == "[AOLV4]":
            AOL4.append(spot)
        if switch == "[AVLV5]":
            AVL5.append(spot)
        if switch == "[AOLV5]":
            AOL5.append(spot)
        if switch == "[AVLV6]":
            AVL6.append(spot)
        if switch == "[AOLV6]":
            AOL6.append(spot)
    return AVL1, AOL1, AVL2, AOL2, AVL3, AOL3, AVL4, AOL4, AVL5, AOL5, AVL6, AOL6

print(condsplit(words))
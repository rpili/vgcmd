#parse.py
#ryan pili 07/31/19
#
#script to define a class for transcriptions, with functions to split it up into conditions, and into participants

from pathlib import Path

data_folder = Path("textfiles/")
file_to_open = data_folder / "dyad01.txt"

with open(file_to_open) as tscript:
    words = tscript.read()
words = words.replace("\n"," ").split(" ")

def remAll(L, item):
    answer = []
    for i in L:
        if i!=item:
            answer.append(i)
    return answer

words = remAll(words, '')

print(words)

for idx, spot in enumerate(words):
    if "[AVLV" in spot:
        print(idx, spot, "here")

class Parse:
    def __init__(self, input):
        self.input = input

    def condsplit(self):
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
        for spot in self.input:
            if "[AVLV1]" == spot:
                switch = spot
                continue
            elif "[AOLV1]" == spot:
                switch = spot
                continue
            elif "[AVLV2]" == spot:
                switch = spot
                continue
            elif "[AOLV2]" == spot:
                switch = spot
                continue
            elif "[AVLV3]" == spot:
                switch = spot
                continue
            elif "[AOLV3]" == spot:
                switch = spot
                continue
            elif "[AVLV4]" == spot:
                switch = spot
                continue
            elif "[AOLV4]" == spot:
                switch = spot
                continue
            elif "[AVLV5]" == spot:
                switch = spot
                continue
            elif "[AOLV5]" == spot:
                switch = spot
                continue
            elif "[AVLV6]" == spot:
                switch = spot
                continue
            elif "[AOLV6]" == spot:
                switch = spot
                continue
            elif "END" in spot:
                if "AV" in spot:
                    if "LV1" in spot:
                        switch = spot
                        print(switch)
                        continue
                    elif "LV2" in spot:
                        switch = spot
                        switch = spot
                        continue
                    elif "LV4" in spot:
                        switch = spot
                        continue
                    elif "LV5" in spot:
                        switch = spot
                        continue
                    elif "LV6" in spot:
                        switch = spot
                        continue
                elif "AO" in spot:
                    if "LV1" in spot:
                        switch = spot
                        continue
                    elif "LV2" in spot:
                        switch = spot
                        continue
                    elif "LV3" in spot:
                        switch = spot
                        continue
                    elif "LV4" in spot:
                        switch = spot
                        continue
                    elif "LV5" in spot:
                        switch = spot
                        continue
                    elif "LV6" in spot:
                        switch = spot
                        continue
            if switch == "[AVLV1]":
                AVL1.append(spot)
            elif switch == "[AOLV1]":
                AOL1.append(spot)
            elif switch == "[AVLV2]":
                AVL2.append(spot)
            elif switch == "[AOLV2]":
                AOL2.append(spot)
            elif switch == "[AVLV3]":
                AVL3.append(spot)
            elif switch == "[AOLV3]":
                AOL3.append(spot)
            elif switch == "[AVLV4]":
                AVL4.append(spot)
            elif switch == "[AOLV4]":
                AOL4.append(spot)
            elif switch == "[AVLV5]":
                AVL5.append(spot)
            elif switch == "[AOLV5]":
                AOL5.append(spot)
            elif switch == "[AVLV6]":
                AVL6.append(spot)
            elif switch == "[AOLV6]":
                AOL6.append(spot)
            elif switch == "[AVLV1END]":
                AVL1e.append(spot)
            elif switch == "[AOLV1END]":
                AOL1e.append(spot)
            elif switch == "[AVLV2END]":
                AVL2e.append(spot)
            elif switch == "[AOLV2END]":
                AOL2e.append(spot)
            elif switch == "[AVLV3END]":
                AVL3e.append(spot)
            elif switch == "[AOLV3END]":
                AOL3e.append(spot)
            elif switch == "[AVLV4END]":
                AVL4e.append(spot)
            elif switch == "[AOLV4END]":
                AOL4e.append(spot)
            elif switch == "[AVLV5END]":
                AVL5e.append(spot)
            elif switch == "[AOLV5END]":
                AOL5e.append(spot)
            elif switch == "[AVLV6END]":
                AVL6e.append(spot)
            elif switch == "[AOLV6END]":
                AOL6e.append(spot)
        return AVL1, AOL1, AVL2, AOL2, AVL3, AOL3, AVL4, AOL4, AVL5, AOL5, AVL6, AOL6

parser = Parse(words)

[AVL1, AOL1, AVL2, AOL2, AVL3, AOL3, AVL4, AOL4, AVL5, AOL5, AVL6, AOL6] = parser.condsplit()
print("AVL2", AVL2)
print("AVL4", AVL4)
print("AVL5", AVL5)
print("AVL1", AVL1)
print("AVL3", AVL3)
print("AVL6", AVL6)
print("AOL2", AOL2)
print("AOL4", AOL4)
print("AOL5", AOL5)
print("AOL1", AOL1)
print("AOL3", AOL3)
print("AOL6", AOL6)


#parse.py
#ryan pili 07/31/19
#
#script to define a class for transcriptions, with functions to split it up into conditions, and into participants

from pathlib import Path

data_folder = Path("textfiles/")
file_to_open = data_folder / "vg09.txt"

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
    if "[AVLVL" in spot:
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
        AVL6e = []i
        AOL6e = []
        switch = "base"
        for spot in self.input:
            if "[AVLVL1]" == spot:
                switch = spot
                continue
            elif "[AOLVL1]" == spot:
                switch = spot
                continue
            elif "[AVLVL2]" == spot:
                switch = spot
                continue
            elif "[AOLVL2]" == spot:
                switch = spot
                continue
            elif "[AVLVL3]" == spot:
                switch = spot
                continue
            elif "[AOLVL3]" == spot:
                switch = spot
                continue
            elif "[AVLVL4]" == spot:
                switch = spot
                continue
            elif "[AOLVL4]" == spot:
                switch = spot
                continue
            elif "[AVLVL5]" == spot:
                switch = spot
                continue
            elif "[AOLVL5]" == spot:
                switch = spot
                continue
            elif "[AVLVL6]" == spot:
                switch = spot
                continue
            elif "[AOLVL6]" == spot:
                switch = spot
                continue
            elif "END" in spot:
                if "AV" in spot:
                    if "LVL1" in spot:
                        switch = spot
                        print(switch)
                        continue
                    elif "LVL2" in spot:
                        switch = spot
                        continue
                    elif "LVL3" in spot:
                        switch = spot
                        continue
                    elif "LVL4" in spot:
                        switch = spot
                        continue
                    elif "LVL5" in spot:
                        switch = spot
                        continue
                    elif "LVL6" in spot:
                        switch = spot
                        continue
                elif "AO" in spot:
                    if "LVL1" in spot:
                        switch = spot
                        continue
                    elif "LVL2" in spot:
                        switch = spot
                        continue
                    elif "LVL3" in spot:
                        switch = spot
                        continue
                    elif "LVL4" in spot:
                        switch = spot
                        continue
                    elif "LVL5" in spot:
                        switch = spot
                        continue
                    elif "LVL6" in spot:
                        switch = spot
                        continue
            if switch == "[AVLVL1]":
                AVL1.append(spot)
            elif switch == "[AOLVL1]":
                AOL1.append(spot)
            elif switch == "[AVLVL2]":
                AVL2.append(spot)
            elif switch == "[AOLVL2]":
                AOL2.append(spot)
            elif switch == "[AVLVL3]":
                AVL3.append(spot)
            elif switch == "[AOLVL3]":
                AOL3.append(spot)
            elif switch == "[AVLVL4]":
                AVL4.append(spot)
            elif switch == "[AOLVL4]":
                AOL4.append(spot)
            elif switch == "[AVLVL5]":
                AVL5.append(spot)
            elif switch == "[AOLVL5]":
                AOL5.append(spot)
            elif switch == "[AVLVL6]":
                AVL6.append(spot)
            elif switch == "[AOLVL6]":
                AOL6.append(spot)
            elif switch == "[AVLVL1END]":
                AVL1e.append(spot)
            elif switch == "[AOLVL1END]":
                AOL1e.append(spot)
            elif switch == "[AVLVL2END]":
                AVL2e.append(spot)
            elif switch == "[AOLVL2END]":
                AOL2e.append(spot)
            elif switch == "[AVLVL3END]":
                AVL3e.append(spot)
            elif switch == "[AOLVL3END]":
                AOL3e.append(spot)
            elif switch == "[AVLVL4END]":
                AVL4e.append(spot)
            elif switch == "[AOLVL4END]":
                AOL4e.append(spot)
            elif switch == "[AVLVL5END]":
                AVL5e.append(spot)
            elif switch == "[AOLVL5END]":
                AOL5e.append(spot)
            elif switch == "[AVLVL6END]":
                AVL6e.append(spot)
            elif switch == "[AOLVL6END]":
                AOL6e.append(spot)
        return AVL1, AOL1, AVL2, AOL2, AVL3, AOL3, AVL4, AOL4, AVL5, AOL5, AVL6, AOL6

parser = Parse(words)

[AVL1, AOL1, AVL2, AOL2, AVL3, AOL3, AVL4, AOL4, AVL5, AOL5, AVL6, AOL6] = parser.condsplit()
print("AVL1", AVL1)
print("AVL3", AVL3)
print("AOL2", AOL2)
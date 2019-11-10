#parse.py
#ryan pili 07/31/19
#
#script to define a class for transcriptions, with functions to split it up into conditions, and into participants

from pathlib import Path
import csv



class Parse:
    def __init__(self, input):
        self.input = input

# method to word count for each participant -- dyad05.txt isn't setup right for it so save for later.
#    def pptsplit(self):
#        ppt_a = 0
#        ppt_b = 0
#        switch = "base"
#        for spot in self.input:
#            if ":" in spot:

    def wordcount(self):
        wordcount = 0
        for spot in self.input:
            if "[" in spot:
                continue
            elif ":" in spot:
                continue
            else:
                wordcount += 1
        return wordcount

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
        av_wordcount = 0
        ao_wordcount = 0
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
                        continue
                    elif "LV2" in spot:
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
                av_wordcount += 1
            elif switch == "[AOLV1]":
                AOL1.append(spot)
                ao_wordcount += 1
            elif switch == "[AVLV2]":
                AVL2.append(spot)
                av_wordcount += 1
            elif switch == "[AOLV2]":
                AOL2.append(spot)
                ao_wordcount += 1
            elif switch == "[AVLV3]":
                AVL3.append(spot)
                av_wordcount += 1
            elif switch == "[AOLV3]":
                AOL3.append(spot)
                ao_wordcount += 1
            elif switch == "[AVLV4]":
                AVL4.append(spot)
                av_wordcount += 1
            elif switch == "[AOLV4]":
                AOL4.append(spot)
                ao_wordcount += 1
            elif switch == "[AVLV5]":
                AVL5.append(spot)
                av_wordcount += 1
            elif switch == "[AOLV5]":
                AOL5.append(spot)
                ao_wordcount += 1
            elif switch == "[AVLV6]":
                AVL6.append(spot)
                av_wordcount += 1
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
        return AVL1, AOL1, AVL2, AOL2, AVL3, AOL3, AVL4, AOL4, AVL5, AOL5, AVL6, AOL6, av_wordcount, ao_wordcount


data_folder = Path("textfiles/")
file_to_open = data_folder / "dyad02.txt"

with open(file_to_open) as tscript:
    words = tscript.read()
words = words.replace("\n"," ").split(" ")

# working on building a script to read in the text
# right now it reads it in as a list of lists of strings
# the highest level list is 6 items long, for each of the 6 dyads
def transcript_reader():
    text_files = Path("textfiles").glob("*.txt")

    text_strings = [] 
    for text in text_files: 
        string = text.read_text()
        text_strings.append(string)

    cleaned_strings = []
    for dyad in text_strings:
        split_transcript = dyad.replace("\n", " ").split(" ")
        cleaned_strings.append(split_transcript)
    length = len(cleaned_strings)
    cleaned_type = type(cleaned_strings)
    print(f"Here is cleaned_strings, a {cleaned_type}, which is {length} items long:", cleaned_type)

transcript_reader()
    

def remall(L, item):
    answer = []
    for i in L:
        if i!=item:
            answer.append(i)
    return answer


words = remall(words, '')

# sanity check: make sure data is read in and previous function works
#print(words)


# sanity check: make sure tags even exist in the transcriptions
#for idx, spot in enumerate(words):
#    if "[AVLV" in spot:
#        print(idx, spot, "here")

parser = Parse(words)

wordcount = parser.wordcount()
print("wordcount is", wordcount)

[AVL1, AOL1, AVL2, AOL2, AVL3, AOL3, AVL4, AOL4, AVL5, AOL5, AVL6, AOL6, ao_wc, av_wc] = parser.condsplit()
condList = [AVL1, AOL1, AVL2, AOL2, AVL3, AOL3, AVL4, AOL4, AVL5, AOL5, AVL6, AOL6]
countList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
condNames = ["AVL1", "AOL1", "AVL2", "AOL2", "AVL3", "AOL3", "AVL4", "AOL4", "AVL5", "AOL5", "AVL6", "AOL6", "AV_BC", "AO_BC", "AV_WC", "AO_WC"]
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
print("av_wc is", av_wc)
print("ao_wc is", ao_wc)

for idx, cond in enumerate(condList):
    BCcounter = 0
    for word in cond:
        if "*" in word:
            BCcounter += 1
    countList[idx] = BCcounter
print(countList)

csv_folder = Path()
parseCSV = csv_folder / "parseCount.csv"

print(parseCSV)

textpath = Path(data_folder).glob('**/*.txt')
'''
try:
    parseCSV = parseCSV.resolve(strict=True)
except FileNotFoundError:
    # doesn't exist: create it and append condNames and countList
    with open('parseCount.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows([condNames])
        for path in textpath:
            countList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            pathStr = str(path)
            print(pathStr)

            with open(pathStr) as tscript:
                words = tscript.read()
            words = words.replace("\n", " ").split(" ")

            words = remall(words, '')

            parser = Parse(words)
            [AVL1, AOL1, AVL2, AOL2, AVL3, AOL3, AVL4, AOL4, AVL5, AOL5, AVL6, AOL6, av_wc, ao_wc] = parser.condsplit()
            condList = [AVL1, AOL1, AVL2, AOL2, AVL3, AOL3, AVL4, AOL4, AVL5, AOL5, AVL6, AOL6]

            for idx, cond in enumerate(condList):
                BCcounter = 0
                for word in cond:
                    if "*" in word:
                        BCcounter += 1
                countList[idx] = BCcounter
            print(countList)
            AV = countList[0] + countList[2] + countList[4] + countList[6] + countList[8] + countList[10]
            AO = countList[1] + countList[3] + countList[5] + countList[7] + countList[9] + countList[11]
            countList.extend((AV, AO, av_wc, ao_wc))
            writer.writerows([countList])
    csvFile.close()
else:
    # exists: append condNames and countList
    parseCSV.unlink()
    with open('parseCount.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows([condNames])
        for path in textpath:
            pathStr = str(path)
            countList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            pathStr = str(path)
            print(pathStr)

            with open(pathStr) as tscript:
                words = tscript.read()
            words = words.replace("\n", " ").split(" ")

            words = remall(words, '')

            parser = Parse(words)
            [AVL1, AOL1, AVL2, AOL2, AVL3, AOL3, AVL4, AOL4, AVL5, AOL5, AVL6, AOL6, av_wc, ao_wc] = parser.condsplit()
            condList = [AVL1, AOL1, AVL2, AOL2, AVL3, AOL3, AVL4, AOL4, AVL5, AOL5, AVL6, AOL6]

            for idx, cond in enumerate(condList):
                BCcounter = 0
                for word in cond:
                    if "*" in word:
                        BCcounter += 1
                countList[idx] = BCcounter
            print(countList)
            AV = countList[0] + countList[2] + countList[4] + countList[6] + countList[8] + countList[10]
            AO = countList[1] + countList[3] + countList[5] + countList[7] + countList[9] + countList[11]
            countList.extend((AV, AO, av_wc, ao_wc))
            writer.writerows([countList])
    csvFile.close()
'''

import random
import re

def answerslist(sentence):
    choices = sentence.replace(".","").strip(" ").split(", ")
    for i in range (0, len(choices)):
        if choices[i].startswith("("):
            answer = choices[i]
            answer = answer[4:]
            choices[i] = answer
    return (choices)

def getlabels(sentence):
    labels = re.findall(r'\([a-z]\)', sentence)
    return labels




def getquestionanswer():
    try:
        file = open("inputfile.txt","r")
        found = True
    except FileNotFoundError:
        print("the file wasnt found")

    if found:
        lines = file.readline()
        question_answer = {}
        while lines != "":
            words = lines.strip().split("(a)")
            question_answer[words[0]] = words[1]
            lines = file.readline()
        return question_answer
getquestionanswer()

def main():
    file = open("new_file.txt","w")
    answer = []
    label_list = []
    question_answer = getquestionanswer()
    count = 0
    for answers in question_answer.values():
        answers = "(a)" + answers
        answer.append(answerslist(answers))
        label_list.append(getlabels(answers))
    for question in question_answer.keys():
        file.write(question + "\n")
        choices = answer[count]
        random.shuffle(choices)
        label = label_list[count]
        for i in range(0,len(label)):
            choice = label[i] + " " + choices[i]
            file.write(choice)
            file.write("\n")
        file.write("\n")
        count += 1

main()
if __name__ == '__main__':
    nListGeneral=[]
    nameList = []


    for _ in range(int(input())):
        nListGeneral.append([input(), float(input())])

    nListGeneral.sort(key=lambda x: x[1])

    worstGrade = nListGeneral[0][1]
    secondWorstGrade = nListGeneral[1][1]

    for i in nListGeneral:
        if secondWorstGrade==worstGrade:
            secondWorstGrade = i[1]
        if i[1]>worstGrade and i[1]<= secondWorstGrade:
            nameList.append(i[0])

    nameList.sort()
    for i in nameList:
        print(i)

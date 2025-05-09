class Person:
    def __init__(self, ida, age, sex, dept, salary, nomenclature):
        self.id = ida
        self.age = age
        self.sex = sex
        self.dept = dept
        self.salary = salary
        self.nomenc = nomenclature

    def affiche(self):
        print(self.id, self.age, self.sex, self.dept, self.salary,  self.nomenc)

workers = []
        
def readFile(fileName):
    f = open(fileName)
    temp = f.readline().split(";")

    pos = {
        "age": 0,
        "sex": 0,
        "dept": 0,
        "salary": 0,
        "nomenc": 0
    }

    for i in range(len(temp)):
        if (temp[i] == "AGE"): pos["age"] = i
        if (temp[i] == "SEXE"): pos["sex"] = i
        if (temp[i] == "DEPT"): pos["dept"] = i
        if (temp[i] == "TRNNETO"): pos["salary"] = i
        if (temp[i] == "A6"): pos["nomenc"] = i

    for i in range (len(open(fileName).readlines()) - 1):
        s = f.readline().split(";")
        workers.append(Person(i+2, s[pos["age"]], s[pos["sex"]], s[pos["dept"]], s[pos["salary"]], s[pos["nomenc"]]))



readFile("FD_SALAAN_2016.csv")



def salaryManWoman(workers):
    repM=[]
    repF=[]
    

    for i in range(0,24):
        repM.append(0)
        repF.append(0)

    for i in range (0,len(workers)):
        if(workers[i].sex=="1"):
            repM[int(workers[i].salary)]+=1
        else:
            repF[int(workers[i].salary)]+=1

    print(repM)
    print(repF)

# la fonction à utiliser est proportionFemmeHomme, celle-là donne directement le nombre d'hommes et de femmes dans chaque departement
def salaireSelonDept(workers):
    sumH = [0, 0, 0, 0, 0, 0, 0]
    sumF = [0, 0, 0, 0, 0, 0, 0]

    for i in range (len(workers)):
        dept = workers[i].nomenc

        if (workers[i].sex == "1"):
            if (dept == ""): sumH[0] += 1
            if (dept == "AZ"): sumH[1] += 1
            if (dept == "BE"): sumH[2] += 1
            if (dept == "FZ"): sumH[3] += 1
            if (dept == "GI"): sumH[4] += 1
            if (dept == "JU"): sumH[5] += 1
            if (dept == "OQ"): sumH[6] += 1

        else:
            if (dept == ""): sumF[0] += 1
            if (dept == "AZ"): sumF[1] += 1
            if (dept == "BE"): sumF[2] += 1
            if (dept == "FZ"): sumF[3] += 1
            if (dept == "GI"): sumF[4] += 1
            if (dept == "JU"): sumF[5] += 1
            if (dept == "OQ"): sumF[6] += 1

    return sumH, sumF

# Proportions des femmes par rapports aux hommes selon la nomenclature agrégée A6
# les nomenclatures sont enregistrées dans cet ordre : non-renseigné, AZ, BE, FZ, GI, JU, OQ
def proportionFemmeHomme(workers):
    res = [0, 0, 0, 0, 0, 0, 0]
    sum = salaireSelonDept(workers)
    sumH = sum[0]
    sumF = sum[1]

    print(sumF)
    print(sumH)
    
    for i in range (len(sumH)):
        res[i] = sumF[i] / (sumH[i] + sumF[i])

    return res


salaryManWoman(workers)
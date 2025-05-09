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

# calcul des effectifs d'homme et de femme dans chaque secteur d'industrie selon la nomenclature agrégée A6 
def effectifSelonDept(workers):
    cpt = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

    # une hashmap serait bien
    for i in range (len(workers)):
        dept = workers[i].nomenc

        if (dept == ""): cpt[int(workers[i].sex) - 1][0] += 1
        if (dept == "AZ"): cpt[int(workers[i].sex) - 1][1] += 1
        if (dept == "BE"): cpt[int(workers[i].sex) - 1][2] += 1
        if (dept == "FZ"): cpt[int(workers[i].sex) - 1][3] += 1
        if (dept == "GI"): cpt[int(workers[i].sex) - 1][4] += 1
        if (dept == "JU"): cpt[int(workers[i].sex) - 1][5] += 1
        if (dept == "OQ"): cpt[int(workers[i].sex) - 1][6] += 1

    return cpt

# calcul de la moyenne d'age selon la région où habite le salarié
# il y a déjà un affichage intégré
def ageSalaireSelonReg(workers):
    cpt = {
        "non": 0,
        "01": 0,
        "02": 0,
        "03": 0,
        "04": 0,
        "11": 0,
        "24": 0,
        "27": 0,
        "28": 0,
        "32": 0,
        "44": 0,
        "52": 0,
        "53": 0,
        "75": 0,
        "76": 0,
        "84": 0,
        "93": 0,
        "94": 0
    }

    sum = {
        "non": 0,
        "01": 0,
        "02": 0,
        "03": 0,
        "04": 0,
        "11": 0,
        "24": 0,
        "27": 0,
        "28": 0,
        "32": 0,
        "44": 0,
        "52": 0,
        "53": 0,
        "75": 0,
        "76": 0,
        "84": 0,
        "93": 0,
        "94": 0
    }

    # sert pour l'affichage
    regr = {
        "non": "non-renseigné",
        "01": "Guadeloupe",
        "02": "Martinique",
        "03": "Guyane",
        "04": "La Réunion",
        "11": "Île-de-France",
        "24": "Centre-Val de Loire",
        "27": "Bourgogne-Franche-Comté",
        "28": "Normandie",
        "32": "Nord-Pas-de-Calais-Picardie",
        "44": "Alsace-Champagne-Ardenne-Lorraine",
        "52": "Pays de la Loire",
        "53": "Bretagne",
        "75": "Aquitaine-Limousin-Poitou-Charentes",
        "76": "Languedoc-Roussillon-Midi-Pyrénées",
        "84": "Auvergne-Rhône-Alpes",
        "93": "Provence-Alpes-Côte d'Azur",
        "94": "Corse"
    }

    for i in range(len(workers)):
        if (workers[i].regr == "" or workers[i].regr == "99"): 
            if (workers[i].age != ""):
                if(int(workers[i].age) > 16):
                    cpt["non"] += 1
                    sum["non"] += int(workers[i].age)

        else:
            if (workers[i].age != ""):
                if(int(workers[i].age) > 16):
                    cpt[workers[i].regr] += 1
                    sum[workers[i].regr] += int(workers[i].age)

    for i in cpt:
        sum[i] = round(sum[i] / cpt[i], 2)
        print(regr[i], ":", sum[i])

    return sum

salaryManWoman(workers)
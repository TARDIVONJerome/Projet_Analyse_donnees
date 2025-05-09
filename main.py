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
        
def readFile(fileName, workers):
    f = open(fileName)
    print(fileName, "en cours d'ouverture...")
    temp = f.readline().split(";")

    pos = {
        "age": 0,
        "sex": 0,
        "dept": 0,
        "salary": 0,
        "nomenc": 0,
        "reg": 0
    }

    # charge les positions de colonnes
    for i in range(len(temp)):
        if (temp[i] == "AGE"): pos["age"] = i
        if (temp[i] == "SEXE"): pos["sex"] = i
        if (temp[i] == "TRNNETO"): pos["salary"] = i
        if (temp[i] == "A6"): pos["nomenc"] = i
        if (temp[i] == "REGR"): pos["regr"] = i

    total = len(open(fileName).readlines()) - 1

    # pourcentage de chargement
    for i in range (total):
        s = f.readline().split(";")
        if (i % 30000 == 0): print(fileName + " lu à : " + str(round((i / total)*100, 2)) + "%")
        workers.append(Person(i+2, s[pos["age"]], s[pos["sex"]], s[pos["salary"]], s[pos["nomenc"]], s[pos["regr"]]))

    f.close()

    print("Lecture de", fileName, "terminé \n")



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
# il y a un affichage intégré (pas besoin d'afficher la valeur renvoyée)
def ageSelonReg(workers):
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
        if (workers[i].regr == "" or workers[i].regr == "99"):  # vérifie que la région soit renseignée
            if (workers[i].age != ""):                          # vérifie que l'age soit renseigné
                if(int(workers[i].age) > 16):                   # vérifie que le salarié aie au moins 16 ans (données abhérentes en dessous)
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


def salaryOldYoung(workers):
    repA=[]


    for i in range(0,16):
        repA.append([])
        for j in range (0,24):
            repA[i].append('#')
    for i in range (16,100):
        repA.append([])
        for j in range (0,24):
            repA[i].append(0)
    
    for i in range (0,len(workers)):
        if(workers[i].age!='' and int(workers[i].age)>15 and int(workers[i].age)<100): #on ne prend en compte que les salariés de 16 ans ou plus et on ignore également ceux ayant un age non renseigné à cause de données aberrantes (salariés en CDI de 0 ou 1 an)
            repA[int(workers[i].age)][int(workers[i].salary)]+=1
    
    for i in range (len(repA)):
        print(repA[i])

    return repA




def medSalaryOldYoung(repA,varmodfilename):
    ECC=[]
    for i in range(0,16):
        ECC.append([])
        for j in range(0,len(repA[i])):
            ECC[i].append('#')

    for i in range(16,len(repA)):
        ECC.append([])
        sum=0
        for j in range (0,len(repA[i])):
            sum+=repA[i][j]
            ECC[i].append(sum)

    for i in range (len(repA)):
        print(ECC[i])

    nummed=[]
    for i in range(0,16):
        nummed.append('#')
    for i in range(16,len(ECC)):
        nummed.append((ECC[i][len(ECC[i])-1]/2))

    print(nummed)

    med=[]
    salaries=getSalariesMinMax(varmodfilename)

    for i in range (0,16):
        med.append('#')
    for i in range (16,len(nummed)):
        # if(nummed[i]%1==0):
            
            for j in range (0,len(ECC[i])):
                if(nummed[i]-ECC[i][j]<=0):
                    
                    
                    med.append(    salaries[j][0]+    (    (nummed[i]-ECC[i][j-1])    *    (salaries[j][2]-salaries[j][0])    )    /    (ECC[i][j]-ECC[i][j-1])    )
                    break
    print(med)





def getSalariesMinMax(varmodfilename):
    res=[]
    f=open(varmodfilename)
    lines=f.readlines()
    cpt=0
    for i in range (0,len(lines)):
        tmp=lines[i].split(';')
        if(tmp[0]=="TRNNETO"):
            cpt+=1


    for i in range (0,cpt):
        res.append([None,None,None])

    for i in range (0,len(lines)):
        tmp=lines[i].split(';')
        
        if(tmp[0]=="TRNNETO"):
            tmp[2]=int(tmp[2])
            if("Moins" in tmp[3]):
                res[tmp[2]][0]=0
                tmpl=tmp[3].split(' ')
                if(len(tmpl)==4):
                    res[tmp[2]][2]=int(tmpl[2])
                else:
                    res[tmp[2]][2]=int(tmpl[2]+tmpl[3])
                
                res[tmp[2]][1]=(res[tmp[2]][0]+res[tmp[2]][2])/2

            elif("et plus" in tmp[3]):
                tmpl=tmp[3].split(' ')
                if(len(tmpl)==4):
                    res[tmp[2]][0]=int(tmpl[0])
                else:
                    res[tmp[2]][0]=int(tmpl[0]+tmpl[1])
                

            else :

                tmpl=tmp[3].split(' ')

                if(len(tmpl)==4):
                    res[tmp[2]][2]=int(tmpl[2])
                    res[tmp[2]][0]=int(tmpl[0])
                elif(len(tmpl)==5):
                    res[tmp[2]][2]=int(tmpl[2]+tmpl[3])
                    res[tmp[2]][0]=int(tmpl[0])
                elif(len(tmpl)==6):
                    res[tmp[2]][2]=int(tmpl[3]+tmpl[4])
                    res[tmp[2]][0]=int(tmpl[0]+tmpl[1])
            
                res[tmp[2]][1]=(res[tmp[2]][0]+res[tmp[2]][2])/2

    
    for i in range (0,len(res)):
        print(res[i])
    
    return res


# calcule la médiane des salaires selon le département
def medSalaireSelonDept(workers):
    cptH = {
        "none": [],
        "AZ": [],
        "BE": [],
        "FZ": [],
        "GI": [],
        "JU": [],
        "OQ": []
    }

    cptF = {
        "none": [],
        "AZ": [],
        "BE": [],
        "FZ": [],
        "GI": [],
        "JU": [],
        "OQ": []
    }

    for i in range(24):
        for j in cptH:
            cptH[j].append(0)
        for j in cptF:
            cptF[j].append(0)
        

    for i in range (len(workers)):
        dept = workers[i].nomenc

        if (workers[i].salary != ""):
            nomenc = workers[i].nomenc
            if (nomenc == ""): nomenc = "none"

            if (workers[i].sex == "1"): cptH[nomenc][int(workers[i].salary)] += 1
            else: cptF[nomenc][int(workers[i].salary)] += 1

    return cptH, cptF
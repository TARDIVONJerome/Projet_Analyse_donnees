class Person:
    def __init__(self, ida, age, sex, salary, nomenclature, regr):
        self.id = ida
        self.age = age
        self.sex = sex
        self.salary = salary
        self.nomenc = nomenclature
        self.regr = regr

    def affiche(self):
        print(self.id, self.age, self.sex, self.salary,  self.nomenc, self.regr)

workers2016 = []
workers2017 = []
workers2018 = []
workers2019 = []



readFile("Salaries\\FD_SALAAN_2016.csv", workers2016)
# readFile("Salaries\\FD_SALAAN_2017.csv", workers2017)
# readFile("Salaries\\FD_SALAAN_2018.csv", workers2018)
# readFile("Salaries\\FD_SALAAN_2019.csv", workers2019)
        
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
    

def salaryManWoman(workers): #calcule la répartition des hommes et de femmes dans les différentes tranches de salaire
    repM=[]
    repF=[]
    
    for i in range(0,24):
        repM.append(0)
        repF.append(0)

    for i in range (0,len(workers)):
        if(workers[i].age!='' and int(workers[i].age)>15 and int(workers[i].age)<100): #on ne prend en compte que les salariés entre 16 et 99 ans et on ignore également ceux ayant un age non renseigné à cause de données aberrantes (salariés en CDI de 0, 1 ou meme 127 ans)
            if(workers[i].sex=="1"):    #1=homme 2=femme
                repM[int(workers[i].salary)]+=1
            else:
                repF[int(workers[i].salary)]+=1

    print(repM) #affichage
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


def salaryOldYoung(workers): # calcul la répartition des ages dans les différentes tranches de salaire
    repA=[]


    for i in range(0,16):   #les 16 primières lignes (0 à 15 ans) sont remplies de '#' pour garder la position des indices (indice 50 = age 50)
        repA.append([])
        for j in range (0,24): #24 trhanges de salaire (0 à 23)
            repA[i].append('#')
    for i in range (16,100): # on vas jusqu'à 99 ans
        repA.append([])
        for j in range (0,24):
            repA[i].append(0) # initialisation à 0
    
    for i in range (0,len(workers)):
        if(workers[i].age!='' and int(workers[i].age)>15 and int(workers[i].age)<100): #on ne prend en compte que les salariés entre 16 et 99 ans et on ignore également ceux ayant un age non renseigné à cause de données aberrantes (salariés en CDI de 0, 1 ou meme 127 ans)
            repA[int(workers[i].age)][int(workers[i].salary)]+=1
    
    for i in range (len(repA)): #affichage
        print(repA[i])

    return repA
    
repA=salaryOldYoung(workers)

def medSalaryOldYoung(repA,varmodfilename): # calcul les salaires médians pour chaque age (16 à 99) (besoins d'un fichier varmod pour connaitre les différentes tranches de slalaire grâce à la fonction getSalariesMinMax())
    ECC=[] # calcul de l'effectif cumulé croissant
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

    for i in range (len(repA)): #affichage
        print(ECC[i])

    nummed=[] # calcul des position des médianes
    for i in range(0,16):
        nummed.append('#')
    for i in range(16,len(ECC)):
        nummed.append((ECC[i][len(ECC[i])-1]/2))

    print(nummed) # affichage

    med=[]
    salaries=getSalariesMinMax(varmodfilename) # récupération des tranches de salaires via le fichier varmod

    for i in range (0,16):
        med.append('#')
    for i in range (16,len(nummed)): #calcul des médianes
        
            
        for j in range (0,len(ECC[i])):
            if(nummed[i]-ECC[i][j]<=0): # vérification de la présence de la médiane dans la tranche actuelle
                    
                    
                med.append(    salaries[j][0]+    (    (nummed[i]-ECC[i][j-1])    *    (salaries[j][2]-salaries[j][0])    )    /    (ECC[i][j]-ECC[i][j-1])    ) # formule de la médiane sur un caractère quantitatif continu
                break
    print(med)




def getSalariesMinMax(varmodfilename): # transformation des codes de tranche de salaires (0 à 23) en listes de 3 éléments : [0]-->min de la tranche ; [1]--> moyenne de la tranche ; [2]--> max de la tranche
    res=[]
    f=open(varmodfilename)
    lines=f.readlines()
    cpt=0
    for i in range (0,len(lines)): # récupération du nombre de tranches (au cas où les tranches ne seraies pas dans l'ordre)
        tmp=lines[i].split(';')
        if(tmp[0]=="TRNNETO"):
            cpt+=1


    for i in range (0,cpt):
        res.append([None,None,None]) #initialisation à None

    for i in range (0,len(lines)):
        tmp=lines[i].split(';')
        
        if(tmp[0]=="TRNNETO"):
            tmp[2]=int(tmp[2])
            if("Moins" in tmp[3]):  #vérification du cas particulier "Moins de * euros"
                res[tmp[2]][0]=0  # min à 0
                tmpl=tmp[3].split(' ')  #ligne temporaire
                if(len(tmpl)==4): # gestion des cas de tailles des nombres (200 créé 1 string et 2 000 en créé 2 lors du split)
                    res[tmp[2]][2]=int(tmpl[2])
                else:
                    res[tmp[2]][2]=int(tmpl[2]+tmpl[3])
                
                res[tmp[2]][1]=(res[tmp[2]][0]+res[tmp[2]][2])/2 #moyenne de la tranche

            elif("et plus" in tmp[3]): #vérification du cas particulier " * euros et plus"
                tmpl=tmp[3].split(' ')
                if(len(tmpl)==4):
                    res[tmp[2]][0]=int(tmpl[0])
                else:
                    res[tmp[2]][0]=int(tmpl[0]+tmpl[1])

                    # les valeurs max et moyenne sont laissées à None
                

            else :

                tmpl=tmp[3].split(' ')

                if(len(tmpl)==4): # vérification des cas de taille de nombre (200 et 300)
                    res[tmp[2]][2]=int(tmpl[2])
                    res[tmp[2]][0]=int(tmpl[0])
                elif(len(tmpl)==5):  # vérification des cas de taille de nombre (900 et 1 000)
                    res[tmp[2]][2]=int(tmpl[2]+tmpl[3])
                    res[tmp[2]][0]=int(tmpl[0])
                elif(len(tmpl)==6):  # vérification des cas de taille de nombre (2 000 et 3 000)
                    res[tmp[2]][2]=int(tmpl[3]+tmpl[4])
                    res[tmp[2]][0]=int(tmpl[0]+tmpl[1])
            
                res[tmp[2]][1]=(res[tmp[2]][0]+res[tmp[2]][2])/2


#////J'aurais pu mieux traiter les tailles des nombres pour ne pas être limité à 99 999 en utilisant plus de split et en bouclant la concaténation des parties du nombre ce qui aurais rendu le programme plus adaptatif mais j'ai préféré utiliser ce temps pour d'autres fonctions (car pas réellement utile ici)\\\\#

    
    for i in range (0,len(res)): # affichage
        print(res[i])
    
    return res
                

medSalaryOldYoung(repA,'Varmod_SALAAN_2016.csv')



def medSalaryOldYoung(repA,varmodfilename): # calcul les salaires médians pour chaque age (16 à 99) (besoins d'un fichier varmod pour connaitre les différentes tranches de slalaire grâce à la fonction getSalariesMinMax())
    ECC=[] # calcul de l'effectif cumulé croissant
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

    for i in range (len(repA)): #affichage
        print(ECC[i])

    nummed=[] # calcul des position des médianes
    for i in range(0,16):
        nummed.append('#')
    for i in range(16,len(ECC)):
        nummed.append((ECC[i][len(ECC[i])-1]/2))

    print(nummed) # affichage

    med=[]
    salaries=getSalariesMinMax(varmodfilename) # récupération des tranches de salaires via le fichier varmod

    for i in range (0,16):
        med.append('#')
    for i in range (16,len(nummed)): #calcul des médianes
        
            
        for j in range (0,len(ECC[i])):
            if(nummed[i]-ECC[i][j]<=0): # vérification de la présence de la médiane dans la tranche actuelle
                    
                    
                med.append(    salaries[j][0]+    (    (nummed[i]-ECC[i][j-1])    *    (salaries[j][2]-salaries[j][0])    )    /    (ECC[i][j]-ECC[i][j-1])    ) # formule de la médiane sur un caractère quantitatif continu
                break
    print(med)


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
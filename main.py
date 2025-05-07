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



readFile("Salaries\FD_SALAAN_2017.csv")

workers[0].affiche()
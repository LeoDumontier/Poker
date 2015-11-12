__author__ = 'Leo'

def sommeAlterne(liste):
    somme = 0
    for i in range(len(liste)):
        if i % 2:
            somme = somme + liste[i]
        else:
            somme = somme - liste[i]

    return somme

def calcul(liste):
    unSurDeux = []
    for i in range(len(liste)):
        if i % 2:
            unSurDeux.append(liste[i])

    return sommeAlterne(unSurDeux)

def f(x,y):
    l = [1,2,3,4,5]
    print(calcul(l[x:y]))

print(f(0,4))

def totalDepensePersonne(depenses):
    total = 0
    for d in depenses:
        total += d

    return  total

def depenseGroupe(groupe):

    total = 0

    for (nom,d) in groupe:
        totalPersonne = totalDepensePersonne(d)
        total += totalPersonne
    return total

groupe = [("dominique", [15,12,8,3]),("camille", [20,34]),("claude", [52]), ("Meridth", [8])]

def bilan(feuilleDepenses):

    bilan = []
    nbParticipants = len(feuilleDepenses)

    totalDepenses = depenseGroupe(feuilleDepenses)
    partDepenses = totalDepenses / nbParticipants

    for (nom,depenses) in feuilleDepenses:
        depensesPersonne = totalDepensePersonne(depenses)
        participationPersonne = depensesPersonne - partDepenses
        bilan.append((nom,participationPersonne))

    return bilan

def afficheBilan(groupe):

    for (personne, totalFinal) in bilan(groupe):
        if totalFinal < 0:
            print(personne + " doit recevoir " + str(round(totalFinal) * - 1) + " euros")
        elif totalFinal > 0:
            print(personne + " doit payer " + str(round(totalFinal)) + " euros")
        else:
            print(personne + " doit ni payer ni, recevoir de l'argent")

afficheBilan(groupe)
# Tanasa Florin Petrisor

# Dilirici Mihai
# Nafornita Valentin
# Grupa 143

#q0,q1,q2,q3,q4,q5,q6
#0
#0, ,x
#3
#q0,0=q1,x,R
#q1,0=q2,x,R
#q2,0=q3,x,R
#q3,0=q4,x,R
#q4,0=q5,x,R
#q4,x=q6,x,R
#q0
#q5
#q6
#0,0,0,0,0

Q = input("Introduceti starile (separate prin virgula): ").split(",")
# Q este multimea starilor
Sigma = input("Introduceti alfabetul inputul (separate prin virgula): ").split(",")
#Sigma este alfabetul inputului
#Mai jos este verificarea ca Sigma nu primeste spatiu, intrucat acesta apartine gamma
while " " in Sigma:
    print("Spatiul nu apartine Sigma, el apartine Gamma. Reintroduceti Sigma")
    Sigma = input("Introduceti alfabetul inputul (separate prin virgula): ").split(",")
Gamma = input("Introduceti alfabetul tape ului (separate prin virgula): ").split(",")
if " " not in Gamma:
    Gamma.append(" ")
#Mai sus verific ca avem spatiu in gamma si daca nu avem ii punem
Delta = {}
Aparitii = [[x,0] for x in Q]
i = int(input("Numarul de tranzitii: "))
print("Introduceti tranzitiile de forma stare,litera=stare,litera,L/R")
for g in range(i):
    tranzitie = input().split('=')
    Stanga = tranzitie[0].split(',')
    Dreapta = tranzitie[1].split(',')
    #Mai jos sunt verificari pentru inputul de la tastatura daca pe foaie am scrie delta(q0,0)=(q1,x,R), aici in loc de q0 o sa avem Stanga[0], in loc de 0 o sa avem Stanga[1], in loc de q1 o sa avem Drepta[0]
    #in loc de x o sa avem Dreapta[1] si in loc de R o sa avem pe L si R
    if(Stanga[0] not in Q):
        print("Starea din stanga nu exista in Q.")
        continue
    if(Stanga[1] not in Gamma):
        print("Simbolul din stanga nu este in Sigma.")
        continue
    if(Dreapta[0] not in Q):
        print("Starea din dreapta nu este in Q.")
        continue
    if(Dreapta[1] not in Gamma):
        print("Simbolul din dreapta nu este in Gamma.")
        continue
    for u in range(len(Aparitii)):
        if Aparitii[u][0] == Stanga[0]:
            Aparitii[u][1] = 1
            #Acest array numit aparitii ma va ajuta mai incolo la verificarea starilor, intrucat nu vreau sa plece vreo tranzitie din qAccept sau qReject
    if(Dreapta[2] != "L" and Dreapta[2] != "R"):
        print("Nu ati introdus o miscare corecta.")
        continue
    #Dupa ce a trecut de toate verificarile necesare, adaugam in Delta tranzitia
    if Stanga[0] not in Delta.keys():
        Delta.update({Stanga[0]:{Stanga[1]:[Dreapta[0],Dreapta[1],Dreapta[2]]}})
    else:
        Delta[Stanga[0]].update({Stanga[1]:[Dreapta[0],Dreapta[1],Dreapta[2]]})
        
print(Delta)

#La starea de inceput nu am ce verificari sa fac, mai putin 
q0 = input("Introduceti starea de inceput: ")
while q0 not in Q:
    q0 = input("Reintroduceti starea de inceput: ")
    
    
#Mai jos avem verificarea ca qAccept este diferit de q0, ca nu pleaca tranzitii din acesta si ca apartine Q

verificare = 0
while verificare == 0:

    qAccept = input("Introduceti starea de acceptare: ")
    verificare = 0
    for u in range(len(Aparitii)):
        if(Aparitii[u][0] == qAccept):
            if Aparitii[u][1] == 0:
                verificare = 1
    if(qAccept == q0):
        verificare = 0
    while verificare == 0:
        print("Introduceti o noua stare de accept.")
        qAccept = input("Introduceti starea de acceptare: ")
        verificare = 0
        for u in range(len(Aparitii)):
            if(Aparitii[u][0] == qAccept):
                if Aparitii[u][1] == 0:
                    verificare = 1
        if qAccept == q0:
            verificare = 0
        if qAccept not in Q:
            verificare = 0
            
#Verificarea de la qReject este aproape la fel, insa trebuie sa avem grija sa nu alea qReject sa fie la fel ca si qAccept
                
qReject = input("Introduceti starea de reject: ")
verificare = 0
for u in range(len(Aparitii)):
    if(Aparitii[u][0] == qReject):
        if Aparitii[u][1] == 0:
            verificare = 1
if(qReject == qAccept or qReject == q0):
    verificare = 0
while verificare == 0:
    print("Introduceti o noua stare de reject.")
    qReject = input("Introduceti starea de reject: ")
    verificare = 0
    for u in range(len(Aparitii)):
        if(Aparitii[u][0] == qReject):
            if Aparitii[u][1] == 0:
                verificare = 1
    if qReject == qAccept or qReject == q0:
        verificare = 0
        
#Afisarea Turing Machine ului
print(Q)
print(Sigma)
print(Gamma)
print(Delta)
print(q0)
print(qAccept)
print(qReject)

Tape = input("Introduceti inputul separat prin virgula si fara a adauga spatii: ").split(',')
verificare = 0
#Verificam ca pe Tape avem elemente din alfabetul tape ului

while verificare == 0:
    v = 0
    for u in Tape:
        if u not in Gamma:
            print("Tape ul contine elemente care nu se afla in Sigma. Introduceti din nou Tape ul.")
            v = 1
            break
    if(v == 0):
        verificare = 1
    else:
        Tape = input("Introduceti inputul separat prin virgula: ").split(',')
    if " " in Tape:
        verificare = 0
        
#Adaugam un spatiu la final pentru a stii cand se termina inputul
Tape.append(" ")
#Copiem Tape ul in TapeBackup
TapeBackup = [x for x in Tape]

#Simulam o problema la tape ul initial, asta insemnand ca pe pozitia 5 in loc de 0 ar fi trebuit sa fie x
TapeBackup[4] = 'x'
#Poate fi comentata comanda de mai sus pentru a se vedea ca merge okay fara aceasta "eroare de stocare" 

stare = q0
stareBackup = q0
indiceTape = 0
indiceTapeBackup = 0
print(Tape)
print(TapeBackup)

while True:
    try:
        #Pentru verificare fac ce am facut la primul exercitiu, insa acum trec prin tranzitii si cu tape ul de backup, iar in momentul in care intalnesc vreo diferenta intre cele doua e clar ca undeva a avut loc
        #o eroare de stocare si opresc programul
        stareNoua = Delta[stare][Tape[indiceTape]][0]
        tapeNou = Delta[stare][Tape[indiceTape]][1]
        indiceNou = indiceTape
        
        if Delta[stare][Tape[indiceTape]][2]=='L':
            indiceNou -= 1
        else:
            indiceNou += 1
            
        Tape[indiceTape] = tapeNou
        stare = stareNoua
        indiceTape = indiceNou
        
        stareNouaBackup = Delta[stareBackup][TapeBackup[indiceTapeBackup]][0]
        tapeNouBackup = Delta[stareBackup][TapeBackup[indiceTapeBackup]][1]
        indiceNouBackup = indiceTapeBackup
        
        if Delta[stareBackup][TapeBackup[indiceTapeBackup]][2]=='L':
            indiceNouBackup -= 1
        else:
            indiceNouBackup += 1
            
        TapeBackup[indiceTapeBackup] = tapeNouBackup
        stareBackup = stareNouaBackup
        indiceTapeBackup = indiceNouBackup
        
        if indiceTapeBackup != indiceTape:
            print("A intervenit o eroare la stocarea tape ului initial.")
            break
        if TapeBackup[indiceTapeBackup] != Tape[indiceTape]:
            print("A intervenit o eroare la stocarea tape ului initial.")
            break
        if stareBackup != stare:
            print("A intervenit o eroare la stocarea tape ului initial.")
            break
        
        if(stare == qAccept):
            print("Input acceptat.")
            break
        if(stare == qReject):
            print("Input neacceptat.")
            break
        
        print(Tape)
    except:
        #Acest try si except are rolul de a nu trimite eroare in momentul cand nu mai are unde sa mearga sau asa si doar afiseaza ca inputul a fost respins
        print("Input respins")
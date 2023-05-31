#Tanasa Florin Petrisor
#Nafornita Valentin-Adrian
#Dilirici Mihai
#Grupa 143

import string 
#importul este pentru a lua toate litere alfabetului mai usor
lung=int(input("Introduceti lungimea w ului:"))
Q = []
Sigma = []
for i in range(lung):
    Q.append(f"q{i}")
Sigma = list(string.ascii_letters)
Gamma = list(string.ascii_letters) + ['@',' ','#']

Delta = {}

for i in range(len(Q)):
    stare = "q"+str(i)
    tranzitii = {stare:{}}
    y = i+1
    stareViitoare ="q"+str(y)

    for j in range(len(Sigma)):
        tranzitii[stare].update({Sigma[j]:[stareViitoare,"@","R"]})
    Delta.update(tranzitii)
    
print(Delta)

q0 = 'q0'
qAccept = 'q'+str(len(Q))
qReject = 'q'+str(len(Q)+1)
Q.append([qAccept,qReject])

Tape = input("Introduceti inputul separat prin virgula: ").split(',')
verificare = 0

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
        
Tape.append(" ")
TapeBackup = [x for x in Tape]

stare = q0
stareBackup = q0
indiceTape = 0
indiceTapeBackup = 0
print(Tape)
print(TapeBackup)

while True:
    if Tape[indiceTape] != Tape[indiceTape + lung+1]:
        print("Inputul a fost respins")
        break

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
    
    if Tape[indiceTape] == "#" and Tape[indiceTape+lung+1] == " ":
        print("Inputul a fost acceptat")
        break
    
    Tape[indiceTape + lung] = '@'
    TapeBackup[indiceTapeBackup + lung] = '@'
    
    if indiceTapeBackup != indiceTape:
        print("A intervenit o eroare la stocarea tape ului initial.")
        break
    if TapeBackup[indiceTapeBackup] != Tape[indiceTape]:
        print("A intervenit o eroare la stocarea tape ului initial.")
        break
    if stareBackup != stare:
        print("A intervenit o eroare la stocarea tape ului initial.")
        break
    
    print(Tape)
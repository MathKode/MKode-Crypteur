import time
def translettre(h,mms) :
    tour = 0
    while tour < h:
        if mms[tour] == 'a':
            mms[tour] = 1
        if mms[tour] == 'b':
            mms[tour] = 2
        if mms[tour] == 'c':
            mms[tour] = 3
        if mms[tour] == 'd':
            mms[tour] = 4
        if mms[tour] == 'e':
            mms[tour] = 5
        if mms[tour] == 'f':
            mms[tour] = 6
        if mms[tour] == 'g':
            mms[tour] = 7
        if mms[tour] == 'h':
            mms[tour] = 8
        if mms[tour] == 'i':
            mms[tour] = 9
        if mms[tour] == 'j':
            mms[tour] = 10
        if mms[tour] == 'k':
            mms[tour] = 11
        if mms[tour] == 'l':
            mms[tour] = 12
        if mms[tour] == 'm':
            mms[tour] = 13
        if mms[tour] == 'n':
            mms[tour] = 14
        if mms[tour] == 'o':
            mms[tour] = 15
        if mms[tour] == 'p':
            mms[tour] = 16
        if mms[tour] == 'q':
            mms[tour] = 17
        if mms[tour] == 'r':
            mms[tour] = 18
        if mms[tour] == 's':
            mms[tour] = 19
        if mms[tour] == 't':
            mms[tour] = 20
        if mms[tour] == 'u':
            mms[tour] = 21
        if mms[tour] == 'v':
            mms[tour] = 22
        if mms[tour] == 'w':
            mms[tour] = 23
        if mms[tour] == 'x':
            mms[tour] = 24
        if mms[tour] == 'y':
            mms[tour] = 25
        if mms[tour] == 'z':
            mms[tour] = 26
        if mms[tour] == '.':
            mms[tour] = 27
        if mms[tour] == '!':
            mms[tour] = 28
        if mms[tour] == ',':
            mms[tour] = 29
        if mms[tour] == '?':
            mms[tour] = 30
        if mms[tour] == "'" :
            mms[tour] = 31
        if mms[tour] == 'ç' :
            mms[tour] = 32
        if mms[tour] == 'é' :
            mms[tour] = 33
        if mms[tour] == 'è' :
            mms[tour] = 34
        if mms[tour] == '(' :
            mms[tour] = 35
        if mms[tour] == ')' :
            mms[tour] = 36
        if mms[tour] == ':' :
            mms[tour] = 37
        if mms[tour] == '/' :
            mms[tour] = 38
        if mms[tour] == 'à':
            mms[tour] = 39
        if mms[tour] == '%' :
            mms[tour] = 40
        if mms[tour] == ' ' :
            mms[tour] = 0

        tour = tour + 1
    return mms
def transchiffre(h,mms) :
    tour = 0
    while tour < h:
        if mms[tour] == 1 :
            mms[tour] = 'a'
        if mms[tour] == 2 :
            mms[tour] = 'b'
        if mms[tour] == 3 :
            mms[tour] = 'c'
        if mms[tour] == 4 :
            mms[tour] = 'd'
        if mms[tour] == 5 :
            mms[tour] = 'e'
        if mms[tour] == 6 :
            mms[tour] = 'f'
        if mms[tour] == 7 :
            mms[tour] = 'g'
        if mms[tour] == 8 :
            mms[tour] = 'h'
        if mms[tour] == 9 :
            mms[tour] = 'i'
        if mms[tour] == 10 :
            mms[tour] = 'j'
        if mms[tour] == 11 :
            mms[tour] = 'k'
        if mms[tour] == 12 :
            mms[tour] = 'l'
        if mms[tour] == 13 :
            mms[tour] = 'm'
        if mms[tour] == 14 :
            mms[tour] = 'n'
        if mms[tour] == 15 :
            mms[tour] = 'o'
        if mms[tour] == 16 :
            mms[tour] = 'p'
        if mms[tour] == 17 :
            mms[tour] = 'q'
        if mms[tour] == 18 :
            mms[tour] = 'r'
        if mms[tour] == 19:
            mms[tour] = 's'
        if mms[tour] == 20 :
            mms[tour] = 't'
        if mms[tour] == 21 :
            mms[tour] = 'u'
        if mms[tour] == 22 :
            mms[tour] = 'v'
        if mms[tour] == 23 :
            mms[tour] = 'w'
        if mms[tour] == 24 :
            mms[tour] = 'x'
        if mms[tour] == 25 :
            mms[tour] = 'y'
        if mms[tour] == 26 :
            mms[tour] = 'z'
        if mms[tour] == 27 :
            mms[tour] = '.'
        if mms[tour] == 28 :
            mms[tour] = '!'
        if mms[tour] == 29 :
            mms[tour] = ','
        if mms[tour] == 30 :
            mms[tour] = '?'
        if mms[tour] == 31 :
            mms[tour] = "'"
        if mms[tour] == 32 :
            mms[tour] = "ç"
        if mms[tour] == 33 :
            mms[tour] = 'é'
        if mms[tour] == 34 :
            mms[tour] = 'è'
        if mms[tour] == 35 :
            mms[tour] = '('
        if mms[tour] == 36 :
            mms[tour] = ')'
        if mms[tour] == 37 :
            mms[tour] = ':'
        if mms[tour] == 38 :
            mms[tour] = '/'
        if mms[tour] == 39 :
            mms[tour] = 'à'
        if mms[tour] == 40 :
            mms[tour] = '%'
        if mms[tour] == 0 :
            mms[tour] = ' '

        tour = tour + 1
    return mms
print("CRYPTEUR MADE BY Mathis KREMER                  V1.9 15/02/2020")
chois = input("Voulez-vous connaître le mode d'utilisation de ce CRYPTEUR (O/N) : ")
chois = chois.lower()

if chois == 'o' :
    print('Ce programme est un Crypteur de Données (format texte)')
    time.sleep(0.5)
    print("Vous entrer votre message, puis une clefs (si vous n'avez pas la clefs, le message sera alors impossible à décrypter)")
    time.sleep(0.5)
    print("Ensuite l'on va vous demander deux lettres pour les échanger")
    time.sleep(0.5)
    print("                 EXEMPLE : E/U        ")
    time.sleep(0.5)
    print("JE SUIS GRAND   ->   JU SEIS GRAND ")
    print('')
    time.sleep(0.5)
    print("Vous pouvez écrire des message en Maj ou min")
    time.sleep(0.5)
    print("Vous n'êtes pas obligé de rentrer une clefs qui fait la même longueur que votre message")
    time.sleep(0.5)
    print("Les chiffres sont INTERDIT")
    time.sleep(0.5)
    chois = input("Voulez-vous connaitres les caractères autorisés (O/N) : ")
    chois = chois.lower()
    if chois == "o" :
        print("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZàéèç.,?:/!%()' ")


while True :

    i = 0
    while i == 0:
        # Crypter ou décrypter
        choix = input("Crypter ou Décrypter (C/D) : ")
        # Je converti tout en majuscule pour éviter les Bugs
        choix = choix.upper()
        if choix == "C" or choix == "D":
            if choix == "C":
                choix = "1"  # Si le choix = 1, cela veut dire que l'on crypte
            else:
                choix = "2"  # On décrypte
            # Demande la message et la key
            message = input("Quel est le message : ")
            key = input("Quelle est la clée : ")
            message = message.lower()
            key = key.lower()

            i = 1
            #demander le changement
            letre = []
            ay = input("Quelle lettre veux tu changer 1 : ")
            ay = ay.lower()
            by = input("Quelle lettre veux tu changer 2 : ")
            by = by.lower()
            letre = [ay,by]

            #commencer le code
            if choix == "1" :
                # isoler les differentes lettres
                # lettre du message :
                second = 0
                h = len(message)  # conte le nombre de lettre t despaces dans message pour la boucle

                mms = []  # creation de la liste qui va contenir les lettre
                tour = 0
                while tour < h:
                    tour = tour + 1
                    mms.append(message[second:tour])

                    second = second + 1

                    # lettre de la clé et repetition meme dure que le msm
                second = 0
                tour = 0
                tourtotal = 0
                c = len(key)
                clefs = []
                while tourtotal < h:
                    tour = tour + 1
                    tourtotal = tourtotal + 1
                    if key[second:tour] == "":
                        tour = 1
                        second = 0
                    clefs.append(key[second:tour])


                    second = second + 1
                # transformation en chiffre
                # message :
                mms = translettre(h, mms)  # h correspond a la longueur du message, mms correspond a la liste

                # key :
                clefs = translettre(h, clefs)


                # additionner les deux liste :

                final = []
                tour = 0
                h = len(mms)


                while tour < h :
                    num1 = mms[tour]
                    num2 = clefs[tour]
                    total = int(num1) + int(num2)
                    final.append(total)

                    tour = tour + 1

                #soustrare 26 pour ceux qui sont a dela de 26
                tour = 0
                while tour < h :
                    if int(final[tour]) > 40 :
                        num1 = int(final[tour])
                        numf = int(num1) - 40
                        final[tour] = numf
                    tour = tour + 1


                #transformer le résultat final en lettre
                final = transchiffre(h,final)


                #transformer les lettres :
                tour = 0
                while tour < h :
                    if final[tour] == letre[0] :
                        final[tour] = letre[1]
                    elif final[tour] == letre[1] :
                        final[tour] = letre[0]
                    tour = tour + 1


                fin = ''.join(final)
                print("---------MESSAGE---------")
                print(fin)
                print("-------------------------")


            else :
                # isoler les differentes lettres
                # lettre du message :
                second = 0
                h = len(message)  # conte le nombre de lettre t despaces dans message pour la boucle

                mms = []  # creation de la liste qui va contenir les lettre
                tour = 0
                while tour < h:
                    tour = tour + 1
                    mms.append(message[second:tour])

                    second = second + 1

                    # lettre de la clé et repetition meme dure que le msm
                second = 0
                tour = 0
                tourtotal = 0
                c = len(key)
                clefs = []
                while tourtotal < h:
                    tour = tour + 1
                    tourtotal = tourtotal + 1
                    if key[second:tour] == "":
                        tour = 1
                        second = 0
                    clefs.append(key[second:tour])

                    second = second + 1
                # changer les lettre
                tour = 0
                while tour < h:
                    if mms[tour] == letre[0]:
                        mms[tour] = letre[1]
                    elif mms[tour] == letre[1]:
                        mms[tour] = letre[0]
                    tour = tour + 1



                # transformation en chiffre
                # message :
                mms = translettre(h, mms)  # h correspond a la longueur du message, mms correspond a la liste

                # key :
                clefs = translettre(h, clefs)




                # transformation en chiffre
                # message :
                mms = translettre(h, mms)  # h correspond a la longueur du message, mms correspond a la liste

                # key :
                clefs = translettre(h, clefs)

                # soustraire les deux liste :

                final = []
                tour = 0
                h = len(mms)

                while tour < h:
                    num1 = mms[tour]
                    num2 = clefs[tour]
                    total = int(num1) - int(num2)
                    final.append(total)

                    tour = tour + 1
                # ajouter 26 pour ceux qui sont en dessous de a
                tour = 0
                while tour < h:
                    if int(final[tour]) < 0 :
                        num1 = int(final[tour])
                        numf = int(num1) + 40
                        final[tour] = numf
                    tour = tour + 1


                # transformer le résultat final en lettre
                final = transchiffre(h, final)


                fin = ''.join(final)
                print("---------MESSAGE---------")
                print(fin)
                print("-------------------------")





        else:
            print("Il faut écrire un D(décrypter) ou un C(crypter)")
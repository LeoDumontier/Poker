import os
from pocker import  Data

class Interface:

    interfaceState = 0

    playerList = []
    gameLimit = 6
    roomName = "Partie_barbieri"

    cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    cardsStr = ["A","2","3","4","5","6","7","8","9","10","J","D","R"]

    cardsType = [1,2,3,4]
    cardsTypeStr = ["P","T","C","O"]

    tirageCard = []

    pot = 15

    unite = "Keb"
    myMoney = 452563
    myPlayerName = "Léo"

    colorList = [('red', '\033[0;31m'),
                 ('green', '\033[0;32m'),
                 ('yellow', '\033[0;33m'),
                 ('blue', '\033[0;34m'),
                 ('purple', '\033[0;35m'),
                 ('cyan', '\033[0;36m')]

    colorEnd = "\033[0m"

    listTable = []

    def getColorTag(self, getColorName):
        tag = ''
        for (colorName, colorTag) in self.colorList:
            if colorName == getColorName:
                tag = colorTag
        return tag

    def __init__(self, playerList):

        for playerName in playerList:
            self.AddPlayer(playerName)

    def CheckGameFull(self):

        gameFull = False
        if len(self.playerList) >= self.gameLimit:
            gameFull = True

        return gameFull

    def GetPlayerNum(self, playerName):
        playerNum = 0

        if self.CheckExistPlayer(playerName):
            for playerIndex in range(len(self.playerList)):
                if self.playerList[playerIndex][0] == playerName:
                    playerNum = playerIndex + 1

        return playerNum

    def AddCardTirage(self, card):
        self.tirageCard.append(card)

    def ClearTirage(self):
        self.tirageCard = []

    def GetPlayerList(self):

        playerList = []

        for player in self.playerList:
            playerList.append(player[0])

        return playerList

    def GetPlayerInfos(self, playerName):

        playerInfo = []

        for player in self.playerList:

            if player[0] == playerName:
                playerInfo = player

        return playerInfo

    def GetPlayerCards(self, playerName):

        playerCards = []

        for player in self.playerList:

            if player[0] == playerName:
                playerCards.append(player[3])
                playerCards.append(player[4])

        return playerCards

    def TranslateCardsStr(self, cardNum):

        card = "[]"
        if len(str(cardNum)) > 1:

            cardType = int(str(cardNum)[-1])
            cardNum = int(str(cardNum)[:-1])

            if cardType <= len(self.cardsType) and cardNum <= len(self.cards):
                card = self.cardsStr[cardNum - 1] + "" + self.cardsTypeStr[cardType - 1]

        return card

    def MoneyFormat(self, money):

        moneyStr = '{:,}'.format(money)
        moneyStr = moneyStr.replace(",", " ")
        return moneyStr

    def ChangeMoneyPlayer(self, playerName, newMoney):

        changeMoney = True
        if self.CheckExistPlayer(playerName) and str(newMoney).isdigit():
            self.playerList[self.GetPlayerNum(playerName) - 1][1] = newMoney
        else:
            changeMoney = False

        return changeMoney

    def GetMoneyPlayer(self, playerName):
        money = 0

        if self.CheckExistPlayer(playerName):
            money = self.playerList[self.GetPlayerNum(playerName) - 1][1]

        return money

    def CheckExistPlayer(self, playerName):
        playerExist = False

        for player in self.playerList:
            if player[0] == playerName:
                playerExist = True
                break

        return playerExist

    def GetPlayerStatus(self, playerName):
        return self.GetPlayerInfos(playerName)[2]

    def AddPlayer(self, playerName):

        playerAdd = False
        if not self.CheckExistPlayer(playerName) and not self.CheckGameFull():

            playerInfo = []
            playerInfo.append(playerName)
            playerInfo.append(0)
            playerInfo.append('C')
            playerInfo.append('00')
            playerInfo.append('00')

            self.playerList.append(playerInfo)

            playerAdd = True

        return playerAdd


    def RemovePlayer(self, playerName):

        playerRemove = False
        if self.CheckExistPlayer(playerName):
            del self.playerList[self.playerList.index(playerName)]
            playerRemove = True

        return playerRemove

    def GetPlayerLabelTable(self, playerName):

        label = "--null--"

        if self.CheckExistPlayer(playerName):
            label = playerName + " - " + self.GetPlayerStatus(playerName)

        return label

    def ClearScreen(self):
        print("\n" * 60)

    def DrawWelcome(self, checkingStateInt, playerName):
        self.ClearScreen()
        for l in range(34):
            line = []
            for c in range(120):
                line.append(" ")
            if l in [0,33]:
                for c in range(120):
                    line[c] = "-"

            else:
                line[119] = "|"
                line[0] = "|"

                lineWrite = ""
                pokerLogo = [
                    "*****************************************************************",
                    "*                                                               *",
                    "*     ***********  **********  *     *  ********  *********     *",
                    "*     *         *  *        *  *    *   *         *       *     *",
                    "*     *         *  *        *  *   *    *         *       *     *",
                    "*     *         *  *        *  *  *     *         *       *     *",
                    "*     *         *  *        *  * *      *         *       *     *",
                    "*     *         *  *        *  **       *         *       *     *",
                    "*     ***********  *        *  **       ********  *********     *",
                    "*     *            *        *  * *      *         **            *",
                    "*     *            *        *  *  *     *         * **          *",
                    "*     *            *        *  *   *    *         *   **        *",
                    "*     *            *        *  *    *   *         *     **      *",
                    "*     *            **********  *     *  ********  *       *     *",
                    "*                                                               *",
                    "*****************************************************************",
                ]

                checkingState = [
                    "Vérification de la connexion au serveur d'identification ...",
                    "Vérfication de mise à jour ...",
                    "Récupération des informations utilisateur ...",
                    "Bienvenue " + playerName + " !",
                    "Erreur : La connexion au serveur à échoué !"
                ]

                for pokerLogoLine in range(len(pokerLogo)):
                    if l == 4 + pokerLogoLine:
                        lineWrite = pokerLogo[pokerLogoLine]

                if l == 21:
                    lineWrite = "Crée par Baptiste & Léo"
                elif l == 25:
                    lineWrite = "-" * 118
                elif l == 29:
                    lineWrite = checkingState[checkingStateInt]

                for caseL in range(len(lineWrite)):
                    line[60 - len(lineWrite) // 2 + caseL] = lineWrite[caseL]

            lineStr = ""
            for lineS in line:
                lineStr += lineS
            print(lineStr)

    def ShowHelpMenu(self):
        print("Aide : ")
        print("   - \\reload                      : rafraichis le menu" + "\n",
              "  - \join <Numero> <Montant>     : pour joindre une salle" + "\n",
              "  - \exit                        : pour quitter")

    def DrawMenu(self, menuState):
        self.ClearScreen()
        playerConnected = Data.GetOnlinePlayer()
        for l in range(34):
            line = []
            for c in range(120):
                line.append(" ")
            if l in [0,33]:
                for c in range(120):
                    line[c] = "-"

            else:
                line[119] = "|"
                line[0] = "|"

                lineWriteLeft = ""
                lineWriteRight = ""
                lineWriteCenter = ""

                if l == 1:
                    lineWriteLeft = " Bienvenue, " + self.myPlayerName
                    lineWriteRight = "| " + self.MoneyFormat(self.myMoney) + " " + self.unite + " "
                elif l == 2:
                    lineWriteLeft = "-" * 118


                if menuState == 0:

                    if l == 3:
                        lineWriteRight = "| Joueurs connectés (" + str(len(playerConnected)) + ") : "
                        lineWriteRight = lineWriteRight + (" " * (31 - len(lineWriteRight)))
                        lineWriteLeft = " Liste des tables disponible (0) :"
                    elif l == 4:
                        lineWriteRight = "|" + ("-" * 30)
                        lineWriteLeft = "-" * 87
                    elif l in range(5, 34):

                        if l < (5 + len(self.listTable)):
                            infoTable = self.listTable[l - 5].split(',')
                            accesStr = "PUBLIC"
                            if len(infoTable[5]) > 0:
                                accesStr = "PRIVE"
                            lineWriteLeft = "  " + str(l - 5 + 1) + (" " * (2 - len(str(l - 5 + 1)))) + " | " + infoTable[1] + (" " * (42 - len(infoTable[1]))) + " | MIN : " + infoTable[4] + " " + self.unite + (" " * (13 - len(infoTable[4] + " " + self.unite))) + " | " + "" + infoTable[2] + "/" + infoTable[3] + "" + " | " + accesStr + ""

                        if l < (5 + len(playerConnected)):
                            lineWriteRight = "| " + playerConnected[l - 5] + (" " * (30 - len(playerConnected[l - 5]) - 1))
                        else:
                            lineWriteRight = "|" + (" " * 30)




                for caseL in range(len(lineWriteLeft)):
                    line[1 + caseL] = lineWriteLeft[caseL]

                lineWriteRight = lineWriteRight[::-1]
                for caseL in range(len(lineWriteRight)):
                    line[len(line) - 1 - caseL - 1] = lineWriteRight[caseL]

                for caseL in range(len(lineWriteCenter)):
                    line[60 - len(lineWriteCenter) // 2 + caseL] = lineWriteCenter[caseL]

            lineStr = ""
            for lineS in line:
                lineStr += lineS
            print(lineStr)

    def DrawTable(self):

        listPlayer = self.GetPlayerList()
        playerLabel = []

        for player in listPlayer:
            playerLabel.append(self.GetPlayerLabelTable(player))

        print(playerLabel)

        cmdPossible = ["\p", "\\add", "\c", "\\allin"]

        for l in range(34):
            line = []
            if l < 4 or l >= 26:
                for c in range(120):
                    if l == 29 or l == 33 or l == 0 or l == 2:
                        line.append("-")
                    else:
                        line.append(" ")

                if l == 28:
                    phrase = "AU TOUR DE : barbieri"
                    for x in range(0, len(phrase)):
                        line[x] = phrase[x]

                    phrase = "MON ARGENT : " + self.MoneyFormat(self.GetMoneyPlayer(self.myPlayerName)) + " " + self.unite
                    phrase = phrase[::-1]

                    for x in range((len(line) - 1) - len(phrase) - 1 + 1, len(line) - 1):
                        line[x] = phrase[((len(line) - 1) - len(phrase) - 1) - x]

                if l == 31:
                    phrase  = "\p : pour suivre     \\add 200 : pour relancer     \c : pour ce coucher     \\allin : pour all in"
                    #phrase = "CE N'EST PAS VOTRE TOUR"
                    for x in range(0, len(phrase)):
                        line[(round(len(line) / 2) - round(len(phrase) / 2)) + x] = phrase[x]

                if l == 31:
                    phrase = "CE N'EST PAS VOTRE TOUR"
                    for x in range(0, len(phrase)):
                        pass
                        #line[(round(len(line) / 2) - round(len(phrase) / 2)) + x] = phrase[x]

                if l == 1:
                    phrase = "SALON : " + self.roomName
                    for x in range(0, len(phrase)):
                        line[0 + x] = phrase[x]

                    phrase = "JOUEUR : " + str(len(self.GetPlayerList())) + "/" + str(self.gameLimit)
                    phrase = phrase[::-1]
                    for x in range(0, len(phrase)):
                        line[(len(line) - 2) - x] = phrase[x]


            elif l < 26:
                if l == 4:
                    for c in range(120):
                        line.append(" ")

                    if len(self.GetPlayerList()) >= 1:
                        phrase = playerLabel[0]
                        for x in range(0, len(phrase)):
                            line[60 - (round(len(phrase) / 2)) + x] = phrase[x]

                elif l == 5:
                    for c in range(120):
                        line.append(" ")

                    if len(self.GetPlayerList()) >= 4:
                        phrase = self.MoneyFormat(self.GetPlayerInfos(listPlayer[0])[1]) + " " + self.unite
                        for x in range(0, len(phrase)):
                            line[60 - (round(len(phrase) / 2)) + x] = phrase[x]

                elif l == 11:
                    for c in range(120):
                            if c == 22:
                                line.append("|")
                            elif c == 98:
                                line.append("|")
                            else:
                                line.append(" ")

                    if len(self.GetPlayerList()) >= 6:
                        phrase = "[] []"
                        for x in range(0, len(phrase)):
                            line[90 + x] = phrase[x]

                        phrase = playerLabel[5]
                        for x in range(0, len(phrase)):
                            line[100 + x] = phrase[x]

                    if len(self.GetPlayerList()) >= 2:
                        phrase = "[] []"
                        for x in range(0, len(phrase)):
                            line[25 + x] = phrase[x]

                        phrase = playerLabel[1]
                        for x in range(0, len(phrase)):
                            line[(20 - len(phrase)) + x] = phrase[x]

                elif l == 18:

                    for c in range(120):
                            if c == 22:
                                line.append("|")
                            elif c == 98:
                                line.append("|")
                            else:
                                line.append(" ")

                    if len(self.GetPlayerList()) >= 5:
                        phrase = "[] []"
                        for x in range(0, len(phrase)):
                            line[90 + x] = phrase[x]

                        phrase = playerLabel[4]
                        for x in range(0, len(phrase)):
                            line[100 + x] = phrase[x]

                    if len(self.GetPlayerList()) >= 3:
                        phrase = "[] []"
                        for x in range(0, len(phrase)):
                            line[25 + x] = phrase[x]

                        phrase = playerLabel[2]
                        for x in range(0, len(phrase)):
                            line[(20 - len(phrase)) + x] = phrase[x]



                elif l == 24:
                    for c in range(120):
                        line.append(" ")

                    if len(self.GetPlayerList()) >= 4:
                        phrase = playerLabel[3]
                        for x in range(0, len(phrase)):
                            line[60 - (round(len(phrase) / 2)) + x] = phrase[x]

                elif l == 25:

                    for c in range(120):
                        line.append(" ")

                    if len(self.GetPlayerList()) >= 4:
                        phrase = self.MoneyFormat(self.GetPlayerInfos(listPlayer[3])[1]) + " " + self.unite
                        for x in range(0, len(phrase)):
                            line[60 - (round(len(phrase) / 2)) + x] = phrase[x]
                else:
                    colsLine = [10,12,13,14,15,16,17,19]
                    colsDiago = [6,7,8,9,19,20,21,22,23]
                    if l in colsLine:
                        for c in range(120):
                            if c == 22:
                                line.append("|")
                            elif c == 98:
                                line.append("|")
                            else:
                                line.append(" ")

                        if l == 13:
                            potStr = str(self.pot) + " " + self.unite
                            indexPot = 0
                            for carP in potStr:
                                line[60 - round(len(potStr) / 2) + indexPot] = carP
                                indexPot += 1

                        if l == 12:
                            if len(self.GetPlayerList()) >= 2:
                                moneyPlayer = self.MoneyFormat(self.GetPlayerInfos(listPlayer[1])[1]) + " " + self.unite
                                startPos = 20 - len(moneyPlayer)
                                for p in range(len(moneyPlayer)):
                                    line[startPos + p] = moneyPlayer[p]

                            if len(self.GetPlayerList()) >= 6:
                                moneyPlayer = self.MoneyFormat(self.GetPlayerInfos(listPlayer[5])[1]) + " " + self.unite
                                startPos = 100
                                for p in range(len(moneyPlayer)):
                                    line[startPos + p] = moneyPlayer[p]

                        if l == 19:

                            if len(self.GetPlayerList()) >= 3:
                                moneyPlayer = self.MoneyFormat(self.GetPlayerInfos(listPlayer[2])[1]) + " " + self.unite
                                startPos = 20 - len(moneyPlayer)
                                for p in range(len(moneyPlayer)):
                                    line[startPos + p] = moneyPlayer[p]

                            if len(self.GetPlayerList()) >= 5:
                                moneyPlayer = self.MoneyFormat(self.GetPlayerInfos(listPlayer[4])[1]) + " " + self.unite
                                startPos = 100
                                for p in range(len(moneyPlayer)):
                                    line[startPos + p] = moneyPlayer[p]

                        if l == 16:
                            tirageStr = []
                            tirage = ""
                            for cards in self.tirageCard:
                                tirageStr.append(self.TranslateCardsStr(cards))

                            for i in range(0, 5):
                                if len(tirageStr) > i:
                                    tirage += tirageStr[i] + "   "
                                else:
                                    tirage += "[]   "

                            tirageConv = tirage[:-1]
                            for i in range(len(tirageConv)):
                                line[61 - (len(tirageConv) // 2) + i] = tirageConv[i]


                    elif l in colsDiago:
                        for c in range(120):
                            if c in [22,23,24,95,96,97] and (l == 9 or l == 20):
                                line.append("-")
                            elif c in [25,26,27,94,93,92] and (l == 8 or l == 21):
                                line.append("-")
                            elif c in [28,29,30,91,90,89] and (l == 7 or l == 22):
                                line.append("-")
                            elif c in [int(i) for i in range(31,(100 - 11))] and (l == 6 or l == 23):
                                line.append("-")
                            else:
                                line.append(" ")

                        if l == 7:
                            if len(self.GetPlayerList()) >= 1:
                                phrase = "[] []"
                                for x in range(0, len(phrase)):
                                    line[58 + x] = phrase[x]

                        if l == 22:
                            if len(self.GetPlayerList()) >= 4:
                                phrase = "[] []"
                                for x in range(0, len(phrase)):
                                    line[58 + x] = phrase[x]


            line.append("|")
            lineStr = ""
            for car in line:
                lineStr += car
            print(lineStr)

        cmdValid = False

        while not cmdValid:
            cmd = input("VOTRE CHOIX : ")

            if cmd in cmdPossible or cmd[0:4] in cmdPossible:

                if cmd == "\p":
                    print("passe")
                    cmdValid = True
                elif cmd == "\c":
                    print("couche")
                    cmdValid = True
                elif cmd == "\\allin":
                    print("allin")
                    cmdValid = True
                else:
                    infoRelance = cmd.split(' ')
                    if infoRelance[0] == "\\add":
                        nbRelance = infoRelance[1]
                        if nbRelance.isdigit():
                            nbRelance = int(nbRelance)
                            if self.GetMoneyPlayer(self.myPlayerName) >= nbRelance:
                                print("Ajoute : " + str(nbRelance))
                                cmdValid = True
                            else:
                                print("Vous n'avez pas assez de " + self.unite)
                        else:
                            print("Vous devez ajouter une nombre et non un chiffre")

            if not cmdValid:
                print("Commande invalide")
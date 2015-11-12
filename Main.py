import sys, time

from pocker import Interface, Chat, Check, Data

Table = Interface.Interface(["barbieri", "dumontier", "martin", "ramos", "sodebo", "res"])
ChatLib = Chat.Chat()

Table.ChangeMoneyPlayer("barbieri", 5032)
Table.ChangeMoneyPlayer("dumontier", 1201)
Table.ChangeMoneyPlayer("martin", 12)
Table.ChangeMoneyPlayer("ramos", 25630)
Table.ChangeMoneyPlayer("sodebo", 1245)
Table.ChangeMoneyPlayer("res", 145236)
#print(Table.playerList)
#print(Table.GetMoneyPlayer("dumontier"))

#print(Table.GetPlayerList())

#print(Table.GetPlayerInfos("dumontier"))

#print(Table.GetPlayerCards("dumontier"))

#print(Table.TranslateCardsStr(11))

Table.AddCardTirage(112)

#FEr5p6
#poker
#94.23.15.139


#print(Table.MoneyFormat(152653))

ChatLib.addMessage("leo", "bonjour dd ad dzad ad", 'blue')

#print(ChatLib.listMsg[0][0])

statusDrawWelcome = 0
while Table.interfaceState == 0:
    Table.DrawWelcome(statusDrawWelcome, "")

    if statusDrawWelcome == 0:
        if not Check.CheckServer():
            statusDrawWelcome = 5
    elif statusDrawWelcome == 2:
        Table.listTable = Data.GetListTable()
    elif statusDrawWelcome == 3:
        Table.interfaceState = 1

    if statusDrawWelcome != 5:
        statusDrawWelcome += 1

    time.sleep(0.5)


if Table.interfaceState == 1:

    selectUser = ""

    Table.DrawMenu(0)

    while selectUser != "exit":
        selectUser = input()
        if selectUser == "\\reload":
            Table.DrawMenu(0)
        elif "\join" in selectUser:
            print("join\join")
        else:
            Table.ShowHelpMenu()



__author__ = 'Leo'

import urllib.request as req

def GetOnlinePlayer():

    list = []

    #proxy = req.ProxyHandler({'http': r'http://username:password@url:port'})
    #auth = req.HTTPBasicAuthHandler()
    #opener = req.build_opener(proxy, auth, req.HTTPHandler)
    #req.install_opener(opener)

    conn = req.urlopen('http://94.23.15.139/poker/onlinePlayers.php').read().decode()

    connList = conn.split('#')

    for player in connList:
        if len(player) > 0:
            list.append(player)

    return list

def GetListTable():

    list = []

    conn = req.urlopen('http://94.23.15.139/poker/listTables.php').read().decode()

    connList = conn.split('#')

    for player in connList:
        if len(player) > 0:
            list.append(player)

    return list


__author__ = 'Leo'

import urllib.request as req


def CheckServer():

    res = False

    #proxy = req.ProxyHandler({'http': r'http://username:password@url:port'})
    #auth = req.HTTPBasicAuthHandler()
    #opener = req.build_opener(proxy, auth, req.HTTPHandler)
    #req.install_opener(opener)

    conn = req.urlopen('http://94.23.15.139/poker/check.php').read().decode()

    if conn == "1":
        res = True

    return res
#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

import cryptocompare

def getCoinsList() :
    liste = []
    listOfCoins = cryptocompare.get_coin_list(format=True)
    for coin in listOfCoins:
        liste.append(coin)
    print(liste)

def getCoinPrice(coin):
    if (cryptocompare.get_price(coin)):
        price = cryptocompare.get_price(coin)
        print('\n',price.get(coin).get('EUR'), '€')
    else:
        if (coin == 'liste') :
            return
        else :    
            print('Il n\'y a aucune monnaie du nom de', coin,'\n')

print('\nBienvenue sur l\'outil qui permet de savoir le prix de toutes les cryptomonnaies. Commençons...\n')

while (True):
    question = input('\nPour voir l\'ensemble des monnaies, entrez "liste". \nPour quitter, tapez "quitter". \nPour voir le prix d\'une monnaie particulière, entrez son nom en majuscules.\n\n')

    if (question == 'liste'):
        getCoinsList()
    if (question == 'quitter'):
        exit()
    else:
        getCoinPrice(question)
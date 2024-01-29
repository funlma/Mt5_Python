# Si on active pas le traiding automatique sur 
# le terminal le code sort une erreur 
# de RETCODE=10027 

################ les imports ###################
import time
import MetaTrader5 as mt5


# établit une connexion avec le terminal MetaTrader 5
if not mt5.initialize():
    print("initialize () a échoué, code d'erreur =",mt5.last_error())
    quit()
#print("cool")

# prépare la structure de la requête d'achat
symbol = "EURUSD"
symbol_info = mt5.symbol_info(symbol)
if symbol_info is None:
    print(symbol, "non trouvé, ne peut pas appeler order_check()")
    mt5.shutdown()
    quit()

# si le symbole n'est pas disponible dans le MarketWatch, il est ajouté
if not symbol_info.visible:
    print(symbol, "n'est pas visible, tentative de l'afficher")
    if not mt5.symbol_select(symbol,True):
        print("symbol_select({}}) a échoué, sortie",symbol)
        mt5.shutdown()
        quit()

############## une position buy ################################
# les parametres pour la prise de position
lot = 0.1
point = mt5.symbol_info(symbol).point
price = mt5.symbol_info_tick(symbol).ask
deviation = 20
sl = price - 100 * point
tp = price + 100 * point
# la requete d'une position Buy
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": price,
    "sl": sl,
    "tp": tp,
    "deviation": deviation,
    "magic": 234000,
    "comment": "ouverture de position buy",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_RETURN,
}

# envoie une demande de prise de position
result = mt5.order_send(request)

# vérifie le résultat de l'exécution
print("1. order_send(): buy {} {} lots à {} avec une déviation={} points".format(symbol,lot,price,deviation));
# Si la position a echoue
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("2. order_send a échoué, retcode={}".format(result.retcode))
    print("shutdown() et sortie")
    mt5.shutdown()
    quit()
# Au cas ou la position executé
print("2. order_send terminé, ", result)
print("################### Buy ouverte ###########################")

time.sleep(2)
# crée une demande de fermeture
position_id=result.order
price=mt5.symbol_info_tick(symbol).bid
deviation=20
request={
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_SELL,
    "position": position_id,
    "price": price,
    "deviation": deviation,
    "magic": 234000,
    "comment": "python script close",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_RETURN,
}
# envoie une demande de fermeture de la position
result=mt5.order_send(request)
# vérifie le résultat de l'exécution
print("3. ferme la position #{} : sell {} {} lots à {} avec la déviation={} points".format(position_id,symbol,lot,price,deviation));
# si la fermeture echoue
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("4. order_send a échoué, retcode={}".format(result.retcode))
    print("   résultat",result)
else:
    # Au cas ou la fermeture reussi
    print("4. position #{} fermée, {}".format(position_id,result))

################# Une position Sell ##########################
lot = 0.1
point = mt5.symbol_info(symbol).point
price = mt5.symbol_info_tick(symbol).bid
deviation = 20
sl = price + 100 * point
tp = price - 100 * point
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_SELL,
    "price": price,
    "sl": sl,
    "tp": tp,
    "deviation": deviation,
    "magic": 234001,
    "comment": "ouverture de position sell",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_RETURN,
}
 
# envoie une demande de trading
result = mt5.order_send(request)
# vérifie le résultat de l'exécution
print("3. order_send(): buy {} {} lots à {} avec une déviation={} points".format(symbol,lot,price,deviation));
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("4. order_send a échoué, retcode={}".format(result.retcode))

print("################ Sell ouverte ##############################")

time.sleep(2)
# crée une demande de fermeture
position_id=result.order
price=mt5.symbol_info_tick(symbol).bid
deviation=20
request={
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "position": position_id,
    "price": price,
    "deviation": deviation,
    "magic": 234001,
    "comment": "python script close",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_RETURN,
}
# envoie une demande de fermeture de la position
result=mt5.order_send(request)
# vérifie le résultat de l'exécution
print("5. ferme la position #{} : sell {} {} lots à {} avec la déviation={} points".format(position_id,symbol,lot,price,deviation));
# si la fermeture echoue
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("6. order_send a échoué, retcode={}".format(result.retcode))
    print("   résultat",result)
else:
    # Au cas ou la fermeture reussi
    print("6. position #{} fermée, {}".format(position_id,result))

# ferme la connexion au terminal MetaTrader 5
mt5.shutdown()
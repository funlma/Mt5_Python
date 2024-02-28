import MetaTrader5 as mt5

# connect to MetaTrader5 account
mt5.initialize()

# get open positions
positions = mt5.positions_get()
#print(positions)

# fermer toute les positions
def close_position(position):

    tick = mt5.symbol_info_tick(position.symbol)

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "position": position.ticket,
        "symbol": position.symbol,
        "volume": position.volume,
        "type": mt5.ORDER_TYPE_BUY if position.type == 1 else mt5.ORDER_TYPE_SELL,
        "price": tick.ask if position.type == 1 else tick.bid,  
        "deviation": 20,
        "magic": 100,
        "comment": "python script close",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    # si la fermeture echoue
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("order_send a échoué, retcode={}".format(result.retcode))
        print("   résultat",result)
    else:
        # Au cas ou la fermeture reussi
        print("Position #{} fermée, {}".format(position.ticket,result))
    return 0

# fermer les positions sell
def close_sell(position):

    tick = mt5.symbol_info_tick(position.symbol)

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "position": position.ticket,
        "symbol": position.symbol,
        "volume": position.volume,
        "type": mt5.ORDER_TYPE_BUY,
        "price": tick.ask,  
        "deviation": 20,
        "magic": 100,
        "comment": "python script close",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    # si la fermeture echoue
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("order_send a échoué, retcode={}".format(result.retcode))
        print("   résultat",result)
    else:
        # Au cas ou la fermeture reussi
        print("Position #{} fermée, {}".format(position.ticket,result))

    return 0

def close_buy(position):

    tick = mt5.symbol_info_tick(position.symbol)

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "position": position.ticket,
        "symbol": position.symbol,
        "volume": position.volume,
        "type": mt5.ORDER_TYPE_SELL,
        "price": tick.bid,  
        "deviation": 20,
        "magic": 100,
        "comment": "python script close",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    # si la fermeture echoue
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("order_send a échoué, retcode={}".format(result.retcode))
        print("   résultat",result)
    else:
        # Au cas ou la fermeture reussi
        print("Position #{} fermée, {}".format(position.ticket,result))
    return 0

if __name__ == "__main__":
    for position in positions:
        print(position.type)
        if(position.type == 0):
            #close_sell(position)
            close_buy(position)
            pass
        else:
            pass
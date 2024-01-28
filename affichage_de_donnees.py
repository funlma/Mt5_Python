################## Les imports ##########################
import os
from dotenv import load_dotenv

from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import MetaTrader5 as mt5

# Charger les donnees du fichier .env
load_dotenv()

login_mt5 = os.getenv('login')
password_mt5 = os.getenv('password')

# connexion à MetaTrader 5
if not mt5.initialize():
    print("initialize() a échoué")
    mt5.shutdown()

# demande l'état et les paramètres de connexion
print(mt5.terminal_info())

print(f"Login: {login_mt5}")
print(f"Mot de passe: {password_mt5}")

# demande 1000 ticks à EURAUD
euraud_ticks = mt5.copy_ticks_from("EURAUD", datetime(2020,1,28,13), 1000, mt5.COPY_TICKS_ALL)
# demande les ticks de AUDUSD du 2019.04.01 13:00 au 2019.04.02 13:00
audusd_ticks = mt5.copy_ticks_range("AUDUSD", datetime(2020,1,27,13), datetime(2020,1,28,13), mt5.COPY_TICKS_ALL)

# récupère les barres de différents symboles de différentes manières
eurusd_rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_M1, datetime(2020,1,28,13), 1000)
eurgbp_rates = mt5.copy_rates_from_pos("EURGBP", mt5.TIMEFRAME_M1, 0, 1000)
eurcad_rates = mt5.copy_rates_range("EURCAD", mt5.TIMEFRAME_M1, datetime(2020,1,27,13), datetime(2020,1,28,13))
 



#Les donnees
# Ici nous affichons dans le terminal
# dix donnees des ticks de EURAUD et AUDUSD 
print('euraud_ticks(', len(euraud_ticks), ')')
for val in euraud_ticks[:10]: print(val)
 
print('audusd_ticks(', len(audusd_ticks), ')')
for val in audusd_ticks[:10]: print(val)

print('eurusd_rates(', len(eurusd_rates), ')')
for val in eurusd_rates[:10]: print(val)
 
print('eurgbp_rates(', len(eurgbp_rates), ')')
for val in eurgbp_rates[:10]: print(val)
 
print('eurcad_rates(', len(eurcad_rates), ')')
for val in eurcad_rates[:10]: print(val)

# ferme la connexion à MetaTrader 5
mt5.shutdown()

# Tracer les courbes des donnees 
# crée le DataFrame à partir des données obtenues
ticks_frame = pd.DataFrame(euraud_ticks)
# convertit le temps en secondes au format datetime
ticks_frame['time']=pd.to_datetime(ticks_frame['time'], unit='s')
# affiche les ticks sur le graphique
plt.plot(ticks_frame['time'], ticks_frame['ask'], 'r-', label='ask')
plt.plot(ticks_frame['time'], ticks_frame['bid'], 'b-', label='bid')
 
# affiche les légendes
plt.legend(loc='upper left')
 
# ajoute l'en-tête
plt.title('EURAUD ticks')
 
# affiche le graphique
plt.show()
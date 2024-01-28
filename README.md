# Metatrader 5 et python

Ce projet est un exercice sur la plateforme Metatrader 5 et son integration avec python

Installer Metatrader 5

Pour lire la documentation complete, se rendre sur:

https://www.mql5.com/fr/docs/python_metatrader5

## Installer les dependances

    $ pip install MetaTrader5

    $ pip install python-dotenv

    $ pip install matplotlib
    
    $ pip install pandas

Pour lire les variable du fichier dotenv je dois installer cette lib. Je vais ignorer le fichier .env dans le projet. 
Mais pour que le code marche la prochaine fois, je dois creer un fichier .env et Mettre les lignes suivante a l'interieur.

login=000000
password="motdepasse"
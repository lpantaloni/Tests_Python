import os
import getpass
import sys

def saluer(nom: str | None = None) -> None:
    """
    Affiche un message de salutation.

    si `nom` est fourni, on salue cette personne ;
    sinon on salue l'utilisateur connecté.
    """
    if nom:
        print(f"Bonjour {nom} !")
    else:
        utilisateur = getpass.getuser()
        print(f"Bonjour {utilisateur} !")

if __name__ == "__main__":
    # appel depuis la ligne de commande : premier argument facultatif
    if len(sys.argv) > 1:
        saluer(sys.argv[1])
    else:
        saluer()

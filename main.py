"""
CathLab Manager v1.0
Point d'entree de l'application. Initialise la base de donnees puis lance
l'interface graphique.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from app import database
from app.ui.login_window import LoginWindow
from app.ui.main_window import MainWindow


def main() -> None:
    database.init_db(seed=True)

    login = LoginWindow()
    login.mainloop()

    if not login.authenticated_user:
        return  # fenetre fermee sans connexion reussie

    app = MainWindow(current_user=login.authenticated_user)
    app.mainloop()


if __name__ == "__main__":
    main()

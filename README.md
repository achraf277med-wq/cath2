# CathLab Manager v1.0

Logiciel de gestion d'une salle de cardiologie interventionnelle.
100% hors ligne, base de donnees locale SQLite, generation de fiches
PDF de consommation.

## Compiler le .exe SANS RIEN INSTALLER (via GitHub Actions - recommande)

Cette methode compile l'exe sur un serveur Windows dans le cloud (gratuit).
Tu n'installes rien sur ton PC.

1. Creer un compte gratuit sur https://github.com si tu n'en as pas
2. Cliquer sur **"New repository"** (bouton vert en haut a droite)
   - Nom : `cathlab-manager` (ou ce que tu veux)
   - Laisser en **"Public"** ou **"Private"**, peu importe
   - Cliquer **"Create repository"**
3. Sur la page du nouveau depot, cliquer **"uploading an existing file"**
   (ou le lien "upload files")
4. Glisser-deposer le dossier **`cathlab_manager`** entier sur la zone
   d'upload (GitHub accepte de glisser un dossier complet et conserve son
   organisation interne). Si le glisser-deposer du dossier ne fonctionne
   pas dans ton navigateur, ouvre le dossier `cathlab_manager` et
   selectionne tout son contenu (Ctrl+A) puis glisse cette selection.
5. En bas de page, cliquer **"Commit changes"**
6. Aller dans l'onglet **"Actions"** en haut du depot
   - La compilation demarre automatiquement (icone orange qui tourne)
   - Attendre 2-3 minutes qu'elle devienne verte (coche verte = succes)
7. Cliquer sur le run termine, puis tout en bas sur
   **"CathLabManager-Windows"** dans la section "Artifacts"
   -> cela telecharge un zip contenant `CathLabManager.exe` pret a l'emploi
   -> decompresse-le puis deplace le dossier sur ton Bureau si tu veux
      l'avoir directement accessible (cette methode compile dans le cloud,
      elle ne peut pas deposer le resultat sur ton Bureau automatiquement)

A chaque fois que tu modifieras des fichiers et les redeposeras sur GitHub,
un nouvel exe sera automatiquement recompile dans l'onglet Actions.

## Compiler le .exe sur ta propre machine (alternative)

1. Installer **Python 3.13** depuis https://www.python.org/downloads/
   (cocher "Add python.exe to PATH" lors de l'installation)
2. Copier tout le dossier `cathlab_manager` sur la machine Windows
3. Double-cliquer sur **`build.bat`**
4. Le programme compile apparait **directement dans ce dossier**, a cote
   de `build.bat`, dans un sous-dossier `CathLabManager\CathLabManager.exe`

Aucune installation de Python n'est necessaire sur les postes qui utiliseront
ensuite l'application : il suffit de copier le dossier `CathLabManager`
(depose automatiquement a cote de build.bat apres compilation) entier
vers un autre poste (l'exe a besoin des fichiers a cote de lui).

## Premier lancement

Au tout premier demarrage, l'application demande de creer un compte
administrateur (nom d'utilisateur + mot de passe). Les lancements suivants
affichent un simple ecran de connexion. D'autres comptes (admin ou operateur)
peuvent ensuite etre crees depuis **Parametres > Utilisateurs de l'application**.

## Lancer en mode developpement (sans compiler)

```
pip install -r requirements.txt
python main.py
```

## Emplacement des donnees

- Base de donnees : `%USERPROFILE%\CathLabManager\cathlab.db`
- Fiches PDF generees : `%USERPROFILE%\CathLabManager\fiches\`

Ces dossiers sont crees automatiquement au premier lancement et persistent
entre les mises a jour du logiciel.

## Structure du projet

```
cathlab_manager/
    main.py                  Point d'entree
    app/
        database.py           Schema SQLite + acces bas niveau
        models.py              Couche Model (CRUD, logique metier)
        pdf_export.py          Generation de la fiche PDF
        ui/
            main_window.py      Fenetre principale + tableau de bord
            new_procedure_view.py
            history_view.py
            stock_view.py
            patients_view.py
            settings_view.py
    assets/
        logo.jpeg              Logo du CHU (extrait du modele Word fourni)
    build.spec                PyInstaller
    build.bat                 Script de compilation Windows en un clic
    requirements.txt
```

## Personnalisation de la fiche PDF

Les champs "Nom de l'etablissement", "Service" et "Unite" sont modifiables
depuis l'onglet **Parametres** de l'application. Le logo peut etre remplace
en ecrasant `assets/logo.jpeg` (meme nom de fichier) avant compilation.

## Notes

- Le stock est automatiquement decremente a chaque procedure enregistree.
- Une alerte rouge apparait dans le tableau de bord et dans la vue Stock
  des qu'un article passe sous son seuil d'alerte (5 par defaut).
- La fiche PDF reproduit la mise en page du document Word fourni en
  reference, avec une grande zone blanche en bas de page pour les
  etiquettes/stickers de tracabilite du materiel.

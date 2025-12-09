
https://github.com/user-attachments/assets/5a7c182a-be87-43db-bf23-19b1b6375d4e


# Space Invaders

A classic Space Invaders game developed in Python with Pygame.

## Features

- **Controls**: Move with Q/D or left/right arrows, shoot with Space
- **Main menu**: Play, Options, Quit
- **Options**:
  - Difficulty selection (Easy, Medium, Hard)
  - Language selection (French, English)
  - Display mode (Windowed, Fullscreen)
- **Power-ups**: Collect bonuses from destroyed enemies (speed boost, fast shoot, triple shoot)

## Installation

1. Install Python 3.8 or higher
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running

To run the game:

```bash
python main.py
```

## Controls

- **Q** or **Left Arrow**: Move spaceship left
- **D** or **Right Arrow**: Move spaceship right
- **Space**: Shoot
- **Up/Down Arrows**: Navigate menus
- **Enter**: Select in menus
- **Escape**: Return to menu (from options)

## Project Structure

- `main.py`: Main entry point
- `game.py`: Space Invaders game logic
- `menu.py`: Main menu
- `options.py`: Options menu
- `config.py`: Configuration and constants
- `requirements.txt`: Python dependencies

## Notes

- Game runs at 60 FPS
- Score increases based on selected difficulty
- Enemies move in synchronized formation
- Difficulty affects enemy speed and shooting frequency
- Some enemies drop power-ups when destroyed (15% chance)

---

# Space Invaders

Un jeu Space Invaders classique développé en Python avec Pygame.

## Fonctionnalités

- **Contrôles** : Déplacement avec Q/D ou flèches gauche/droite, tir avec Espace
- **Menu principal** : Jouer, Options, Quitter
- **Options** :
  - Choix de la difficulté (Facile, Moyen, Difficile)
  - Choix de la langue (Français, Anglais)
  - Mode d'affichage (Fenêtré, Plein écran)
- **Bonus** : Collectez des bonus sur les ennemis détruits (vitesse, tir rapide, tir triple)

## Installation

1. Installez Python 3.8 ou supérieur
2. Installez les dépendances :

```bash
pip install -r requirements.txt
```

## Lancement

Pour lancer le jeu :

```bash
python main.py
```

## Contrôles

- **Q** ou **Flèche gauche** : Déplacer le vaisseau vers la gauche
- **D** ou **Flèche droite** : Déplacer le vaisseau vers la droite
- **Espace** : Tirer
- **Flèches haut/bas** : Naviguer dans les menus
- **Entrée** : Sélectionner dans les menus
- **Échap** : Retour au menu (depuis les options)

## Structure du projet

- `main.py` : Point d'entrée principal
- `game.py` : Logique du jeu Space Invaders
- `menu.py` : Menu principal
- `options.py` : Menu des options
- `config.py` : Configuration et constantes
- `requirements.txt` : Dépendances Python

## Notes

- Le jeu fonctionne à 60 FPS
- Le score augmente selon la difficulté choisie
- Les ennemis se déplacent de manière synchronisée
- La difficulté affecte la vitesse des ennemis et leur fréquence de tir
- Certains ennemis laissent tomber des bonus quand ils sont détruits (15% de chance)

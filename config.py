SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

SHIP_WIDTH = 50
SHIP_HEIGHT = 40
SHIP_SPEED = 5

ENEMY_WIDTH = 40
ENEMY_HEIGHT = 30
ENEMY_SPEED_X = 2
ENEMY_SPEED_Y = 30
ENEMY_ROWS = 5
ENEMY_COLS = 10
ENEMY_SPACING = 10

BULLET_WIDTH = 5
BULLET_HEIGHT = 10
BULLET_SPEED = 7
ENEMY_BULLET_SPEED = 5

BONUS_WIDTH = 30
BONUS_HEIGHT = 30
BONUS_SPEED = 3
BONUS_DROP_CHANCE = 0.15
BONUS_DURATION = 10000
SHOOT_COOLDOWN_NORMAL = 500
SHOOT_COOLDOWN_FAST = 200
SPEED_BOOST = 2

DIFFICULTY_SETTINGS = {
  "facile": {
    "enemy_speed": 1,
    "enemy_bullet_speed": 3,
    "enemy_shoot_chance": 0.0005,
    "points_per_enemy": 10
  },
  "moyen": {
    "enemy_speed": 2,
    "enemy_bullet_speed": 5,
    "enemy_shoot_chance": 0.001,
    "points_per_enemy": 20
  },
  "difficile": {
    "enemy_speed": 3,
    "enemy_bullet_speed": 7,
    "enemy_shoot_chance": 0.002,
    "points_per_enemy": 30
  }
}

TEXTS = {
  "français": {
    "menu_title": "SPACE INVADERS",
    "play": "Jouer",
    "options": "Options",
    "quit": "Quitter",
    "difficulty": "Difficulté",
    "language": "Langue",
    "easy": "Facile",
    "medium": "Moyen",
    "hard": "Difficile",
    "score": "Score",
    "game_over": "GAME OVER",
    "press_any_key": "Appuyez sur une touche pour continuer",
    "victory": "VICTOIRE !",
    "back": "Retour",
    "change": "Changer",
    "navigate": "Naviguer",
    "display": "Affichage",
    "windowed": "Fenêtré",
    "fullscreen": "Plein écran"
  },
  "anglais": {
    "menu_title": "SPACE INVADERS",
    "play": "Play",
    "options": "Options",
    "quit": "Quit",
    "difficulty": "Difficulty",
    "language": "Language",
    "easy": "Easy",
    "medium": "Medium",
    "hard": "Hard",
    "score": "Score",
    "game_over": "GAME OVER",
    "press_any_key": "Press any key to continue",
    "victory": "VICTORY !",
    "back": "Back",
    "change": "Change",
    "navigate": "Navigate",
    "display": "Display",
    "windowed": "Windowed",
    "fullscreen": "Fullscreen"
  }
}

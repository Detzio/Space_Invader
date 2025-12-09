import pygame
import menu
import game
import options

pygame.init()

def create_screen(display_mode):
  import config
  if display_mode == "plein_ecran":
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.FULLSCREEN)
  else:
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
  return screen

def main():
  current_difficulty = "moyen"
  current_language = "français"
  current_display_mode = "fenetre"
  
  screen = create_screen(current_display_mode)
  pygame.display.set_caption("Space Invaders")
  
  current_state = "menu"
  
  running = True
  while running:
    if current_state == "menu":
      menu_screen = menu.Menu(screen, current_language)
      result = menu_screen.run()
      
      if result == "quit":
        running = False
      elif result == "play":
        current_state = "game"
      elif result == "options":
        current_state = "options"
        
    elif current_state == "options":
      options_screen = options.Options(screen, current_difficulty, current_language, current_display_mode)
      result, new_difficulty, new_language, new_display_mode = options_screen.run()
      
      if result == "quit":
        running = False
      elif result == "menu":
        if new_display_mode != current_display_mode:
          current_display_mode = new_display_mode
          screen = create_screen(current_display_mode)
          pygame.display.set_caption("Space Invaders")
        current_difficulty = new_difficulty
        current_language = new_language
        current_state = "menu"
        
    elif current_state == "game":
      game_instance = game.Game(screen, current_difficulty, current_language)
      result = game_instance.run()
      
      if result == "quit":
        running = False
      elif result == "menu":
        current_state = "menu"
        
  pygame.quit()

if __name__ == "__main__":
  main()

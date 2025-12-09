import pygame
import config

class Menu:
  
  def __init__(self, screen, language="français"):
    self.screen = screen
    self.language = language
    self.texts = config.TEXTS[language]
    
    self.options = ["play", "options", "quit"]
    self.selected_option = 0
    
    self.title_font = pygame.font.Font(None, 72)
    self.option_font = pygame.font.Font(None, 48)
    
      
  def draw(self):
    self.screen.fill(config.BLACK)
    
    title_text = self.title_font.render(self.texts["menu_title"], True, config.WHITE)
    title_rect = title_text.get_rect(center=(config.SCREEN_WIDTH // 2, 150))
    self.screen.blit(title_text, title_rect)
    
    y_offset = 300
    spacing = 80
    
    for i, option in enumerate(self.options):
      option_text = self.texts[option]
      
      color = config.GREEN if i == self.selected_option else config.WHITE
      
      if i == self.selected_option:
        display_text = f"> {option_text}"
      else:
        display_text = f"  {option_text}"
        
      text_surface = self.option_font.render(display_text, True, color)
      text_rect = text_surface.get_rect(center=(config.SCREEN_WIDTH // 2, y_offset + i * spacing))
      self.screen.blit(text_surface, text_rect)
      
  def run(self):
    clock = pygame.time.Clock()
    last_key_time = 0
    
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return "quit"
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
            selected = self.options[self.selected_option]
            if selected == "play":
              return "play"
            elif selected == "options":
              return "options"
            elif selected == "quit":
              return "quit"
          elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            current_time = pygame.time.get_ticks()
            if current_time - last_key_time > 200:
              if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
              elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
              last_key_time = current_time
          
      self.draw()
      pygame.display.flip()
      
      clock.tick(60)

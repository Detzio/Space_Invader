import pygame
import config

class Options:
  
  def __init__(self, screen, current_difficulty="moyen", current_language="français", current_display_mode="fenetre"):
    self.screen = screen
    self.difficulty = current_difficulty
    self.language = current_language
    self.display_mode = current_display_mode
    self.texts = config.TEXTS[current_language]
    
    self.difficulties = ["facile", "moyen", "difficile"]
    self.languages = ["français", "anglais"]
    self.display_modes = ["fenetre", "plein_ecran"]
    
    self.selected_category = 0
    self.selected_index = {
      "difficulty": self.difficulties.index(self.difficulty),
      "language": self.languages.index(self.language),
      "display": self.display_modes.index(self.display_mode)
    }
    
    self.title_font = pygame.font.Font(None, 48)
    self.option_font = pygame.font.Font(None, 36)
    
  def handle_key(self, key):
    if key == pygame.K_LEFT:
      if self.selected_category == 0:
        self.selected_index["difficulty"] = (self.selected_index["difficulty"] - 1) % len(self.difficulties)
        self.difficulty = self.difficulties[self.selected_index["difficulty"]]
      elif self.selected_category == 1:
        self.selected_index["language"] = (self.selected_index["language"] - 1) % len(self.languages)
        self.language = self.languages[self.selected_index["language"]]
        self.texts = config.TEXTS[self.language]
      elif self.selected_category == 2:
        self.selected_index["display"] = (self.selected_index["display"] - 1) % len(self.display_modes)
        self.display_mode = self.display_modes[self.selected_index["display"]]
        
    elif key == pygame.K_RIGHT:
      if self.selected_category == 0:
        self.selected_index["difficulty"] = (self.selected_index["difficulty"] + 1) % len(self.difficulties)
        self.difficulty = self.difficulties[self.selected_index["difficulty"]]
      elif self.selected_category == 1:
        self.selected_index["language"] = (self.selected_index["language"] + 1) % len(self.languages)
        self.language = self.languages[self.selected_index["language"]]
        self.texts = config.TEXTS[self.language]
      elif self.selected_category == 2:
        self.selected_index["display"] = (self.selected_index["display"] + 1) % len(self.display_modes)
        self.display_mode = self.display_modes[self.selected_index["display"]]
        
    elif key == pygame.K_UP:
      self.selected_category = (self.selected_category - 1) % 3
    elif key == pygame.K_DOWN:
      self.selected_category = (self.selected_category + 1) % 3
      
  def draw(self):
    self.screen.fill(config.BLACK)
    
    title_text = self.title_font.render(self.texts["options"], True, config.WHITE)
    title_rect = title_text.get_rect(center=(config.SCREEN_WIDTH // 2, 100))
    self.screen.blit(title_text, title_rect)
    
    y_difficulty = 250
    self.draw_category(
      self.texts["difficulty"],
      self.difficulties,
      self.selected_index["difficulty"],
      y_difficulty,
      self.selected_category == 0
    )
    
    y_language = 300
    self.draw_category(
      self.texts["language"],
      self.languages,
      self.selected_index["language"],
      y_language,
      self.selected_category == 1
    )
    
    y_display = 350
    self.draw_category(
      self.texts["display"],
      self.display_modes,
      self.selected_index["display"],
      y_display,
      self.selected_category == 2
    )
    
    instruction_font = pygame.font.Font(None, 24)
    instructions = [
      self.texts["back"] + ": ESC",
      "← →: " + self.texts["change"],
      "↑ ↓: " + self.texts["navigate"]
    ]
    y_instructions = 480
    for i, instruction in enumerate(instructions):
      text = instruction_font.render(instruction, True, config.WHITE)
      text_rect = text.get_rect(center=(config.SCREEN_WIDTH // 2, y_instructions + i * 30))
      self.screen.blit(text, text_rect)
      
  def draw_category(self, label, values, selected_index, y_pos, is_selected):
    label_color = config.GREEN if is_selected else config.WHITE
    label_text = self.option_font.render(label + ":", True, label_color)
    label_rect = label_text.get_rect(center=(config.SCREEN_WIDTH // 2 - 150, y_pos))
    self.screen.blit(label_text, label_rect)
    
    x_start = config.SCREEN_WIDTH // 2
    spacing = 120
    
    for i, value in enumerate(values):
      if label == self.texts["difficulty"]:
        difficulty_map = {
          "facile": "easy",
          "moyen": "medium",
          "difficile": "hard"
        }
        display_value = self.texts[difficulty_map[value]]
      elif label == self.texts["display"]:
        display_map = {
          "fenetre": "windowed",
          "plein_ecran": "fullscreen"
        }
        display_value = self.texts[display_map[value]]
      else:
        display_value = value.capitalize()
        
      if i == selected_index:
        color = config.GREEN if is_selected else config.YELLOW
        display_value = f"[{display_value}]"
      else:
        color = config.WHITE
        
      value_text = self.option_font.render(display_value, True, color)
      value_rect = value_text.get_rect(center=(x_start + i * spacing, y_pos))
      self.screen.blit(value_text, value_rect)
      
  def run(self):
    clock = pygame.time.Clock()
    last_key_time = 0
    
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return "quit", self.difficulty, self.language, self.display_mode
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            return "menu", self.difficulty, self.language, self.display_mode
          elif event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
            current_time = pygame.time.get_ticks()
            if current_time - last_key_time > 200:
              self.handle_key(event.key)
              last_key_time = current_time
          
      self.draw()
      pygame.display.flip()
      
      clock.tick(60)

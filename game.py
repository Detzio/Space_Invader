

import pygame
import random
import config

class Ship:

  def __init__(self, x, y):
    
    self.x = x
    self.y = y
    self.width = config.SHIP_WIDTH
    self.height = config.SHIP_HEIGHT
    self.base_speed = config.SHIP_SPEED
    self.speed = config.SHIP_SPEED

    self.has_speed_boost = False
    self.has_fast_shoot = False
    self.has_triple_shoot = False
    
  def move_left(self):

    if self.x > 0:
      self.x -= self.speed
      
  def move_right(self):

    if self.x < config.SCREEN_WIDTH - self.width:
      self.x += self.speed
      
  def get_rect(self):
    
    return pygame.Rect(self.x, self.y, self.width, self.height)
    
  def draw(self, screen):
    
    center_x = self.x + self.width // 2
    bottom_y = self.y + self.height

    nose_points = [
      (center_x, self.y),  
      (center_x - 8, self.y + 10),
      (center_x - 15, self.y + 20),
      (center_x - 12, bottom_y - 5),
      (center_x, bottom_y),  
      (center_x + 12, bottom_y - 5),
      (center_x + 15, self.y + 20),
      (center_x + 8, self.y + 10)
    ]

    pygame.draw.polygon(screen, (0, 100, 0), nose_points)

    pygame.draw.polygon(screen, (0, 180, 0), nose_points)

    cockpit_points = [
      (center_x, self.y + 5),
      (center_x - 6, self.y + 15),
      (center_x, self.y + 20),
      (center_x + 6, self.y + 15)
    ]
    pygame.draw.polygon(screen, (100, 200, 255), cockpit_points)

    pygame.draw.polygon(screen, (0, 220, 0), [
      (center_x - 15, self.y + 20),
      (center_x - 20, self.y + 15),
      (center_x - 12, self.y + 25)
    ])
    pygame.draw.polygon(screen, (0, 220, 0), [
      (center_x + 15, self.y + 20),
      (center_x + 20, self.y + 15),
      (center_x + 12, self.y + 25)
    ])

    pygame.draw.circle(screen, (255, 200, 0), (center_x - 8, bottom_y - 3), 2)
    pygame.draw.circle(screen, (255, 200, 0), (center_x + 8, bottom_y - 3), 2)

    pygame.draw.polygon(screen, (150, 255, 150), nose_points, 1)

class Enemy:

  def __init__(self, x, y, has_bonus=False):
    self.x = x
    self.y = y
    self.width = config.ENEMY_WIDTH
    self.height = config.ENEMY_HEIGHT
    self.has_bonus = has_bonus  
    
  def get_rect(self):
    
    return pygame.Rect(self.x, self.y, self.width, self.height)
    
  def draw(self, screen):
    
    center_x = self.x + self.width // 2
    top_y = self.y

    ship_points = [
      (center_x, self.y + self.height),  
      (center_x - 8, self.y + self.height - 10),
      (center_x - 12, self.y + self.height - 20),
      (center_x - 10, self.y + 5),
      (center_x, top_y),  
      (center_x + 10, self.y + 5),
      (center_x + 12, self.y + self.height - 20),
      (center_x + 8, self.y + self.height - 10)
    ]

    pygame.draw.polygon(screen, (100, 0, 0), ship_points)

    pygame.draw.polygon(screen, (180, 0, 0), ship_points)

    cockpit_points = [
      (center_x, top_y + 5),
      (center_x - 6, top_y + 15),
      (center_x, top_y + 20),
      (center_x + 6, top_y + 15)
    ]
    pygame.draw.polygon(screen, (255, 100, 100), cockpit_points)

    pygame.draw.polygon(screen, (200, 0, 0), [
      (center_x - 12, self.y + self.height - 20),
      (center_x - 18, self.y + self.height - 25),
      (center_x - 10, self.y + self.height - 15)
    ])
    pygame.draw.polygon(screen, (200, 0, 0), [
      (center_x + 12, self.y + self.height - 20),
      (center_x + 18, self.y + self.height - 25),
      (center_x + 10, self.y + self.height - 15)
    ])

    pygame.draw.circle(screen, (255, 150, 0), (center_x - 6, top_y + 8), 2)
    pygame.draw.circle(screen, (255, 150, 0), (center_x + 6, top_y + 8), 2)

    pygame.draw.polygon(screen, (255, 150, 150), ship_points, 1)

class Bullet:

  def __init__(self, x, y, is_player_bullet=True, speed=None):
    self.x = x
    self.y = y
    self.width = config.BULLET_WIDTH
    self.height = config.BULLET_HEIGHT
    self.is_player_bullet = is_player_bullet

    if speed is not None:
      self.speed = speed
    else:
      self.speed = config.BULLET_SPEED if is_player_bullet else config.ENEMY_BULLET_SPEED
    
  def update(self):
    
    if self.is_player_bullet:
      
      self.y -= self.speed
    else:
      
      self.y += self.speed
      
  def get_rect(self):
    
    return pygame.Rect(self.x, self.y, self.width, self.height)
    
  def draw(self, screen):
    
    color = config.GREEN if self.is_player_bullet else config.YELLOW
    pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
    
  def is_off_screen(self):
    
    return self.y < 0 or self.y > config.SCREEN_HEIGHT

class Bonus:

  def __init__(self, x, y, bonus_type):
    self.x = x
    self.y = y
    self.width = config.BONUS_WIDTH
    self.height = config.BONUS_HEIGHT
    self.speed = config.BONUS_SPEED
    self.type = bonus_type  
    
  def update(self):
    
    self.y += self.speed
    
  def get_rect(self):
    
    return pygame.Rect(self.x, self.y, self.width, self.height)
    
  def draw(self, screen):

    if self.type == "speed":
      color = config.BLUE
    elif self.type == "fast_shoot":
      color = config.YELLOW
    elif self.type == "triple_shoot":
      color = config.GREEN
    else:
      color = config.WHITE

    pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height), 2)
    
    center_x = self.x + self.width // 2
    center_y = self.y + self.height // 2
    
    if self.type == "speed":
      
      pygame.draw.polygon(screen, color, [
        (center_x - 5, center_y - 5),
        (center_x + 5, center_y),
        (center_x - 5, center_y + 5)
      ])
    elif self.type == "fast_shoot":
      
      pygame.draw.lines(screen, color, False, [
        (center_x - 5, center_y - 5),
        (center_x, center_y),
        (center_x - 3, center_y),
        (center_x + 5, center_y + 5)
      ], 2)
    elif self.type == "triple_shoot":
      
      for i in range(3):
        pygame.draw.circle(screen, color, (center_x - 6 + i * 6, center_y), 3)
        
  def is_off_screen(self):
    
    return self.y > config.SCREEN_HEIGHT

class Explosion:

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.frame = 0
    self.max_frames = 15  
    self.particles = []
    self.create_particles()
    
  def create_particles(self):
    
    import math
    
    for i in range(20):
      angle = (2 * math.pi * i) / 20
      speed = random.uniform(2, 5)
      self.particles.append({
        "x": self.x,
        "y": self.y,
        "vx": math.cos(angle) * speed,
        "vy": math.sin(angle) * speed,
        "life": self.max_frames,
        "size": random.randint(3, 6)
      })
      
  def update(self):
    
    self.frame += 1

    for particle in self.particles:
      particle["x"] += particle["vx"]
      particle["y"] += particle["vy"]
      particle["life"] -= 1
      
      particle["vx"] *= 0.95
      particle["vy"] *= 0.95
      
  def is_finished(self):
    
    return self.frame >= self.max_frames
    
  def draw(self, screen):

    if self.frame < self.max_frames // 2:
      
      radius = int(self.frame * 3)
      alpha = 255 - (self.frame * 255 // (self.max_frames // 2))
    else:
      
      radius = int((self.max_frames - self.frame) * 3)
      alpha = 0

    if radius > 0:
      
      color_intensity = min(255, alpha)
      color = (255, min(200, color_intensity), 0)
      pygame.draw.circle(screen, color, (int(self.x), int(self.y)), radius)
      pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), radius // 2)

    for particle in self.particles:
      if particle["life"] > 0:
        
        life_ratio = particle["life"] / self.max_frames
        color_intensity = int(255 * life_ratio)
        color = (255, min(200, color_intensity), 0)
        size = max(1, int(particle["size"] * life_ratio))
        pygame.draw.circle(screen, color, (int(particle["x"]), int(particle["y"])), size)

class Game:

  def __init__(self, screen, difficulty="moyen", language="français"):
    self.screen = screen
    self.difficulty = difficulty
    self.language = language
    self.texts = config.TEXTS[language]

    self.difficulty_settings = config.DIFFICULTY_SETTINGS[difficulty]

    ship_x = (config.SCREEN_WIDTH - config.SHIP_WIDTH) // 2
    ship_y = config.SCREEN_HEIGHT - config.SHIP_HEIGHT - 20
    self.ship = Ship(ship_x, ship_y)

    self.enemies = []
    self.create_enemies()

    self.player_bullets = []
    self.enemy_bullets = []

    self.active_bonuses = []

    self.explosions = []

    self.score = 0
    self.game_over = False
    self.victory = False
    self.clock = pygame.time.Clock()

    self.enemy_direction = 1

    self.last_shot_time = 0
    self.shoot_cooldown = config.SHOOT_COOLDOWN_NORMAL

    self.bonus_timers = {
      "speed": 0,
      "fast_shoot": 0,
      "triple_shoot": 0
    }

    self.stars = []
    self.generate_stars()

    self.background_surface = None
    self.generate_background()
    
  def generate_stars(self):
    
    for _ in range(100):  
      x = random.randint(0, config.SCREEN_WIDTH)
      y = random.randint(0, config.SCREEN_HEIGHT)
      brightness = random.randint(150, 255)
      size = random.randint(1, 2)
      self.stars.append({"x": x, "y": y, "brightness": brightness, "size": size})
      
  def generate_background(self):
    
    import math
    
    self.background_surface = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    self.background_surface.fill((10, 5, 20))  

    nebula_center_x = config.SCREEN_WIDTH // 3
    nebula_center_y = config.SCREEN_HEIGHT // 2
    nebula_radius = 300
    
    for i in range(200):
      angle = random.uniform(0, 2 * math.pi)
      distance = random.uniform(0, nebula_radius)
      x = int(nebula_center_x + distance * math.cos(angle))
      y = int(nebula_center_y + distance * math.sin(angle))
      
      if 0 <= x < config.SCREEN_WIDTH and 0 <= y < config.SCREEN_HEIGHT:
        
        intensity = 1 - (distance / nebula_radius)
        r = int(50 + intensity * 30)
        g = int(20 + intensity * 40)
        b = int(80 + intensity * 100)

        color = (min(255, r), min(255, g), min(255, b))
        size = random.randint(2, 5)
        pygame.draw.circle(self.background_surface, color, (x, y), size)

    nebula2_center_x = config.SCREEN_WIDTH * 2 // 3
    nebula2_center_y = config.SCREEN_HEIGHT // 3
    nebula2_radius = 250
    
    for i in range(150):
      angle = random.uniform(0, 2 * math.pi)
      distance = random.uniform(0, nebula2_radius)
      x = int(nebula2_center_x + distance * math.cos(angle))
      y = int(nebula2_center_y + distance * math.sin(angle))
      
      if 0 <= x < config.SCREEN_WIDTH and 0 <= y < config.SCREEN_HEIGHT:
        intensity = 1 - (distance / nebula2_radius)
        r = int(100 + intensity * 80)
        g = int(30 + intensity * 50)
        b = int(50 + intensity * 70)
        
        color = (min(255, r), min(255, g), min(255, b))
        size = random.randint(2, 4)
        pygame.draw.circle(self.background_surface, color, (x, y), size)

    for star in self.stars:
      pygame.draw.circle(self.background_surface, (star["brightness"], star["brightness"], star["brightness"]), 
                        (star["x"], star["y"]), star["size"])
    
  def create_enemies(self):
    
    self.enemies = []
    start_x = 50
    start_y = 50

    for row in range(config.ENEMY_ROWS):
      for col in range(config.ENEMY_COLS):
        x = start_x + col * (config.ENEMY_WIDTH + config.ENEMY_SPACING)
        y = start_y + row * (config.ENEMY_HEIGHT + config.ENEMY_SPACING)
        
        has_bonus = random.random() < config.BONUS_DROP_CHANCE
        self.enemies.append(Enemy(x, y, has_bonus))
        
  def handle_input(self, keys):

    if keys[pygame.K_q] or keys[pygame.K_LEFT]:
      self.ship.move_left()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
      self.ship.move_right()
      
  def shoot(self):
    
    current_time = pygame.time.get_ticks()

    if current_time - self.last_shot_time < self.shoot_cooldown:
      return
      
    self.last_shot_time = current_time

    base_x = self.ship.x + self.ship.width // 2 - config.BULLET_WIDTH // 2
    bullet_y = self.ship.y
    
    if self.ship.has_triple_shoot:
      
      self.player_bullets.append(Bullet(base_x, bullet_y, True))
      self.player_bullets.append(Bullet(base_x - 15, bullet_y, True))
      self.player_bullets.append(Bullet(base_x + 15, bullet_y, True))
    else:
      
      self.player_bullets.append(Bullet(base_x, bullet_y, True))
    
  def update_enemies(self):
    
    if not self.enemies:
      return

    move_down = False
    for enemy in self.enemies:
      if enemy.x <= 0 or enemy.x + enemy.width >= config.SCREEN_WIDTH:
        move_down = True
        
        self.enemy_direction *= -1
        break

    speed = self.difficulty_settings["enemy_speed"]
    for enemy in self.enemies:
      enemy.x += speed * self.enemy_direction
      if move_down:
        enemy.y += config.ENEMY_SPEED_Y

    for enemy in self.enemies:
      if enemy.y + enemy.height >= self.ship.y:
        self.game_over = True
        return

    for enemy in self.enemies:
      if random.random() < self.difficulty_settings["enemy_shoot_chance"]:
        bullet_x = enemy.x + enemy.width // 2 - config.BULLET_WIDTH // 2
        bullet_y = enemy.y + enemy.height
        
        enemy_bullet_speed = self.difficulty_settings["enemy_bullet_speed"]
        self.enemy_bullets.append(Bullet(bullet_x, bullet_y, False, enemy_bullet_speed))
        
  def update_bullets(self):

    for bullet in self.player_bullets[:]:
      bullet.update()
      if bullet.is_off_screen():
        self.player_bullets.remove(bullet)

    for bullet in self.enemy_bullets[:]:
      bullet.update()
      if bullet.is_off_screen():
        self.enemy_bullets.remove(bullet)
        
  def check_collisions(self):

    for bullet in self.player_bullets[:]:
      bullet_rect = bullet.get_rect()
      for enemy in self.enemies[:]:
        if bullet_rect.colliderect(enemy.get_rect()):
          
          enemy_x = enemy.x + enemy.width // 2
          enemy_y = enemy.y + enemy.height // 2
          had_bonus = enemy.has_bonus

          self.explosions.append(Explosion(enemy_x, enemy_y))
          
          self.enemies.remove(enemy)
          self.player_bullets.remove(bullet)
          
          self.score += self.difficulty_settings["points_per_enemy"]

          if had_bonus:
            bonus_type = random.choice(["speed", "fast_shoot", "triple_shoot"])
            bonus_x = enemy_x - config.BONUS_WIDTH // 2
            self.active_bonuses.append(Bonus(bonus_x, enemy_y, bonus_type))
          break

    ship_rect = self.ship.get_rect()
    for bullet in self.enemy_bullets[:]:
      if bullet.get_rect().colliderect(ship_rect):
        
        ship_x = self.ship.x + self.ship.width // 2
        ship_y = self.ship.y + self.ship.height // 2
        self.explosions.append(Explosion(ship_x, ship_y))

        self.game_over = True
        self.enemy_bullets.remove(bullet)
        return

    for bonus in self.active_bonuses[:]:
      if bonus.get_rect().colliderect(ship_rect):
        
        self.apply_bonus(bonus.type)
        self.active_bonuses.remove(bonus)

    if not self.enemies:
      self.victory = True
      
  def apply_bonus(self, bonus_type):
    
    current_time = pygame.time.get_ticks()
    
    if bonus_type == "speed":
      self.ship.has_speed_boost = True
      self.ship.speed = self.ship.base_speed * config.SPEED_BOOST
      self.bonus_timers["speed"] = current_time + config.BONUS_DURATION
    elif bonus_type == "fast_shoot":
      self.ship.has_fast_shoot = True
      self.shoot_cooldown = config.SHOOT_COOLDOWN_FAST
      self.bonus_timers["fast_shoot"] = current_time + config.BONUS_DURATION
    elif bonus_type == "triple_shoot":
      self.ship.has_triple_shoot = True
      self.bonus_timers["triple_shoot"] = current_time + config.BONUS_DURATION
      
  def update_bonuses(self):
    
    current_time = pygame.time.get_ticks()

    for bonus in self.active_bonuses[:]:
      bonus.update()
      if bonus.is_off_screen():
        self.active_bonuses.remove(bonus)

    if self.ship.has_speed_boost and current_time > self.bonus_timers["speed"]:
      self.ship.has_speed_boost = False
      self.ship.speed = self.ship.base_speed
      
    if self.ship.has_fast_shoot and current_time > self.bonus_timers["fast_shoot"]:
      self.ship.has_fast_shoot = False
      self.shoot_cooldown = config.SHOOT_COOLDOWN_NORMAL
      
    if self.ship.has_triple_shoot and current_time > self.bonus_timers["triple_shoot"]:
      self.ship.has_triple_shoot = False
      
  def draw(self):

    if self.background_surface:
      self.screen.blit(self.background_surface, (0, 0))
    else:
      self.screen.fill(config.BLACK)

    for star in self.stars:
      
      brightness = star["brightness"] + random.randint(-20, 20)
      brightness = max(100, min(255, brightness))
      color = (brightness, brightness, brightness)
      pygame.draw.circle(self.screen, color, (star["x"], star["y"]), star["size"])

    self.ship.draw(self.screen)

    for enemy in self.enemies:
      enemy.draw(self.screen)

    for bullet in self.player_bullets:
      bullet.draw(self.screen)
    for bullet in self.enemy_bullets:
      bullet.draw(self.screen)

    for bonus in self.active_bonuses:
      bonus.draw(self.screen)

    for explosion in self.explosions:
      explosion.draw(self.screen)

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"{self.texts['score']}: {self.score}", True, config.WHITE)
    self.screen.blit(score_text, (10, 10))

    self.draw_active_bonuses()

    if self.game_over:
      self.draw_game_over()
    elif self.victory:
      self.draw_victory()
      
  def draw_game_over(self):
    
    font_large = pygame.font.Font(None, 72)
    font_small = pygame.font.Font(None, 36)

    game_over_text = font_large.render(self.texts["game_over"], True, config.RED)
    text_rect = game_over_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
    self.screen.blit(game_over_text, text_rect)

    instruction_text = font_small.render(self.texts["press_any_key"], True, config.WHITE)
    instruction_rect = instruction_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 60))
    self.screen.blit(instruction_text, instruction_rect)
    
  def draw_victory(self):
    
    font_large = pygame.font.Font(None, 72)
    font_small = pygame.font.Font(None, 36)

    victory_text = font_large.render(self.texts["victory"], True, config.GREEN)
    text_rect = victory_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
    self.screen.blit(victory_text, text_rect)

    score_text = font_small.render(f"{self.texts['score']}: {self.score}", True, config.WHITE)
    score_rect = score_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 60))
    self.screen.blit(score_text, score_rect)

    instruction_text = font_small.render(self.texts["press_any_key"], True, config.WHITE)
    instruction_rect = instruction_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 100))
    self.screen.blit(instruction_text, instruction_rect)
    
  def update(self):
    
    if self.game_over or self.victory:
      return

    self.update_enemies()

    self.update_bullets()

    self.update_bonuses()

    for explosion in self.explosions[:]:
      explosion.update()
      if explosion.is_finished():
        self.explosions.remove(explosion)

    self.check_collisions()
    
  def draw_active_bonuses(self):
    
    font = pygame.font.Font(None, 24)
    y_offset = 50
    x_offset = 10
    
    if self.ship.has_speed_boost:
      
      speed_text = font.render("Vitesse", True, config.BLUE)
      self.screen.blit(speed_text, (x_offset, y_offset))
      y_offset += 25
      
    if self.ship.has_fast_shoot:
      
      fast_text = font.render("Tir rapide", True, config.YELLOW)
      self.screen.blit(fast_text, (x_offset, y_offset))
      y_offset += 25
      
    if self.ship.has_triple_shoot:
      
      triple_text = font.render("Tir triple", True, config.GREEN)
      self.screen.blit(triple_text, (x_offset, y_offset))
    
  def run(self):
    
    running = True
    
    while running:
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return "quit"
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE and not self.game_over and not self.victory:
            
            self.shoot()
          elif (self.game_over or self.victory) and event.key:
            
            return "menu"

      keys = pygame.key.get_pressed()
      self.handle_input(keys)

      self.update()

      self.draw()
      pygame.display.flip()

      self.clock.tick(60)
      
    return "quit"


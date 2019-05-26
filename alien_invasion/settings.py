class Settings:
  """a class to store all settings for alien invasion"""
  def __init__(self):
    """initialize the game's settings."""
    self.screen_width = 900
    self.screen_height = 600
    self.bg_color = (230, 230, 230)
    self.ship_speed = 5.0
    self.bullet_speed = 50
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = (60,60,60)
    self.bullet_allowed = 3

    self.alien_speed = 13
    self.fleet_drop_speed = 10
    # fleet_direction of 1 represents right; -1 for left
    self.fleet_direction = 1

    self.ship_limit = 1





















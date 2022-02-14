from dataclasses import dataclass


@dataclass
class Skills:
    love: int
    education: int
    luck: int
    health: int
    money: int
    illegal: int

    def __init__(self, love=0, education=0, luck=0, health=0, money=0, illegal=0):
        self.love = love
        self.education = education
        self.luck = luck
        self.health = health
        self.money = money
        self.illegal = illegal


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (30, 30, 30)

def draw_text(string, x, y, screen, FONT):
    skill_text = FONT.render(string, True, BLACK)
    parallaxe(screen, skill_text, x, y)

def parallaxe(window, image, position_x, bg_position_y):
    window.blit(image, (position_x, bg_position_y))

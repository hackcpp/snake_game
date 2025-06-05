import pygame
import random
import sys
import os
from typing import Tuple, List

print("Starting game initialization...")

# 初始化 Pygame
pygame.init()
print("Pygame initialized")

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 设置游戏窗口
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLOCK_SIZE = 20
GAME_SPEED = 10

print("Creating game window...")
# 创建游戏窗口
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.DOUBLEBUF)
pygame.display.set_caption('贪吃蛇游戏')
print("Game window created")

# 初始化时钟
clock = pygame.time.Clock()

# 定义方向
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class GameState:
    PLAYING = 0
    GAME_OVER = 1

class Snake:
    def __init__(self):
        self.reset()

    def get_head_position(self) -> Tuple[int, int]:
        return self.positions[0]

    def update(self) -> bool:
        cur = self.get_head_position()
        x, y = self.direction
        new_x = cur[0] + (x * BLOCK_SIZE)
        new_y = cur[1] + (y * BLOCK_SIZE)
        
        # 检查是否撞到边界
        if (new_x < 0 or new_x >= WINDOW_WIDTH or 
            new_y < 0 or new_y >= WINDOW_HEIGHT):
            return False
            
        new = (new_x, new_y)
        
        # 检查是否撞到自己
        if new in self.positions[3:]:
            return False
        
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()
        return True

    def reset(self) -> None:
        self.length = 1
        self.positions = [(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
        self.color = GREEN

    def render(self, surface: pygame.Surface) -> None:
        for p in self.positions:
            pygame.draw.rect(surface, self.color, 
                           (p[0], p[1], BLOCK_SIZE, BLOCK_SIZE))

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self) -> None:
        self.position = (
            random.randint(0, (WINDOW_WIDTH-BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE,
            random.randint(0, (WINDOW_HEIGHT-BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE
        )

    def render(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, self.color, 
                        (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

def handle_input(snake: Snake, game_state: int) -> int:
    """处理用户输入"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit event received")
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            print(f"Key pressed: {event.key}, unicode: {getattr(event, 'unicode', '')}")
            # 允许在任意状态下按 Q/q 退出
            if event.key == pygame.K_q or getattr(event, 'unicode', '').lower() == 'q':
                print("Quitting game by Q/q")
                pygame.quit()
                sys.exit(0)
            if game_state == GameState.PLAYING:
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.direction = DOWN
                elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT
            elif game_state == GameState.GAME_OVER:
                if event.key == pygame.K_SPACE:
                    print("Restarting game")
                    snake.reset()  # 重置蛇的位置和状态
                    return GameState.PLAYING
    return game_state

def render_game(snake: Snake, food: Food, font: pygame.font.Font, game_state: int) -> None:
    """渲染游戏画面"""
    screen.fill(BLACK)
    snake.render(screen)
    food.render(screen)
    
    # 显示分数
    score_text = font.render(f'Score: {snake.score}', True, WHITE)
    screen.blit(score_text, (10, 10))
    
    # 如果游戏结束，显示结束信息
    if game_state == GameState.GAME_OVER:
        game_over_text = font.render('Game Over!', True, RED)
        restart_text = font.render('Press SPACE to restart', True, WHITE)
        quit_text = font.render('Press Q to quit', True, WHITE)
        
        screen.blit(game_over_text, 
                   (WINDOW_WIDTH//2 - game_over_text.get_width()//2, 
                    WINDOW_HEIGHT//2 - 60))
        screen.blit(restart_text, 
                   (WINDOW_WIDTH//2 - restart_text.get_width()//2, 
                    WINDOW_HEIGHT//2))
        screen.blit(quit_text, 
                   (WINDOW_WIDTH//2 - quit_text.get_width()//2, 
                    WINDOW_HEIGHT//2 + 40))
    
    pygame.display.flip()

def main() -> None:
    """游戏主循环"""
    print("Starting main game loop")
    snake = Snake()
    food = Food()
    game_state = GameState.PLAYING
    
    # 使用系统默认字体，确保中文显示正常
    try:
        font = pygame.font.SysFont('microsoftyaheimicrosoftyaheiui', 36)
    except:
        font = pygame.font.Font(None, 36)  # 如果找不到中文字体，使用默认字体

    print("Entering game loop")
    running = True
    while running:
        try:
            game_state = handle_input(snake, game_state)

            if game_state == GameState.PLAYING:
                # 更新蛇的位置
                if not snake.update():
                    game_state = GameState.GAME_OVER

                # 检查是否吃到食物
                if snake.get_head_position() == food.position:
                    snake.length += 1
                    snake.score += 1
                    food.randomize_position()

            render_game(snake, food, font, game_state)
            clock.tick(GAME_SPEED)
        except Exception as e:
            print(f"Error in game loop: {e}")
            running = False

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error occurred: {e}")
        input("Press Enter to exit...")
    finally:
        pygame.quit()
        sys.exit(0)

 
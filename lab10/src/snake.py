import pygame as py
import sys
import random
from psycopg2 import Error

from config import load_config
from database_connect import connect

py.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
SNAKE_SIZE = 20
INITIAL_SPEED = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

font = py.font.SysFont(None, 40)

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = (0, 0)
        self.color = GREEN
        self.score = 0
        self.level = 1
        self.speed = INITIAL_SPEED

    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % SCREEN_WIDTH), (cur[1] + (y * GRID_SIZE)) % SCREEN_HEIGHT)

        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def change_direction(self, dir):
        if dir == py.K_UP and self.direction != (0, 1):
            self.direction = (0, -1)
        if dir == py.K_DOWN and self.direction != (0, -1):
            self.direction = (0, 1)
        if dir == py.K_LEFT and self.direction != (1, 0):
            self.direction = (-1, 0)
        if dir == py.K_RIGHT and self.direction != (-1, 0):
            self.direction = (1, 0)

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([py.K_UP, py.K_DOWN, py.K_LEFT, py.K_RIGHT])
        self.score = 0
        self.level = 1
        self.speed = INITIAL_SPEED

    def increase_length(self, score):
        self.length += 1
        self.score += score
        if self.score % 3 == 0:
            self.level += 1
            self.speed += 1

    def draw(self, surface):
        for p in self.positions:
            r = py.Rect((p[0], p[1]), (SNAKE_SIZE, SNAKE_SIZE))
            py.draw.rect(surface, self.color, r)
            py.draw.rect(surface, WHITE, r, 1)

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.weight = random.randint(1, 3)
        self.position = (random.randint(0, (SCREEN_WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                         random.randint(0, (SCREEN_HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)

    def draw(self, surface):
        r = py.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        py.draw.rect(surface, self.color, r)
        py.draw.rect(surface, WHITE, r, 1)


screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption("Snake Game")

snake = Snake()
food = Food()

def create_tables():
    try:
        config = load_config()
        connection = connect(config)
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_scores (
                id SERIAL PRIMARY KEY,
                user_id INT REFERENCES users(id),
                score INT,
                level INT,
                CONSTRAINT fk_user_score FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
        connection.commit()

    except Error as e:
        print("Ошибка при создании таблиц:", e)

    finally:
        if connection:
            cursor.close()
            connection.close()

def create_user(username):
    try:
        config = load_config()
        connection = connect(config)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cursor.fetchone()[0]

        connection.commit()
        return user_id
    except Error as e:
        print("Ошибка при создании пользователя:", e)
        return None

    finally:
        if connection:
            cursor.close()
            connection.close()

def get_user_by_name(username):
    try:
        config = load_config()
        connection = connect(config)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user:
            user_info = {
                "id": user[0],
                "username": user[1]
            }
            return user_info
        else:
            print("Пользователь с таким именем не найден.")
            return None

    except Error as e:
        print("Ошибка при получении пользователя:", e)
        return None

    finally:
        if connection:
            cursor.close()
            connection.close()

def get_user_level(username):
    try:
        config = load_config()
        connection = connect(config)
        cursor = connection.cursor()

        cursor.execute("SELECT level FROM users WHERE username = %s", (username,))
        level = cursor.fetchone()

        if level:
            return level[0]
        else:
            print("Пользователь не найден.")
            return None

    except Error as e:
        print("Ошибка при получении уровня пользователя:", e)
        return None

    finally:
        if connection:
            cursor.close()
            connection.close()

def update_user_score(username, score, level):
    try:
        config = load_config()
        connection = connect(config)
        cursor = connection.cursor()

        cursor.execute("UPDATE user_scores SET score = %s, level = %s WHERE user_id = (SELECT id FROM users WHERE username = %s)", (score, level, username))
        connection.commit()
    except Error as e:
        print("Ошибка при обновлении результатов игры пользователя:", e)

    finally:
        if connection:
            cursor.close()
            connection.close()

def game():
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            elif event.type == py.KEYDOWN:
                snake.change_direction(event.key)

        snake.move()

        if snake.positions[0] == food.position:
            snake.increase_length(food.weight)
            food.randomize_position()

        if snake.positions[0][0] < 0 or snake.positions[0][0] >= SCREEN_WIDTH or \
                snake.positions[0][1] < 0 or snake.positions[0][1] >= SCREEN_HEIGHT:
            snake.reset()

        screen.fill(BLACK)

        snake.draw(screen)
        food.draw(screen)

        score_text = font.render(f"Score: {snake.score}", True, WHITE)
        level_text = font.render(f"Level: {snake.level}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 50))

        py.display.update()

        py.time.Clock().tick(snake.speed)

if __name__ == "__main__":
    create_tables()
    username = input("Введите имя пользователя: ")

    user = get_user_by_name(username)        

    if user:
        level = get_user_level(username)
        if level:
            print(f"Текущий уровень пользователя: {level}")
        game()
    else:
        user_id = create_user(username)
        if user_id:
            level = 0
            print(f"Текущий уровень пользователя: {level}")
            game()

            score = snake.score
            level = snake.level
            update_user_score(username, score, level)

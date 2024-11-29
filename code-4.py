import pygame
import random
# Initialize Pygame
pygame.init()
# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CAR_WIDTH, CAR_HEIGHT = 40, 60
# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Autonomous Vehicle Simulation")
clock = pygame.time.Clock()

# Define Classes
class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5

    def move(self):
        self.y -= self.speed

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, CAR_WIDTH, CAR_HEIGHT))

class Obstacle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, speed):
        self.y -= speed

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

# Main function
def main():
    # Initialize car in the middle bottom of the screen
    car = Car(WIDTH // 2 - CAR_WIDTH // 2, HEIGHT - CAR_HEIGHT - 20)
    obstacles = []
    score = 0

    running = True
    while running:
        screen.fill(WHITE)

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Generate Obstacles at random intervals
        if random.randint(0, 100) < 5:
            obstacle_width = random.randint(20, 100)
            obstacle_height = random.randint(20, 100)
            obstacle_x = random.randint(0, WIDTH - obstacle_width)
            obstacle_y = HEIGHT
            obstacles.append(Obstacle(obstacle_x, obstacle_y, obstacle_width, obstacle_height))

        # Move and Draw Car
        car.move()
        car.draw()

        # Move, Draw and Check Collision for Obstacles
        for obstacle in obstacles[:]:
            obstacle.move(car.speed)
            obstacle.draw()

            # Collision Detection
            if (car.x < obstacle.x + obstacle.width and
                car.x + CAR_WIDTH > obstacle.x and
                car.y < obstacle.y + obstacle.height and
                car.y + CAR_HEIGHT > obstacle.y):
                print("Collision! Game Over.")
                running = False

            # Remove off-screen obstacles and update score
            if obstacle.y < -obstacle.height:
                obstacles.remove(obstacle)
                score += 1  # Increase score for each avoided obstacle

        # Display Score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update Screen
        pygame.display.flip()
        clock.tick(30)  # 30 FPS for smoother gameplay

    pygame.quit()

if __name__ == "__main__":
    main()

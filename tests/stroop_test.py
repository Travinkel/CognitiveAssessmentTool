import pygame
import random
import time
import csv

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stroop Test")

# Colors for the test
COLORS = {
    "RED": (255, 0, 0),
    "BLUE": (0, 0, 255),
    "GREEN": (0, 255, 0),
    "YELLOW": (255, 255, 0),
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255)
}

# Font settings
font = pygame.font.Font(None, 80)
instruction_font = pygame.font.Font(None, 30)

# Word-color pairs
WORDS = ["RED", "BLUE", "GREEN", "YELLOW"]
RESPONSES = {"r": "RED", "b": "BLUE", "g": "GREEN", "y": "YELLOW"}

# Store results
results = []

# Game loop
def run_stroop_test():
    running = True
    start_time = time.time()
    while running:
        screen.fill(COLORS["WHITE"])

        # Select a random word and color
        word = random.choice(WORDS)
        color = random.choice(list(COLORS.keys())[:4])

        # Render text
        text = font.render(word, True, COLORS[color])
        screen.blit(text, (WIDTH//3, HEIGHT//3))

        # Instructions
        instruction_text = instruction_font.render("Press R, B, G, Y to match color", True, COLORS["BLACK"])
        screen.blit(instruction_text, (WIDTH//4, HEIGHT - 50))

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.name(event.key)
                if key_pressed in RESPONSES:
                    response_time = time.time() - start_time
                    correct = RESPONSES[key_pressed] == color
                    results.append([word, color, RESPONSES[key_pressed], correct, round(response_time, 3)])
                    start_time = time.time()

        pygame.time.delay(500)

    pygame.quit()

    # Save results
    with open("data/results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Word", "Color", "User Response", "Correct", "Response Time"])
        writer.writerows(results)

    print("Results saved to data/results.csv")

# Run the test
if __name__ == "__main__":
    run_stroop_test()
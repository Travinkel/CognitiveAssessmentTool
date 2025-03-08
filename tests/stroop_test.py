import pygame
import random
import time
import csv

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scientific Stroop Test")

# Font settings
font = pygame.font.Font(None, 80)
instruction_font = pygame.font.Font(None, 30)

# Colors for test
COLORS = {
    "RED": (255, 0, 0),
    "BLUE": (0, 0, 255),
    "GREEN": (0, 255, 0),
    "YELLOW": (255, 255, 0),
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255)
}

# Word-color pairs
WORDS = ["RED", "BLUE", "GREEN", "YELLOW"]
EMOTIONAL_WORDS = ["ANGER", "MURDER", "FEAR", "DEATH"]  # Emotional Stroop
NEUTRAL_WORDS = ["CHAIR", "TABLE", "PENCIL", "WATER"]  # Control

RESPONSES = {"r": "RED", "b": "BLUE", "g": "GREEN", "y": "YELLOW"}

# Store results
results = []

def show_stimulus(text, color):
    """ Displays word stimulus in the center of the screen """
    screen.fill(COLORS["WHITE"])
    rendered_text = font.render(text, True, COLORS[color])
    screen.blit(rendered_text, (WIDTH // 3, HEIGHT // 3))
    pygame.display.flip()

def run_stroop_test(condition="color-word"):
    """ Main Stroop Test Function """
    running = True
    trial_count = 10  # Set a limited number of trials
    for _ in range(trial_count):
        # Choose condition
        if condition == "color-word":
            word = random.choice(WORDS)
            color = random.choice(list(COLORS.keys())[:4])
        elif condition == "emotional":
            word = random.choice(EMOTIONAL_WORDS + NEUTRAL_WORDS)
            color = "BLACK"  # Emotional test uses black text

        show_stimulus(word, color)
        
        # Start timing
        start_time = time.time()
        response = None

        while response is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    return
                
                if event.type == pygame.KEYDOWN:
                    key_pressed = pygame.key.name(event.key)
                    if key_pressed in RESPONSES:
                        response_time = time.time() - start_time
                        correct = RESPONSES[key_pressed] == color
                        results.append([word, color, RESPONSES[key_pressed], correct, round(response_time, 3)])
                        response = key_pressed

        pygame.time.delay(1000)  # Short delay before next trial

    # Save results
    with open("data/results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Word", "Color", "User Response", "Correct", "Response Time"])
        writer.writerows(results)

    print("Results saved to data/results.csv")

# Run test
if __name__ == "__main__":
    # Choose "color-word" or "emotional"
    run_stroop_test(condition="color-word")  # Or change to "emotional"

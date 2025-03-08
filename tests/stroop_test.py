import pygame
import random
import time
import json
import os

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stroop Test")

# Colors
COLOR_MAP = {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0)
}

COLOR_NAMES = list(COLOR_MAP.keys())

# Font
font = pygame.font.Font(None, 72)

# Instructions
def show_instructions():
    screen.fill((0, 0, 0))
    instructions = [
        "STROOP TEST",
        "Identify the color of the word, NOT the word itself.",
        "Press: R for Red, G for Green, B for Blue, Y for Yellow.",
        "Press SPACE to start."
    ]
    for i, text in enumerate(instructions):
        rendered_text = font.render(text, True, (255, 255, 255))
        screen.blit(rendered_text, (50, 100 + (i * 80)))
    pygame.display.flip()

# Test function
def stroop_test():
    show_instructions()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

    # Experiment setup
    trials = 10
    results = []
    
    for _ in range(trials):
        word = random.choice(COLOR_NAMES)
        color_name = random.choice(COLOR_NAMES)
        color = COLOR_MAP[color_name]

        # Display word
        screen.fill((0, 0, 0))
        text = font.render(word, True, color)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()

        # Time measurement
        start_time = time.time()
        response = None

        while response is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    key_map = {
                        pygame.K_r: "Red",
                        pygame.K_g: "Green",
                        pygame.K_b: "Blue",
                        pygame.K_y: "Yellow"
                    }
                    if event.key in key_map:
                        response = key_map[event.key]
                        reaction_time = time.time() - start_time
                        results.append({
                            "word": word,
                            "color": color_name,
                            "response": response,
                            "correct": response == color_name,
                            "reaction_time": reaction_time
                        })

        time.sleep(0.5)

    # Save results
    save_results(results)
    pygame.quit()

# Save results to JSON
def save_results(results):
    file_path = os.path.join("data", "results.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
    else:
        data = {}

    data["stroop_test"] = results

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print("\nResults saved to 'data/results.json'.")

# Run test
if __name__ == "__main__":
    stroop_test()

import random
import time
import json
import os
import pygame

RESULTS_DIR = "results"
if not os.path.exists(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)

# Define color mapping
COLORS = {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
}

# Generate congruent and incongruent trials
def generate_stroop_trials(num_trials=10):
    trials = []
    words = list(COLORS.keys())

    for _ in range(num_trials // 2):  # Half congruent
        word = random.choice(words)
        trials.append((word, word))  # Word and color are the same

    for _ in range(num_trials // 2):  # Half incongruent
        word = random.choice(words)
        color = random.choice([c for c in words if c != word])  # Different color
        trials.append((word, color))

    random.shuffle(trials)  # Randomize order
    return trials

def run_color_word_stroop():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Color-Word Stroop Test")
    font = pygame.font.Font(None, 72)

    trials = generate_stroop_trials()
    results = []

    for word, color in trials:
        screen.fill((255, 255, 255))
        text_surface = font.render(word, True, COLORS[color])
        text_rect = text_surface.get_rect(center=(300, 200))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()

        start_time = time.time()
        response = None

        while response is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        response = "Red"
                    elif event.key == pygame.K_g:
                        response = "Green"
                    elif event.key == pygame.K_b:
                        response = "Blue"
                    elif event.key == pygame.K_y:
                        response = "Yellow"

        reaction_time = time.time() - start_time
        correct = (response == color)
        results.append({
            "word": word,
            "color": color,
            "response": response,
            "correct": correct,
            "reaction_time": reaction_time
        })

    pygame.quit()

    # Save results
    filename = os.path.join(RESULTS_DIR, f"stroop_cw_{int(time.time())}.json")
    with open(filename, "w") as file:
        json.dump({"stroop_test": results}, file, indent=4)

    print(f"\nResults saved: {filename}")


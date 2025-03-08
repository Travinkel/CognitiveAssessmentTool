import random
import time
import json
import os
import csv
import pygame

# Directories
RESULTS_DIR = "results"
IMAGES_DIR = "images"

# Ensure results directory exists
if not os.path.exists(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)

# Load validated Snodgrass & Vanderwart images
IMAGE_WORDS = {
    "Dog": "dog.png",
    "Cat": "cat.png",
    "Car": "car.png",
    "Tree": "tree.png",
    "Bird": "bird.png",
    "Chair": "chair.png",
    "House": "house.png",
    "Key": "key.png",
    "Lamp": "lamp.png",
    "Clock": "clock.png",
    # Extend with all 260 images
}

# Dynamically assign keys for responses
KEY_MAPPING = {
    pygame.K_1: "Dog", pygame.K_2: "Cat", pygame.K_3: "Car", pygame.K_4: "Tree",
    pygame.K_5: "Bird", pygame.K_6: "Chair", pygame.K_7: "House", pygame.K_8: "Key",
    pygame.K_9: "Lamp", pygame.K_0: "Clock"
}

def generate_pw_stroop_trials(num_trials=20, congruent_ratio=0.5):
    """Generate a mix of congruent and incongruent trials."""
    trials = []
    words = list(IMAGE_WORDS.keys())
    num_congruent = int(num_trials * congruent_ratio)
    num_incongruent = num_trials - num_congruent

    # Generate congruent trials
    for _ in range(num_congruent):
        word = random.choice(words)
        trials.append((word, IMAGE_WORDS[word], "congruent"))

    # Generate incongruent trials
    for _ in range(num_incongruent):
        word = random.choice(words)
        image = random.choice([IMAGE_WORDS[w] for w in words if w != word])
        trials.append((word, image, "incongruent"))

    random.shuffle(trials)
    return trials

def run_picture_word_stroop(num_trials=20, congruent_ratio=0.5):
    """Run the Picture-Word Stroop Task with word superimposed on the image."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Picture-Word Stroop Test")
    font = pygame.font.Font(None, 72)  # Larger font for readability

    trials = generate_pw_stroop_trials(num_trials, congruent_ratio)
    results = []

    for word, image_file, trial_type in trials:
        screen.fill((255, 255, 255))

        # Load and resize image
        image_path = os.path.join(IMAGES_DIR, image_file)
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (400, 400))  # Larger image size
        screen.blit(image, (200, 100))  # Center the image

        # Display word superimposed on the image
        text_surface = font.render(word, True, (255, 0, 0))  # Red text for contrast
        text_rect = text_surface.get_rect(center=(400, 300))  # Center over the image
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
                    if event.key in KEY_MAPPING:
                        response = KEY_MAPPING[event.key]

        reaction_time = time.time() - start_time
        correct = (response == word)
        results.append({
            "word": word,
            "image": image_file,
            "trial_type": trial_type,
            "response": response,
            "correct": correct,
            "reaction_time": reaction_time
        })

    pygame.quit()

    # Save results to JSON
    json_filename = os.path.join(RESULTS_DIR, f"stroop_pw_{int(time.time())}.json")
    with open(json_filename, "w") as file:
        json.dump({"picture_word_stroop": results}, file, indent=4)
    
    # Save results to CSV
    csv_filename = os.path.join(RESULTS_DIR, f"stroop_pw_{int(time.time())}.csv")
    with open(csv_filename, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["word", "image", "trial_type", "response", "correct", "reaction_time"])
        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved:\nJSON: {json_filename}\nCSV: {csv_filename}")


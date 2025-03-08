import pandas as pd
import os

# Ensure the script runs from the correct directory
script_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(script_dir, "Snodgrass_Vanderwart_labels.csv")

# Data dictionary with 260 image labels
data = {
    "Number": list(range(1, 261)),  # Numbers from 1 to 260
    "Concept": [
        "Accordion", "Airplane", "Alligator", "Anchor", "Ant", "Apple", "Arm", "Arrow",
        "Artichoke", "Ashtray", "Asparagus", "Axe", "Baby carriage", "Ball", "Balloon",
        "Banana", "Barn", "Barrel", "Baseball bat", "Basket", "Bear", "Bed", "Bee", "Beetle",
        "Bell", "Belt", "Bicycle", "Bird", "Blouse", "Book", "Boot", "Bottle", "Bow", "Bowl",
        "Box", "Bread", "Broom", "Brush", "Bus", "Butterfly", "Button", "Cake", "Camel",
        "Candle", "Cannon", "Cap", "Car", "Carrot", "Cat", "Caterpillar", "Celery", "Chain",
        "Chair", "Cherry", "Chicken", "Chisel", "Church", "Cigar", "Cigarette", "Clock",
        "Clothespin", "Cloud", "Clown", "Coat", "Comb", "Corn", "Couch", "Cow", "Crown",
        "Cup", "Deer", "Desk", "Dog", "Doll", "Donkey", "Door", "Doorknob", "Dress", "Dresser",
        "Drum", "Duck", "Eagle", "Ear", "Elephant", "Envelope", "Eye", "Fence", "Finger",
        "Fish", "Flag", "Flower", "Flute", "Fly", "Foot", "Football", "Football helmet",
        "Fork", "Fox", "French horn", "Frog", "Frying pan", "Garbage can", "Giraffe",
        "Glass", "Glasses", "Glove", "Goat", "Gorilla", "Grapes", "Grasshopper", "Guitar",
        "Gun", "Hair", "Hammer", "Hand", "Hanger", "Harp", "Hat", "Heart", "Helicopter",
        "Horse", "House", "Iron", "Ironing board", "Jacket", "Kangaroo", "Kettle", "Key",
        "Kite", "Knife", "Ladder", "Lamp", "Leaf", "Leg", "Lemon", "Leopard", "Lettuce",
        "Light bulb", "Light switch", "Lion", "Lips", "Lobster", "Lock", "Mitten", "Monkey",
        "Moon", "Motorcycle", "Mountain", "Mouse", "Mushroom", "Nail", "Nail file",
        "Necklace", "Needle", "Nose", "Nut", "Onion", "Orange", "Ostrich", "Owl",
        "Paintbrush", "Pants", "Peach", "Peacock", "Peanut", "Pear", "Pen", "Pencil",
        "Penguin", "Pepper", "Piano", "Pig", "Pineapple", "Pipe", "Pitcher", "Pliers",
        "Plug", "Pocketbook", "Pot", "Potato", "Pumpkin", "Rabbit", "Raccoon", "Record player",
        "Refrigerator", "Rhinoceros", "Ring", "Rocking chair", "Roller skate", "Rolling pin",
        "Rooster", "Ruler", "Sailboat", "Saltshaker", "Sandwich", "Saw", "Scissors",
        "Screw", "Screwdriver", "Sea horse", "Seal", "Sheep", "Shirt", "Shoe", "Skirt",
        "Skunk", "Sled", "Snail", "Snake", "Snowman", "Sock", "Spider", "Spinning wheel",
        "Spool of thread", "Spoon", "Squirrel", "Star", "Stool", "Stove", "Strawberry",
        "Suitcase", "Sun", "Swan", "Sweater", "Swing", "Table", "Telephone", "Television",
        "Tennis racket", "Thimble", "Thumb", "Tie", "Tiger", "Toaster", "Toe", "Tomato",
        "Toothbrush", "Top", "Traffic light", "Train", "Tree", "Truck", "Trumpet", "Turtle",
        "Umbrella", "Vase", "Vest", "Violin", "Wagon", "Watch", "Watering can", "Watermelon",
        "Well", "Wheel", "Whistle", "Windmill", "Window", "Wineglass", "Wrench", "Zebra"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save as CSV in the script's directory
df.to_csv(output_file, index=False)

# Confirm file save
print(f"CSV file saved successfully at: {output_file}")

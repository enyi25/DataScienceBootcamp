# Define the rooms and their descriptions
rooms = {
    # Storage (fuel rod can be picked up here)
    "Room 1": {
        "description": "You have found the Storage Room. You look around and see nothing of interest. \nThere are doors to the north, south, and east.",
        "n": "Room 10",
        "s": "Room 5",
        "e": "Room 2",
        "item": "fuel rod"  # Fuel rod is in the room initially
    },
    # Engine
    "Room 2": {
        "description": "You're in what looks like an Engine Room. A massive crystalline reactor pulses with energy. There are doors to the west and the east.",
        "w": "Room 1",
        "e": "Room 3",
        "power_on": False  # Track if the power is on in the engine room
    },
    # Northern Hallway
    "Room 3": {
        "description": "You have reached the Northern Hallway. You look around and see a cool corridor with windows showing Earth below.\nGlowing pipes line the ceiling.\nYou can follow the hallway south, there are doors to the east, and west.",
        "w": "Room 2",
        "s": "Room 7",
        "e": "Room 4",
    },
    # Medbay
    "Room 4": {
        "description": "You are in the Medbay. The Medical bay is filled with hovering diagnostic machines and strange examination pods.\nYou can exit to the west.",
        "w": "Room 3",
    },
    # Navigation
    "Room 5": {
        "description": "You've discovered the Navigation Room. Panoramic windows offer a breathtaking view of the stars.\nThere is a door to the north and the east.",
        "n": "Room 1",
        "e": "Room 6",
    },
    # Control Room
    "Room 6": {
        "description": "You have found the UFO's Control room. You want to leave quickly before the aliens find you. There is a door to the west and the east.",
        "w": "Room 5",
        "e": "Room 7",
    },
    # Middle Hallway
    "Room 7": {
        "description": "You have arrived in the Middle Hallway. This is the central hub of the UFO and has a rotating holographic galaxy map. You may follow the hallway to the north or south, there is a door to the west.",
        "n": "Room 3",
        "w": "Room 6",
        "s": "Room 9",
    },
    # Cafeteria
    "Room 8": {
        "description": "You arrive in the Cafeteria. This is an alien dining area with floating tables and mysterious food replicators along the walls.\nYou can exit to the east.",
        "e": "Room 9",
    },
    # Southern Hallway
    "Room 9": {
        "description": "You look around and see a warm corridor with red-tinted walls. Engine vibrations pulse through the metal floor.\nYou can continue to the north, or enter a door to the west.",
        "n": "Room 7",
        "w": "Room 8",
    },
    # Exit
    "Room 10": {
        "description": "You have reached the airlock chamber with pulsing warning lights and Earth is visible through a viewing screen.",
    }
}

# Set the starting room and initialize variables
current_room = "Room 9"
player_inv = []  # Inventory is an empty list at the start
ship_power = False  # Track whether the ship's power is on

print("Welcome to the UFO Adventure Game!")
print("Type 'quit' to exit the game.")
print("You awaken to find yourself aboard an alien spacecraft! Try to find the exit to escape, before the aliens find you!")

def interact():
    global ship_power  # We'll need to modify the ship_power state
    
    if current_room == "Room 1" and "fuel rod" not in player_inv:  # In Room 1 and don't have the fuel rod yet
        print("You see a fuel rod on the ground. It looks important. Do you want to pick it up? (f)")
        action = input().lower()
        if action == "f":
            player_inv.append("fuel rod")  # Add fuel rod to the inventory
            print("You have picked up a fuel rod and added it to your inventory.")
    
    if current_room == "Room 2" and "fuel rod" in player_inv:  # In Room 2 with the fuel rod
        print("You have a fuel rod. Would you like to power up the engine? (f)")
        action = input().lower()
        if action == "f" and not ship_power:
            ship_power = True  # Turn the ship power on
            rooms["Room 10"]["n"] = "Room 10"  # Unlock access to Room 10 by adding the north exit
            print("You have powered up the engine! The door to Room 10 is now accessible.")
        elif ship_power:
            print("The engine is already powered up.")
    
def update_room_description():
    # Dynamically update the description of Room 1 based on whether the fuel rod is in the player's inventory
    if "fuel rod" in player_inv:
        rooms["Room 1"]["description"] = "You have found the Storage Room. You look around and see nothing of interest. \nThere are doors to the north, south, and east."
    else:
        rooms["Room 1"]["description"] = "You have found the Storage Room. You look around and see a fuel rod on the ground. It looks important. \nThere are doors to the north, south, and east."

while True:
    # Update the description of Room 1 based on whether the fuel rod is in the player's inventory
    update_room_description()
    
    # Print the description of the current room
    print("\n" + rooms[current_room]["description"])
    
    if "item" in rooms[current_room]:  # Check if there's an item in the room to interact with
        interact()
    
    # Update input options based on current room and inventory state
    if "fuel rod" in player_inv and current_room == "Room 2" and not ship_power:
        direction_input = "n, w, s, e, f"  # Allow interaction with f if the fuel rod is in the inventory
    else:
        direction_input = "n, w, s, e"  # Only basic directions if no fuel rod
    
    # Get user input for direction
    direction = input(f"\nWhich direction do you want to go? ({direction_input}): ").lower()

    if direction == "quit":
        print("\nThanks for playing! Goodbye!")
        break
    
    # Check if the direction is valid
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
        
        if current_room == "Room 10" and ship_power:  # Check if the ship's power is on to enter Room 10
            print("\nYou have reached the airlock chamber with pulsing warning lights and Earth is visible through a viewing screen.\nYou escape the UFO and can return home with the escape pod in front of you!")
            break
    else:
        print("\nYou can't go that way! There is no path.")
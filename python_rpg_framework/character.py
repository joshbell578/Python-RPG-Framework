""" character.py
The base class for the player and any NPCs in game. Will have attributes and behavior common to all characters
"""

class Character:
    """Any playing and non-playing characters share these traits
    
    Attributes:
        name: a string
        class_name: string name of character class
        strength: int strength attribute as a number
        dexterity: int agility, balance, coordination
        constitution: int endurance, stamina, health
        intelligence: int reasoning, knowledge, money
        ...and so on (you choose which of these you want)"""
    

    def __init__(self, name: str, class_name="") -> None:
        self.name = name
        self.class_name = class_name

        # initialize all remaining stats to 0 (we'll create a function to set them)
        self.strength = 0
        self.dexteritry = 0
        self.constitution = 0
        self.intelligence = 0

    def get_stats(self) -> str:
        """ return a formatted string of stats """
        stats = f"Name: {self.name}\nClass: {self.class_name}"
        stats += f"Strength: {self.strength}\nDexterity: {self.dexteritry}"
        stats += f"Constitution: {self.constitution}"
        stats += f"Intelligence: {self.intelligence}"
        return stats

# global scope
if __name__ == "__main__":
    player = Character("Chris", "Half-orc")
    print(player.get_stats())
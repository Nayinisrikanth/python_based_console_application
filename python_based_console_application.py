import random
import time
import json
import os

# Optional third-party libraries (install if needed)
try:
    from colorama import Fore, Style
    import emoji
except ImportError:
    Fore = Style = None
    emoji = None

# =========================
# Color Psychology Mappings
# =========================
color_mappings = {
    "red": {"meaning": "Confidence, passion", "outfits": ["red shirt", "red dress", "red jacket"]},
    "blue": {"meaning": "Calmness, trust", "outfits": ["blue jeans", "blue blazer", "blue t-shirt"]},
    "green": {"meaning": "Balance, freshness", "outfits": ["green kurta", "green top", "green hoodie"]},
    "black": {"meaning": "Power, elegance", "outfits": ["black suit", "black jeans", "black t-shirt"]},
    "yellow": {"meaning": "Optimism, energy", "outfits": ["yellow shirt", "yellow dress", "yellow hoodie"]},
    "white": {"meaning": "Purity, simplicity", "outfits": ["white kurta", "white shirt", "white t-shirt"]}
}

# Seasonal suggestions
seasonal_styles = {
    "summer": ["light cotton fabrics", "short sleeves", "sunglasses"],
    "winter": ["wool jackets", "sweaters", "scarves"],
    "rainy": ["raincoat", "umbrella", "waterproof shoes"]
}

# Random style tips
style_tips = [
    "Accessories can change your entire look!",
    "Confidence is the best outfit, rock it and own it!",
    "Pair bold colors with neutrals for balance.",
    "Seasonal fabrics enhance comfort and style."
]

# File for storing user history
HISTORY_FILE = "user_history.json"


# =========================
# Helper Functions
# =========================

def save_history(entry):
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = []

    history.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


def get_user_input():
    print("\n--- Color Psychology Outfit Recommender ---")
    mood = input("Enter your mood (happy, calm, confident, energetic, stressed): ").lower().strip()
    event = input("Enter event type (interview, date, party, casual outing): ").lower().strip()
    season = input("Enter season (summer, winter, rainy): ").lower().strip()
    gender = input("Enter your gender (male, female, neutral): ").lower().strip()
    return mood, event, season, gender


def recommend_color(mood):
    mood_to_color = {
        "happy": "yellow",
        "calm": "blue",
        "confident": "red",
        "energetic": "yellow",
        "stressed": "green"
    }
    return mood_to_color.get(mood, random.choice(list(color_mappings.keys())))


def display_recommendation(color, season, gender):
    outfit_choices = color_mappings[color]["outfits"]
    outfit = random.choice(outfit_choices)
    season_suggestion = random.choice(seasonal_styles.get(season, ["regular wear"]))
    tip = random.choice(style_tips)

    # Format text with colorama (if available)
    if Fore:
        print(Fore.CYAN + f"\nWe recommend: {outfit} ({color.upper()})" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Meaning: {color_mappings[color]['meaning']}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Seasonal Style: {season_suggestion}" + Style.RESET_ALL)
        print(Fore.MAGENTA + f"Tip: {tip}" + Style.RESET_ALL)
    else:
        print(f"\nWe recommend: {outfit} ({color.upper()})")
        print(f"Meaning: {color_mappings[color]['meaning']}")
        print(f"Seasonal Style: {season_suggestion}")
        print(f"Tip: {tip}")

    # Add emoji if available
    if emoji:
        print(emoji.emojize(":sparkles: Dress well, feel good! :sparkles:"))

    # Save to history
    entry = {
        "color": color,
        "outfit": outfit,
        "season": season,
        "gender": gender,
        "tip": tip
    }
    save_history(entry)


# =========================
# Main Program
# =========================
def main():
    while True:
        mood, event, season, gender = get_user_input()
        color = recommend_color(mood)
        time.sleep(1)  # small delay for effect
        display_recommendation(color, season, gender)

        again = input("\nDo you want another recommendation? (yes/no): ").lower()
        if again != "yes":
            print("\nThanks for using the Outfit Recommender. Stay stylish! ✨")
            break


if __name__ == "__main__":
    main()
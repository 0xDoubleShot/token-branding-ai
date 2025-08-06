import json
import random

def generate_branding(data):
    meme = random.choice(data["memes"])
    ai_term = random.choice(data["ai_terms"])
    animal = random.choice(data["animals"])
    emojis = random.sample(data["emojis"], 2)

    name = f"{meme}{animal}"
    symbol = (meme[:2] + animal[:1]).upper()
    slogan = f"{ai_term}-powered token for the {meme.lower()} generation"
    emoji_string = "".join(emojis)

    return {
        "name": name,
        "symbol": symbol,
        "slogan": slogan,
        "emojis": emoji_string
    }

if __name__ == "__main__":
    with open("branding_data.json", "r") as file:
        data = json.load(file)

    branding = generate_branding(data)
    print("💡 Generated Meme Token Branding:")
    for key, value in branding.items():
        print(f"{key.capitalize()}: {value}")
"Add main script"

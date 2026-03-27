import random
import re

CONNECTORS = ["at", "the", "in", "on", "with", "and", "but", "for", "by", "to", "of"]

def get_words():
    while True:
        raw = input("Enter at least 20 words separated by commas: ")
        words = [w.strip() for w in raw.split(",") if w.strip()]

        if len(words) >= 20:
            return words

        print("Please enter at least 20 words.")

def capitalize_word(word):
    if word.lower() == "i":
        return "I"
    return word[:1].upper() + word[1:] if word else word

def make_line(words):
    line_parts = []

    for i, word in enumerate(words):
        word = capitalize_word(word)

        line_parts.append(word)

        if i < len(words) - 1:
            r = random.random()
            if r < 0.20:
                line_parts[-1] += ","
            elif r < 0.28:
                line_parts[-1] += "."
            else:
                line_parts.append(random.choice(CONNECTORS) if random.random() < 0.35 else "")

    line = " ".join(part for part in line_parts if part).strip()
    if line and line[-1] not in ".!?":
        line += random.choice([",", "."])
    return line

def make_poem(words):
    random.shuffle(words)

    selected = words[:20]
    first_half = selected[:10]
    second_half = selected[10:]

    stanza1 = []
    stanza2 = []

    # 1. kıta: 3 satır
    stanza1.append(make_line(first_half[:3]))
    stanza1.append(make_line(first_half[3:7]))
    stanza1.append(make_line(first_half[7:10]))

    # 2. kıta: 3 satır
    stanza2.append(make_line(second_half[:3]))
    stanza2.append(make_line(second_half[3:7]))
    stanza2.append(make_line(second_half[7:10]))

    return "\n".join(stanza1) + "\n\n" + "\n".join(stanza2)

def main():
    words = get_words()
    poem = make_poem(words)

    print("\n" + poem)

    with open("poem.txt", "w", encoding="utf-8") as f:
        f.write(poem)

if __name__ == "__main__":
    main()

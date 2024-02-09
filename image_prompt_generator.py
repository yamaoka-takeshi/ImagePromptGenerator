import random
import json
import sys

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_prompt(data):
    template = data["template"]
    candidates = data["candidates"]

    for placeholder, word_list in candidates.items():
        random_word = random.choice(word_list)
        template = template.replace(placeholder, random_word)

    return template

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <external_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        data = load_data(file_path)
        generated_prompt = generate_prompt(data)
        print(generated_prompt)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{file_path}'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

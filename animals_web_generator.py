import json

def load_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def animal_names_list(raw_animals):
    #it tells you the name of the animal that is shown in the jsonfile.
    names = []

    for animal in raw_animals:
        name = animal.get("name", "Unknown")
        names.append(name)

    return names

def main():
    raw_data = load_data("animals_data.json")
    animal_names = animal_names_list(raw_data)

    for name in animal_names:
        print(name)


if __name__ == "__main__":
    main()
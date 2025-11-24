import json





def load_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def main():
    animal_data = load_data("animals_data.json")
    print (animal_data)


if __name__ == "__main__":
    main()
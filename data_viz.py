from parse_data import parse_data
from paths import PATHS

if __name__ == "__main__":
    path = PATHS["a"]
    contributors, projects = parse_data(path)

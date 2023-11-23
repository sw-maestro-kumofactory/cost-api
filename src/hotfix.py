import json
import sys

def remove_network_interfaces(data):
    if isinstance(data, dict):
        if "NetworkInterfaces" in data:
            del data["NetworkInterfaces"]
        for key, value in data.items():
            remove_network_interfaces(value)
    elif isinstance(data, list):
        for item in data:
            remove_network_interfaces(item)

def func(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        remove_network_interfaces(data)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Updated JSON saved to {file_path}")


    except Exception as e:
        print(f"An error occurred: {e}")

    # print file

    


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)

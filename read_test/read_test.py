import json
import os

def read_config():
    # Save the current working directory
    original_cwd = os.getcwd()
    print(f"Original working directory: {original_cwd}")

    try:
        # Change to the script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"Script directory: {script_dir}")
        os.chdir(script_dir)

        # Construct the path to the config.json file relative to the script directory
        config_path = os.path.join(script_dir, '..', 'ServoConfig', 'backend', 'Config', 'config.json')
        print(f"Config path: {config_path}")

        # Check if the config file exists
        if not os.path.exists(config_path):
            print("The config.json file was not found at the specified path.")
            return

        # Read and print the configuration
        with open(config_path, 'r') as file:
            config = json.load(file)
            for key, value in config.items():
                print(f"{key}: {value}")

    except FileNotFoundError:
        print("The config.json file was not found.")
    except json.JSONDecodeError:
        print("Error decoding the JSON file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Change back to the original working directory
        os.chdir(original_cwd)
        print(f"Returned to original directory: {os.getcwd()}")

# Ensure the script runs only once
if __name__ == "__main__":
    read_config()

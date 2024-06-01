import configparser
import os

# Print the absolute path to ensure the correct path is being used
config_file_path = os.path.join(os.path.dirname(__file__), 'config/config.local')
print(f"Config file path: {os.path.abspath(config_file_path)}")

# Check if the file exists
if not os.path.exists(config_file_path):
    raise FileNotFoundError(f"Config file not found at {config_file_path}")

# Initialize the ConfigParser and read the config file
parser = configparser.ConfigParser()
parser.read(config_file_path)

# Attempt to get the API_KEY from the youtube section
try:
    YOUTUBE_API_KEY = parser.get('youtube', 'API_KEY')
    YOUTUBE_PLAYLIST_ID = parser.get('youtube', 'PLAYLIST_ID')
except configparser.NoSectionError:
    print("Error: No section 'youtube' found in the config file")
except configparser.NoOptionError:
    print("Error: No option 'API_KEY' or 'PLAYLIST_ID' found in the 'youtube' section")
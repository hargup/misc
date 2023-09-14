# Finding `places.sqlite` varies by OS:

# 1. **Windows**
#     - `%APPDATA%\Mozilla\Firefox\Profiles\<profile_folder>`

# 2. **macOS**
#     - `~/Library/Application Support/Firefox/Profiles/<profile_folder>`

# 3. **Linux**
#     - `~/.mozilla/firefox/<profile_folder>`

# Replace `<profile_folder>` with the actual profile folder, which often ends in `.default`.


import os

# Replace this with the base path from above
base_path = 'path/to/profiles/'
for profile_folder in os.listdir(base_path):
    if profile_folder.endswith('.default-release'):
        print(f"Found: {os.path.join(base_path, profile_folder, 'places.sqlite')}")



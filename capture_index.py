import os
import shutil
import json
import argparse

# Parse the command-line arguments
parser = argparse.ArgumentParser(description="Index Autodoc folders.")
parser.add_argument("source_path", help="The directory to search for .autodoc folders.")
args = parser.parse_args()

# Define the destination path where the .autodoc folders will be moved
destination_path = os.path.expanduser("./indexes")

# Create the destination path if it does not exist
if not os.path.exists(destination_path):
    os.makedirs(destination_path)

# Recursively search for .autodoc folders in the source path
for root, dirs, files in os.walk(args.source_path):
    if ".autodoc" in dirs:
        # Get the path of the .autodoc folder and the parent folder
        autodoc_path = os.path.join(root, ".autodoc")
        parent_path = os.path.dirname(autodoc_path)

        # Get the name of the repository from the autodoc.config.json file
        config_path = os.path.join(root, "autodoc.config.json")
        with open(config_path) as f:
            config = json.load(f)
            repo_name = config["repositoryUrl"].split("/")[-1]

        # Create a subfolder in the destination path for the repository
        repo_dest_path = os.path.join(destination_path, repo_name)
        if not os.path.exists(repo_dest_path):
            os.makedirs(repo_dest_path)

        # Move the .autodoc folder and autodoc.config.json to the repository's subfolder
        shutil.move(autodoc_path, repo_dest_path)
        shutil.move(config_path, repo_dest_path)

        # Create a symbolic link from the original location to the new location
        link_path = os.path.join(parent_path, ".autodoc")
        target_path = os.path.join(repo_dest_path, ".autodoc")
        if not os.path.exists(link_path):
            os.symlink(target_path, link_path)

        # Create a symbolic link to autodoc.config.json in the repository's subfolder
        json_link_path = os.path.join(parent_path, "autodoc.config.json")
        json_target_path = os.path.join(repo_dest_path, "autodoc.config.json")
        if not os.path.exists(json_link_path):
            os.symlink(json_target_path, json_link_path)

# Autodoc Indexer
Repo for us to share OSS [Autodoc](https://github.com/context-labs/autodoc) indexes. 

Use the capture script to add additional repos and submit a PR. 

## Requirements

The script requires Python 3.x and the `os`, `shutil`, and `json` modules to be installed.

## Usage

To use the script, simply modify the `source_path` and `destination_path` variables at the beginning of the script to match your desired directory paths, and run the script using Python:

```
python capture-index.py 
```
This is a Python script that searches for `.autodoc` folders in a specified directory and its subdirectories, and moves them to a destination folder named after the corresponding GitHub repository. The script also creates symbolic links to the `.autodoc` folder and `autodoc.config.json` file in their original location, so that they can still be accessed by the Autodoc documentation generation tool.

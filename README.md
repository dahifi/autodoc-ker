# Autodoc Indexer
Repo for us to share OSS [Autodoc](https://github.com/context-labs/autodoc) indexes. 

## Requirements

[Autodoc](https://github.com/context-labs/autodoc)


## Usage

Use the capture_index script to add additional repos and submit a PR. 
`doc q` can be run from any of the indexes subdirectories, no need to move them to the repo. 

```
python capture-index.py /source/to/git_repo
```
This is a Python script that searches for `.autodoc` folders in a specified directory and its subdirectories, and moves them to a destination folder named after the corresponding GitHub repository. The script also creates symbolic links to the `.autodoc` folder and `autodoc.config.json` file in their original location, so that they can still be accessed by the Autodoc documentation generation tool.

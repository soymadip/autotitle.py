# Autotitle

A tool for renaming series episodes with proper titles, mark fillers.

## Features

> [!WARNING]
> This project is in planning stage.  

- Automatically renames episodes to a consistent format
- Marks filler episodes based on a filler list
- Adds episode titles from a database
- Special handling for movies
- Creates backups before renaming

## Installation
<!-- 
```bash
pip install autotitle
```
Or install directly from this repository:
 -->

```bash
pipx install .
```

## Usage

```bash
autotitle /path/to/episodes
```

### Options

- `-dd, --data-directory`: Directory containing files to rename (default: current directory)
- `-f, --filler-file`: Path to file containing filler episode numbers
- `-n, --names-file`: Path to file containing episode and movie names


## Example Output

```
Searching for series files in '/path/to/episodes'...

Renaming:-

=> Detective Conan Remastered 001 - English Subtitle.mkv
   └─> 1 - The Roller Coaster Murder Case - 1080p.mkv

=> Detective Conan Movie 01 - The Time-Bombed Skyscraper.mkv
   └─> Movie 1 - The Time-Bombed Skyscraper (1997) - 1080p.mkv

Summary: 2 files renamed (0 fillers marked, 1 movie)
Backup: 2 files backed up to /path/to/episodes/_backup
Skipped: 0 files
```
<h1 align="center">Welcome to pixel-watcher 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <img alt="Platform" src="https://img.shields.io/badge/platform-linux-red.svg?cacheSeconds=2592000" />
</p>

> `pixel-watcher` will watch as many spots on your screen as you want and notify you by sound if anything (pixel color) changes

## Features
- Multiple spot watching
- Custom alert sound (`.wav`)

## Requirements
- Python 3
- [grabc](https://github.com/muquit/grabc)
- [xdotool](https://github.com/jordansissel/xdotool)

## Usage

1. Create a `.env` file
   ```env
   ALERT="<path to your .wav file>"
   ```

2. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```

3. Run
   ```sh
   python main.py
   ```


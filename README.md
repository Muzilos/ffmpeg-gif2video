# ffmpeg-gif2video
## Usage
### Setting up virtualenv
```bash
virtualenv [-p python37] venv
source venv/bin/activate  # UNIX/MacOS
.\venv\Scripts\activate   # Windows
pip install -r requirements.txt
```
### Converting painting.gif to loop.gif (with 6 hardcoded loops)
[Download the `ffmpeg` executable for your system](https://www.ffmpeg.org/download.html), then run
```bash
./addloops.sh
```

### Processing loop.gif into painting.mp4
```python
python3 main.py
```
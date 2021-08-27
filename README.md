# motion
Watch and delete [motion](https://motion-project.github.io/) videos online.
Tested on `Raspberry Pi zero w` and `Rasperry Pi 4` running `Ubuntu Server 20.04` and `Raspbian OS`.

## Requirements
- Python 3.6 or higher
- Machine running motion

## Installation
``` bash
git clone https://github.com/gifuzzz/motionctl
cd motionctl
pip3 install -r requirements.txt
```

## Configuration
- Feel free to change default configs in `config.py` (particularly if your stream has a static address)

## Start
``` bash
python3 app.py
```

### deleter<area>.py
This file deletes all the motion videos of 4 and more days ago. Put this in crontab to delete old files periodically.

# motion_detector
RPi motion detection with OpenCV
Inspired by https://www.pyimagesearch.com/2015/06/01/home-surveillance-and-motion-detection-with-the-raspberry-pi-python-and-opencv/

# Installation
```bash
sudo apt install libgirepository1.0-dev
pip install PyGObject
pip install boto3
pip install Pillow
install_opencv.sh
```

# Config
```json
{
        "show_video": true,
	"video_resolution": [480, 320],
	"use_s3": true,
	"min_upload_seconds": 3.0,
	"min_motion_frames": 8,
	"camera_warmup_time": 2.5,
	"delta_thresh": 5,
	"resolution": [640, 480],
	"fps": 16,
	"min_area": 5000,
	"region_name": "nyc3",
	"endpoint_url": "https://nyc3.digitaloceanspaces.com",
	"aws_access_key_id": "<YOUR_ID_HERE>",
	"aws_secret_access_key": "<YOUR_KEY_HERE>",
	"bucket": "common-space",
	"s3_path": "sentinels/aragorn/pictures/",
	"backlight_timer": 30000
}
```

# Cron
```bash
crontab -e
* * * * * cd /home/pi/Projects/motion_detector && ./start.sh >> log.txt
```

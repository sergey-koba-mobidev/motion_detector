# motion_detector
RPi motion detection with OpenCV
Inspired by https://www.pyimagesearch.com/2015/06/01/home-surveillance-and-motion-detection-with-the-raspberry-pi-python-and-opencv/

# Installation
```bash
pip install boto3
pip install Pillow
install_opencv.sh
```

# Config
```json
{
        "show_video": true,
	"video_resolution": [360, 240],
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
	"aws_access_key_id": "627U32YYZKZATVC5KD4I",
	"aws_secret_access_key": "/j/MKpkNZctsryFwarqML5ZLwzaqmyYeCNfF+SYdn/s",
	"bucket": "common-space",
	"s3_path": "sentinels/aragorn/pictures/"
}
```

#!/bin/bash

# Update the code
git pull

# Switch python env
source /usr/local/bin/virtualenvwrapper.sh
workon cv

# Run the motion detector
export DISPLAY=:0.0
mkdir -p images
if ! pgrep -f "motion_detector.py" > /dev/null
then
	python motion_detector.py --conf config.json
else
	echo "[INFO] motion_detector is already running"
fi


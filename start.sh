#!/bin/bash

# Update the code
git pull

# Switch python env
source /usr/local/bin/virtualenvwrapper.sh
workon cv

# Run the motion detector
export DISPLAY=:0.0
mkdir -p images
python motion_detector.py --conf config.json

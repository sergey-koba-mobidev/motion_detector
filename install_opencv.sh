#!/bin/sh

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

echo "${green}Install some Developer Tools...${reset}"
sudo apt-get -y install build-essential git cmake unzip pkg-config

echo "${green}Install Image packages...${reset}"
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev

echo "${green}Install Video packages...${reset}"
sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get -y install libxvidcore-dev libx264-dev

echo "${green}Install GTK...${reset}"
sudo apt-get -y install libgtk-3-dev
sudo apt-get -y install libcanberra-gtk*

echo "${green}Install optimization packages...${reset}"
sudo apt-get -y install libatlas-base-dev gfortran

echo "${green}Install python headers...${reset}"
sudo apt-get -y install python2.7-dev python3-dev

echo "${green}Grab OpenCV 4.0.0 code...${reset}"
cd ~
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.0.0.zip
unzip opencv.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.0.0.zip
unzip opencv_contrib.zip

echo "${green}Configure python virtual env...${reset}"
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/get-pip.py ~/.cache/pip
echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.profile
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.profile
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile
source ~/.profile
mkvirtualenv cv -p python3
workon cv
pip install numpy

echo "${green}Compile and install OpenCV 4.0.0...${reset}"
mv opencv-4.0.0 opencv
mv opencv_contrib-4.0.0 opencv_contrib
cd ~/opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D ENABLE_NEON=ON \
    -D ENABLE_VFPV3=ON \
    -D BUILD_TESTS=OFF \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D BUILD_EXAMPLES=OFF ..
echo "${green}Please Increase the SWAP on the Raspberry Pi if next step hangs${reset}"
make -j4
sudo make install
sudo ldconfig

echo "${green}Link opencv packages${reset}"
cd ~/.virtualenvs/cv/lib/python3.5/site-packages/
ln -s /usr/local/python/cv2/python-3.5/cv2.cpython-35m-arm-linux-gnueabihf.so cv2.so

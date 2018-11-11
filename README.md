# RaspberryPi-Face-Recognition
Use Python and Open CV to recognize multi face and show the name

# Some Packages to be installed in Raspberry Pi 3 - Raspbian OS
$ sudo apt-get purge wolfram-engine
$ sudo apt-get purge libreoffice*
$ sudo apt-get clean
$ sudo apt-get autoremove
$ sudo apt-get update && sudo apt-get upgrade
$ sudo apt-get install build-essential cmake pkg-config
$ sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
$ sudo apt-get install libxvidcore-dev libx264-dev
$ sudo apt-get install libgtk2.0-dev libgtk-3-dev
$ sudo apt-get install libatlas-base-dev gfortran
$ sudo apt-get install python2.7-dev python3-dev
$ sudo apt-get install libjpeg-dev
$ sudo apt-get install libtiff5-dev
$ sudo apt-get install libjasper-dev
$ sudo apt-get install libpng12-dev
$ sudo apt-get install libavcodec-dev
$ sudo apt-get install libavformat-dev
$ sudo apt-get install libswscale-dev
$ sudo apt-get install libeigen3-dev
$ sudo apt-get install libxvidcore-dev
$ sudo apt-get install libx264-dev
$ sudo apt-get install libgtk2.0-dev

# Raspberry pi camera installation commands
$ sudo apt-get -y install libv4l-dev v4l-utils
$ sudo modprobe bcm2835-v4l2
$ v4l2-ctl —list-devices

# Install Numpy 
$ sudo apt-get install python2.7-dev python2.7-numpy
$ sudo apt-get install python3-dev python3-numpy 

# Opencv packages
$  mkdir opencv
$  cd opencv 
$  wget https://github.com/opencv/opencv/archive/3.2.0.zip -O opencv_source.zip
$  wget https://github.com/opencv/opencv_contrib/archive/3.2.0.zip -O opencv_contrib.zip

# unzip
$  cd opencv 
$  unzip opencv_source.zip
$  unzip opencv_contrib.zip

#Create folder
$  cd opencv 
$  cd opencv-3.2.0
$  mkdir build 
$  cd build

#Install python package manager
$ cd
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python get-pip.py
$ sudo python3 get-pip.py 

#Run your python Codes in virtuals so we need to workon with virtuals
$  sudo pip install virtualenv virtualenvwrapper
$  sudo rm -rf ~/.cache/pip

export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

$ echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.profile
$ echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.profile
$ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile
$ source ~/.profile
$ mkvirtualenv cv -p python2

$ mkvirtualenv cv -p python3
$ source ~/.profile
$ workon cv
$ pip install numpy

#Cmake files
#inside build folder you should make this cmake
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D BUILD_WITH_DEBUG_INFO=OFF \
-D BUILD_DOCS=OFF \
-D BUILD_EXAMPLES=OFF \
-D BUILD_TESTS=OFF \
-D BUILD_opencv_ts=OFF \
-D BUILD_PREF_TESTS=OFF \
-D INSTALL_C_EXAMPLES=ON \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.2.0/modules \
-D ENABLE_NEON=ON \
-D WITH_LIBV4L=ON \
../

cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_WITH_DEBUG_INFO=OFF -D BUILD_DOCS=OFF -D BUILD_EXAMPLES=OFF -D BUILD_TESTS=OFF -D BUILD_opencv_ts=OFF -D BUILD_PREF_TESTS=OFF -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.2.0/modules -D ENABLE_NEON=ON -D WITH_LIBV4L=ON ../

CONF_SWAPSIZE=1024

$ sudo /etc/init.d/dphys-swapfile stop
$ sudo /etc/init.d/dphys-swapfile start

#Opencv installation
$ make -j4
$ sudo make install 
$ sudo ldconfig
$ ls -l /usr/local/lib/python2.7/site-packages/
total 1852
-rw-r--r-- 1 root staff 1895772 Mar 20 20:00 cv2.so


$ cd ~/.virtualenvs/cv/lib/python2.7/site-packages/
$ ln -s /usr/local/lib/python2.7/site-packages/cv2.so cv2.so

$ ls -l /usr/local/lib/python3.5/site-packages/
total 1852
-rw-r--r-- 1 root staff 1895932 Mar 20 21:51 cv2.cpython-34m.so

$ cd /usr/local/lib/python3.5/site-packages/
$ sudo mv cv2.cpython-35m-arm-linux-gnueabihf.so cv2.so

$ cd ~/.virtualenvs/cv/lib/python3.5/site-packages/
$ ln -s /usr/local/lib/python3.5/site-packages/cv2.so cv2.so

#Finally swap the conf size

CONF_SWAPSIZE=100
$ sudo /etc/init.d/dphys-swapfile stop
$ sudo /etc/init.d/dphys-swapfile start

$ sudo apt-get install build-essential
$ sudo apt-get install python-dev 
$ sudo apt-get install gfortran 
$ sudo apt-get install python-opencv
$ sudo apt-get install python-matplotlib
$ sudo apt-get install python-numpy 

#RPI-DOCKER-TENSORFLOW
#If you want to work on rpi docker with tensorflow follow this link 

https://github.com/romilly/rpi-docker-tensorflow 

##THANKS
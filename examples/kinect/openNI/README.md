# Kinect + OpenCV + OpenNNI
useful: https://gist.github.com/joinAero/1f76844278f141cea8338d1118423648

and

https://gist.github.com/chatchavan/990d3c0a5b085dc7bae1

cmake -D CMAKE_BUILD_TYPE=RELEASE     -D CMAKE_INSTALL_PREFIX=/usr/local     -D INSTALL_PYTHON_EXAMPLES=ON     -D OPENCV_EXTRA_MODULES_PATH=/usr/local/src/opencv_contrib-3.1.0/modules     -D BUILD_EXAMPLES=ON cmake -DENABLE_PRECOMPILED_HEADERS=OFF -DCMAKE_BUILD_PYTHON=ON -DBUILD_EXAMPLES=OFF -DBUILD_C_SYNC=OFF -D CMAKE_BUILD_TYPE=RELEASE -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_OPENNI=ON -D ENABLE_NEON=ON -D ENABLE_VFPV3=ON ..

https://github.com/xxorde/librekinect

sudo rmmod gspca_kinect
modprobe gspca_kinect depth_mode=1

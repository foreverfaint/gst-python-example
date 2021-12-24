# gst-rtsp-server

An example for hosting a rtsp streaming by gstreamer. This code is inspired by [prabhakar-sivanesan/OpenCV-rtsp-server](https://github.com/prabhakar-sivanesan/OpenCV-rtsp-server). The major difference with [prabhakar-sivanesan/OpenCV-rtsp-server](https://github.com/prabhakar-sivanesan/OpenCV-rtsp-server) is supporting:

- Playbacks a media file in cycle way for streaming.
- Launch multiple rtsp streams.

## Installation

The installation steps are learned from [How to install Gstreamer Python Bindings](http://lifestyletransfer.com/how-to-install-gstreamer-python-bindings/). The process is tested at Windows 11 + WSL2 + Ubuntu 20.04. Some tiny changes are adapted for Ubuntu 20.04.

```bash
# Install gstreamer basis
sudo apt install libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio

# Install rtsp server related
sudo apt-get install libglib2.0-dev libgstrtspserver-1.0-dev gstreamer1.0-rtsp

# Install Python basis. You can replace 3.6 with any other version.
sudo apt install python3.6 python3.6-dev python-dev python3-dev python3-pip python-dev python3.6-venv

# Install gstreamer Python binding
sudo apt install autoconf automake libtool python3-gi python3-gst-1.0 libgirepository1.0-dev libcairo2-dev gir1.2-gstreamer-1.0 gir1.2-gst-rtsp-server-1.0

# Setup a virtual environment for development and testing
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install python packages for gstreamer Python binding.
pip install --upgrade wheel pip setuptools
pip install pycairo PyGObject

# Verify packages installed successfully
python -c "import gi; gi.require_version('Gst', '1.0'); \
gi.require_version('GstApp', '1.0'); \
gi.require_version('GstVideo', '1.0'); \
gi.require_version('GstBase', '1.0'); \
gi.require_version('GstRtspServer', '1.0')"
```

## Usage

### `example_filesrc_to_rtsp.py`

```bash
$ python example_filesrc_to_rtsp.py
stream ready at rtsp://127.0.0.1:8554/0

# launch a new shell for testing
$ gst-launch-1.0 rtspsrc location=rtsp://localhost:8554/0 latency=0 ! decodebin ! autovideosink

# you can launch more clients
$ gst-launch-1.0 rtspsrc location=rtsp://localhost:8554/0 latency=0 ! decodebin ! autovideosink

# even switch to multiple paths, e.g, /0 and /1
$ gst-launch-1.0 rtspsrc location=rtsp://localhost:8554/1 latency=0 ! decodebin ! autovideosink
```

> The testing video *sample-mp4-file-small.mp4* is downloaded from [11 Sample video files | MP4 sample download](https://www.learningcontainer.com/mp4-sample-video-files-download/). Please do *NOT* use or distribute it for other purposes.


## Tip

If your program doesn't work well, please set GST_DEBUG environment variable for logging some levels of information to stdout.

```bash
# basic
$ GST_DEBUG=1 python gst_rtsp_server_2.py

# verbose
$ GST_DEBUG=6 python gst_rtsp_server_2.py

# verbose and python logging only
$ GST_DEBUG=python:6 python gst_rtsp_server_2.py
```

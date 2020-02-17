#!/bin/bash
ffmpeg -stream_loop 6 -i ./tmp/painting.gif ./tmp/loop.gif -y
# ffmpeg -i ./tmp/loop.gif -pix_fmt yuv720p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ./tmp/loop.mp4 -y
Title: HTPC Stutter Over HDMI on Samsung HDTV
Date: 2011-02-18 23:25
Author: Admin
Category: Technology
Tags: hdmi, samsung, tv, xbmc

This will be a quick one. I recently built an HTPC to run XBMC and play
videos off my file share. I noticed that almost all videos had
an occasional stutter that would occur every few seconds and produce a
very slight stutter in the image. This happened for all file types and
resolutions. I'm running with an integrated ATI HD 4250.

I eventually figured out that it was my TV settings. I was connecting
over HDMI and Samsung must do some extra processing or handshaking over
the HDMI to HTPC. I realized this since I connected my HTPC to my
monitor at the same resolution (1080p 60hz) and I experienced perfect
video playback. I eventually was able to solve the problem by setting
the HDMI input source name to PC and disabling Auto Motion Plus
features. It seems like this tells the Samsung set to stop any extra
processing that causes and occasional stutter.

Hope this helps someone out there!

UPDATE: I found that turning off "de-interlacing" in the ATI catalyst
settings eliminated this effect. Try that in addition to the above steps

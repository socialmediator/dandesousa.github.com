Title: How To: Dual Monitors in Ubuntu with Nvidia
Date: 2010-01-24 15:13
Author: Admin
Category: Technology
Tags: linux

I noticed that a lot of people are getting "cannot parse xorg.conf"
message when they try to set up dual monitors with Nvidia settings
manager in ubuntu. Here is the solution.

On the command line:

<p>
    sudo nvidia-xconfig

</p>

You should see it tell you that it overrode your xorg.conf. If you get
warnings don't worry, it's likely just indicating that there was a
previous problem. Then on the command line again, type this:

<p>
    sudo nvidia-settings

</p>

Now setup your dual monitor or triple monitor configuration as you want
(with Twin View and the correct orientation). Then hit save
configuration at the bottom and you should see that you get no error.

Reboot and enjoy.

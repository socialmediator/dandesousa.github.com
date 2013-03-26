Title: Getting Highpoint RocketRaid 2640x4 Controller To Work In Linux
Date: 2011-06-03 17:29
Author: Admin
Category: Technology

So, I finally got around to re-organizing my home server situation, and
was given a RocketRaid 2640x4 SAS Raid Controller from a friend. My
intention was to simply use it for the extra SATA slots and not bother
with its own on-board RAID. However, when I tried to get it to work, I
noticed that the drives weren't being detected under Ubuntu. I scored
the internet until I finally found a post from a newegg buyer that
resolved my issue and I feel its important enough to post.

Here are the steps you need to follow to get this controller to work
under Linux. They may work for all versions of Linux but I have not
tried them.

1.) Flash the BIOS to legacy

If you don't need the RAID features, you can flash the BIOS on the card
to replace the current BIOS with a legacy BIOS *sans* RAID. To do this,
simply download the legacy BIOS from the Highpoint website. You can then
either run the highpoint flash utility under windows or you'll need to
create a DOS boot disk. If you have access to a Windows box, using the
utility is the easier course of action. When you extract the BIOS zip it
should be listed as hptflash.exe and look like this:

![][]

2.) Configure the drive to be under legacy mode

Now plug you card back into the linux box and make sure that all the
drives connected to the card are listed as "legacy" in the RocketRaid
RAID utility that appears when you boot your machine (You may need to
press CTRL+H when the appropriate screen appears).

3.) Download and Compile the Driver Source

Now you need to make sure the drivers are properly installed. I got
issues when I tried to install the pre-built binaries. Luckily its
pretty easy to compile the drivers yourself. Simply download the
*legacy* drives from the RocketRaid site on the same page as the BIOS.
Now just cd in the lowest level of the source directory and type "sudo
make install". You'll see it build and then you are done!

The drivers will then be installed. If you reboot and check ls /dev you
should see a drive labeled sd\<\*\> for every drive connect to the card
or your motherboard. Enjoy!

  []: ./static/wp-content/uploads/2011/06/Capture-300x178.png "Capture"

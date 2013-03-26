Title: HowTo Fix: Slow SSD Boot Times in Mac OS X
Date: 2012-03-07 21:31
Author: Admin
Category: Technology
Tags: ssd, apple, macbook, boot

I recently bought a ssd for my macbook pro and noticed after installing
and reformatting, the boot times were slow ... about as slow as my hdd
or even slower. If you have an SSD, you can except boot times around 15
seconds or so. If you are encountering boot times of 35+ seconds, you
may have the same problem I had. I was able to solve the problem by
following these steps:

1.  System Preferences -\> Startup Disk. Make sure that your SSD drive
    is selected.
2.  Open Disk Utility and select your drive, and click "Repair Disk
    Permissions"
3.  [Reset your PRAM][]
4.  [Reset your SMC][]

</p>
The final step of reseting the SMC finally fixed this for me, but I had
tried all the steps before hand, so I cannot be sure which will work for
you. If you have any comments, please post for the benefit of all
readers.

  [Reset your PRAM]: http://support.apple.com/kb/ht1379
  [Reset your SMC]: http://support.apple.com/kb/HT3964

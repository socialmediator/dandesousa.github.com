Title: Changing PlexSync Temporary Directory
Date: 2012-11-20 20:10
Author: Admin
Category: Technology
Tags: plex

Plex just announced a great new syncing feature for iOS devices, but I
noticed that when I started syncing, my SSD would quickly fill up. It
turns out that as of the current release of plex server v0.9.7.3, you
cannot directly change the directory. However, you can change the entire
local application path for plex. There are instructions on the Plex wiki
detailing how this is done:

[Plex Wiki][1]

In my case I set LocalAppDataPath in the registry to my RAID disc which
has plenty of storage. You'll have to follow the instructions for your
particular platform.

**IMPORTANT: **Make sure that when you change the path you copy your old
plex app data directory to preserve all your metadata, thumbnails, and
database. On Windows, its in "C:/Users/\<USERNAME\>/AppData/Local/Plex
Media Server". Also important, remember that the directory
Cache/Transcode/Sync **MUST** exist. I tried to delete the cache to save
myself some transfer time and when I was missing that
Cache/Transcode/Sync directory, PlexSync would not work at all. Once I
restored the directory, all was well.

  [1]: http://wiki.plexapp.com/index.php/Plex_Media_Server_Preferences#Advanced_Preferences%20%20

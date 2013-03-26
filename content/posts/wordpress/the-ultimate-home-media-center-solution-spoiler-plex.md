Title: The Ultimate Home Media Center Solution [Spoiler: Plex!]
Date: 2011-11-05 23:08
Author: Admin
Category: Technology
Tags: plex, home media center

In this article, I cover my opinion on currently the best media center
option for managing local content libraries, and my thoughts on the
state of digital video distribution.

I do not condone any mention of piracy in the article and any references
are merely for illustrative purposes regarding this rather opinionated
article :-).

Feel free to jump ahead to the guide, but first some background:

**How I Discovered Plex**
=========================

</p>
I can say that I have been searching for the "perfect" home media center
for a long time. I have a rather large collection of TV Shows and DVDs
that have been ripped. For years I struggled with getting that media on
devices I wanted. At first I converted them to PS3 compatible formats
and streamed them over DLNA using TwonkeyMedia. That was great except
that conversions took a long time. Then if I wanted them on my iPhone or
iPod I need to convert them yet again, to a different format. Then I
needed space for all those duplicate files (and managing them was a
nightmare). There seemed to be a lot of disjoint solutions which
required manual management. A friend of mine suggested XBMC, which is a
great home media center front end with tons of plug-in support. It
actually eventually led to my discovery of what I believe to be clearly
the best product out there for managing a local collection of content
and getting it on your devices, and it is called [Plex][].

**What Is Plex?**
=================

</p>
First, let me explain what Plex does. Plex is a media center front end
for Plex Media Server. Basically, Plex Media Server manages a library of
media on a computer for you, and serves it up to multiple devices. So
you can have a drive with all your TV Shows, Movies, Music, Photos, etc
and Plex Media Server (PMS -- an unfortunate abbreviation) will deliver
it over your home network or the internet. Plex is a UI which runs on a
computer, mobile phone or TV and gives you access to that content. It
looks something like this:

![][]

<a href="./static/wp-content/uploads/2011/11/episode_overview.png">

</a>Basically gives you all your episodes (with metadata) automatically.
Lets you browse by tons of different categories, like unwatched or
recently aired/added. Did I mention it automatically organize your media
assuming you have everything reasonable named? Basically it is pretty
close to media center nirvana, and the basic application and server are
free to use.

</p>

So what makes this better than any other solution out there, especially
XBMC (from which Plex was originally development from)?

</p>

Well it's all about Plex Media Server. Basically you can setup one
machine in your network with media center, and serve up content to every
client device running plex. The Plex client is available for Mac, Roku,
Samsung and LG TVs, and jailbroken Apple TVs and more -- so theres
plenty of choice on the set top box front. Additionally there are native
iPhone, iPad, and Android apps. Also, Plex Media Server automatically
live transcodes videos which are unsupported on client devices, and
almost all video formats are supported. This solves the problem I had
originally in storing many copies of files. Also, since everything is on
a common server, you can stop a show or movie on your TV, then watch it
on your iPad in bed. The server keeps track of partially watch shows on
all devices. Also, you may want to search for an application called
sickbeard, as it can integrate with plex to enhance your experience
(that is all I can say :-) ).

</p>

If you like what you hear, I suggest trying it out. I can also recommend
a setup which I've found useful, not everyone needs what I have, you can
make due with less, but my setup fits with my other server needs.

</p>

**Setting Up Plex Media Center**
================================

</p>
EDIT: I just noticed that as of the latest update, Plex is also
available for Windows. So you can use any machine you want.

You Will Need:

-   Mac Mini (Alternative: Samsung or LG TV with Apps, Roku, Google TV,
    Apple TV)
-   Dedicated Server of any OS (Mac Mini will do, or any other machine
    so long as it is on while you watch videos)
-   Plex for iOS / Android (Last I checked it was about \$3-5 in the app
    store but definitely the best purchase I've made)
-   Plex for Mac
-   Plex Media Server

</p>

<div>
Rough Setup and Reasoning:

</div>
</p>

<div>
</p>

1.  First, you want to setup your Mac Mini or other plex box. I
    recommend a mac mini because it is small and provides the best
    looking, fastest Plex experience. You also get a complete client
    implementation. It is also the most expensive option. There are Plex
    clients for TVs, Roku, Google TV or Apple TV (jailbroken), so you
    can also try one of those if you already have a different box.
2.  You should install and run Plex Media Server on a dedicated box you
    can always count on being on when you want to watch videos. This
    should also be the server all the media is stored on. Advantage of
    an always on server is that you can access your content from any
    time on the network (or on the internet if you setup myPlex which is
    available as of Plex 0.9.5).
3.  Plex for iOS is only necessary if you want to watch you media on
    mobile devices. The apps cost a few bucks but they are totally worth
    it and highly polished.
4.  Once you setup PMS you just need to run plex and it should
    auto-detect your local server, exposing all your media. If you run
    an alternative plex client you may need to point it to the address
    of your server.

</p>
<p>
</div>
</p>

**Why People Want Plex** {style="text-align: left;"}
========================

</p>

I asked myself why people want home media centers. I don't think it is
necessarily due to wanting to own copies of movies, tv shows and music.
I think that Plex and XBMC have succeeded because simply put, the
providers and TV device manufacturers have failed consumers. There is no
single product out there that can give you everything you want, despite
having tons of companies dedicated to this purpose.

</p>

*Netflix* {style="text-align: left;"}
---------

</p>

Netflix is cheap and great, but it has a terrible selection. I mean 8\$
a month isn't much but it seems like half the content on there are
national geographic documentaries. They have great coverage for client
devices (all mobile phone platforms, tablets, set tops, tvs) but their
coverage is just so spotty. It seems like they are always losing
providers or having content negotiation problems. Even so, most shows
only come out on Netflix the same time they come out on DVD. Maybe I
don't want to wait 8 months to watch a TV show.

</p>

*Amazon Instant Video* {style="text-align: left;"}
----------------------

</p>

The next best service is probably Amazon Instant Video. It has a decent
selection of TV shows and if you are an Amazon Prime member, the deal is
great (I recently get addicted to Doctor Who thanks to Amazon Instant
Video and am now I lover of the series). The problem with Amazon is that
the client support is simply abysmal. I don't understand what they are
doing. Amazon is perhaps my favorite internet company but I think
whoever is running their video distribution strategy is a buffoon.
Amazon Instant Video has clients for Roku and some TVs. However, theres
no iOS support (no iPad -- come on!), no Android support, no apple tv
support. If you sell a streaming service you need to make it accessible.
Also, same criticism applies to the waiting period as netflix.

</p>

*iTunes and Apple TV* {style="text-align: left;"}
---------------------

</p>

Apple TV provides a wide selection of TV Shows and Movies. They have
their own dedicated box which is simple and cheap. Unfortunately, Apple
TV has serious, serious flaws. The deal breaker being that its 720p, as
is most of the content on the iTunes store. Also, theres no subscription
option, you have to actually buy all the episodes of every show. Its
almost a good alternative if you don't want cable.

</p>

I think what the world really needs is a digital form of on demand
cable. Where you choose your box or client, and subscribe through a
cable provider to certain shows or subsets of channels and have
optionally commercial free streaming of content. Then you have access to
all their networks contents from all time. The issue is that content
providers and cable companies don't want to stray from a profitable
traditional business model. They like charging you 100\$ a month for
digital cable, when you watch about 25% of the shows and channels. Then
they want to sell people box set DVDs they will watch once if ever after
the original airing date. They think this is the best way to make money.
What they don't realize is that if they provide customers with choice,
such as choosing which channels they watch, choosing whether or not to
watch with commercials, they will make more money. You can lend a box
set of DVDs to your friend. You can't share DRM digital rental,
subscription or purchase, and you can't resell it when you are finish
(this is why the video game industry loves digital downloads -- they
lose millions to the resale game market). This is not even to mention
the possibility for targeted advertisements or exposing people to shows
directly.

</p>

So how does Plex solve this? Well let's be honest, a large number of
people who want XBMC or Plex are downloading TV Shows or ripping their
own bought discs. They are making this complete service for themselves,
for the subset of shows they want to watch. The sad thing is that the
piracy is actually a better solution then what is legally available.
Using the right tools, it can become completely automated, commercial
free, and instant available after airing -- you could get full quality
720 TV shows and 1080p Movies as soon as they air or become commercially
available without lifting a finger. Get with the program providers, if
people are willing to spend thousands on custom servers, software and
services, they will pay a little extra for complete, high quality
streaming access that is guaranteed and legal.

</p>

Hopefully Google, Microsoft or Apple will get their act together and
release a good solution. Apple has a good track record with provider
industries in getting content on digital devices. Maybe we will see an
Apple TV running iOS with native third party app support soon. That
could mean an app store that supports channels from providers, or a
common subscription model. There is a lot of money to be made here.

</p>

I'd like to hear what anyone else thinks. What sort of setup do you guys
have, what do you want to see in a streaming service that doesn't exist?

</p>

  [Plex]: http://www.plexapp.com/
  []: ./static/wp-content/uploads/2011/11/episode_overview.png "episode_overview"

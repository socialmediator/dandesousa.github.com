Title: HowTo: Setup a network with two internet connections
Date: 2012-05-26 08:41
Author: Admin
Category: Technology
Tags: networking

If you are living in an area where internet connection options are
limited, you may find yourself in a connundrum. Perhaps you want to be
able to use high bandwidth services (netflix, itunes, bittorrent,
gaming) but a single connection pipe is not large enough to accomodate
all the traffic. Or perhaps, your internet is capped or throttled after
a certain amount of time.

**My Situation**
----------------

</p>
I currently live in such an area, where my faster internet provider will
quickly throttle for high usage. I needed to be able to download (iTunes
videos, Steam games, etc), but my primary provider throttles if we
download too much. To make matters worse, my girlfriend works from home,
so she needs a fast constant connection.

So what I wanted was to be able to use Clear (which has great speed and
reception in our area) for normal internet and DSL for all the high
bandwidth content. We needed to have one or two computers in our network
use the DSL, and the others use Clear. However, we still needed everyone
on the same network because we needed to access file shares and other
applications running on the network.

After much searching I found a solution that fits my needs and that I
hope will help some other people as well.

**The Solution**
----------------

</p>
The solution to my problem is to create a ***Multiple Gateway*** setup.
The idea is you have a standard network with one internet connection
that acts as the primary gateway. By default all connecting devices use
this connection. You then add one or more routers with separate incoming
connections as other gateways. You assign them IPs and you tell the
devices you want to use that gateway and it will use it for those
connections.

*So in summary, this setup will allow you to keep all devices on one
network and manually assign which connection each device uses (using one
connection as the default).*

You just need to follow these steps:

### **Setup your default gateway**

</p>
For the purpose of this article, gateway is just another term for a
router with an incoming WAN or internet connection. Chances are your
default gateway is already setup -- its just your current single
connection network setup. If you want to continue to use this connection
as the default for all devices on the network, leave as is and continue
to the next step. Otherwise swap the internet connections.

*The internet connection on this gateway will be used for all devices by
default.*

***Make a note of your router's IP address; in most cases it is
'192.168.1.1'.***

Also note the DHCP range of your router, this varies by model but on the
common dd-wrt setup can be found here:

![][]

</p>
For this scenario our DHCP range starts at 192.168.1.100. So anything
from 192.168.1.0 - 192.168.1.99 is out of range and won't be used by the
router when assigning the addresses to devices. This is important to
know for the next step.

### **Setup your second gateway**

</p>
You want to setup a completely separate network with the second router
and connection. Don't connect the second gateway to the main network
yet. Verify that on your second connection you have an internet
connection and everything is working.

**Assign the second gateway an IP address**

Once that works, you want to give the second gateway a different IP
address to distinguish it from the primary gateway. Since the primary
gateway is IP address 192.168.1.1, we'll use 192.168.1.2. Note that the
address must be outside the range of DHCP for the primary gateway.

**Disable DHCP on the second gateway**

Now, you want to disable DHCP server on the second gateway. If you are
using DD-WRT, the highlighted radio box in the box image should be
'Disable'. This is important, DHCP MUST BE DISABLED. Not set to a new
gateway, not turned onto DHCP forwarding -- DISABLED. Make sure you hit
apply and save any settings before moving onto the next step.

### **Connect your second gateway to your network through the LAN port**

</p>
Now connect your second gateway to your network through the LAN part as
you would connect a switch to your network to allow for additional
connections. Once you do so, you should be able to connect to your
primary network and access both the primary gateway and the secondary
gateway by their addresses. Confirm this by ensuring you can access
192.168.1.1 and 192.168.1.2.

### **Configure your machines to use the alternative gateway**

</p>
Good news is you are pretty much done now. You can confirm your setup is
working by assigning a machine to either network. You want to open up
your network menu and find your network interface (representing the one
connected to your network  -- be it wired or wireless).

![][1]

now right click and select properties. Then select the IPv4 settings and
hit properties again:

![][2]

Now you want to manually configure your connection.

![][3]

For your IP address, assign anything that is outside the DHCP range of
your router (anything below 192.168.1.100 works in this example). Leave
subnet mask matching your primary gateway and assign default gateway to
the second connection. You'll also want to add that as the DNS server.
This tells this network interface to use that gateway for your internet
connection.

If all works successfully you should now have access, and all traffic on
that box will flow to your second gateway, leaving your other
connections unaffected.

Most devices give you the ability to customize the your IP configuration
this way, so you should be able to configure your devices in any manner
you choose.

### **Repeat for any additional connections **

</p>
The multiple gateway setup works for as many connections as you want.
Just continue adding addresses outside your DHCP range for your gateways
and you should be fine.

Hopefully this will be useful to people out there trying to work out how
to use multiple connections in their home network. I know it was for me.

  []: ./static/wp-content/uploads/2012/05/default-gateway-192.168.1.1-dhcp-address-781x1024.png
    "default-gateway-192.168.1.1-dhcp-address"
  [1]: ./static/wp-content/uploads/2012/05/network-1.png
    "network-1"
  [2]: ./static/wp-content/uploads/2012/05/network-2.png
    "network-2"
  [3]: ./static/wp-content/uploads/2012/05/network-3.png
    "network-3"

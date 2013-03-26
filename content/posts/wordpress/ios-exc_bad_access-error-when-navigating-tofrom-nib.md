Title: iOS EXC_BAD_ACCESS error when navigating to/from nib
Date: 2010-11-27 13:01
Author: Admin
Category: Programming
Tags: iphone, memory management, objective-c, UITableView

As I have begun the trek towards mastering objective-c, I've come to
appreciate the memory management nuances. I came across a problem where
when navigating backwards in a table view, the application would just
crash with an EXC\_BAD\_ACCESS error. If you see this it is most likely
due to accidently mis-managing memory. I fixed my particular error by
referring to the memory management rules with NIBs. Because of the way
nibs are access you need to unload IBOutlet properties in the
viewDidUnload method. Here are examples from apple's documentation:

    :::objective-c
    - (void)viewDidUnload {
        self.anOutlet = nil;
        [super viewDidUnload];
    }

Also, for some reason you also have to release them in the dealloc for
the controller you are in:

    :::objective-c
    - (void)dealloc {
        // Release outlets and set outlet variables to nil.
        [anOutlet release], anOutlet = nil;
        [super dealloc];
    }

Hope this helps someone out there. [Here are the details of how to
manage memory in NIBS for Mac OS or iOS.][]

  [Here are the details of how to manage memory in NIBS for Mac OS or iOS.]: http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmNibObjects.html

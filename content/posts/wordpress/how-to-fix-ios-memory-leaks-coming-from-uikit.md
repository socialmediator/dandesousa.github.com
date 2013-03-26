Title: How To Fix iOS Memory Leaks Coming From UIKit 
Date: 2011-02-11 21:10
Author: Admin
Category: Programming

It looks as though I'm going to be posting a number of troubleshooting
iOS SDK and objective-c guides in the coming weeks. The first deals with
memory leaks coming from UIKit and QuartzCore.

If you are using the leaks tool included with Instruments and XCode, you
might notice leaks. This is a pretty amazing tool that will tell you
when you leak, how much and where the allocations occurred.

In instruments, you can select View -\> Extended Detail. This will
provide you with the stack trace. You can then see where the leak
originated. If you see errors coming straight from main, or from a call
to pushViewController, you likely had the same problem I had -- you are
not cleaning up your View or ViewController.

To be safe in memory management, be careful to do the following:

1.  In viewDidUnload:, you should set all your retain and IBOutlet
    properties to nil like so:
2.  Secondly, and very important, you should release and set all the
    IBOutlet backing properties to nil, like so:
3.  Make sure you have no references to parent views or controllers in
    the leaking view controller.

</p>
This may seem totally counterintuitive since retain properties should
properly free all held memory when nil is set, but actually the second
step is required when dealing with UI components, otherwise it will
result it leaks that appear to originate from UIKit or other Apple
libraries. Be very careful that all IBOutlets are set to nil.

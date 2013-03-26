Title: Windows Phone 7: Making an HTTP Request
Date: 2010-08-30 22:20
Author: Admin
Category: Programming
Tags: .net, C#, Windows Phone 7, WP7

Silverlight and the Windows Phone 7 SDK include the standard System.Net
packages for making various requests over ftp and http. Making a
standard http request in C\# involves setting up a number of delegates
and asynchronous callbacks for getting http responses and can be a tad
complicated. If you simply want to get some xml or html back as a string
over http, it’s much easier to use the simpler, more abstract WebClient
class. Here’s an example of using the WebClient class to make a request.

    :::c#
    public void getResults(string websiteURL)
    {
        WebClient c = new WebClient();
        c.DownloadStringAsync(new Uri(websiteURL));
        c.DownloadStringCompleted += new
            DownloadStringCompletedEventHandler(c_DownloadStringCompleted);
    }
    void c_DownloadStringCompleted(object sender,
            DownloadStringCompletedEventArgs e)
    {
        lock (this)
        {
            string s = e.Result;
            XmlReader r = XmlReader.Create(new
                    MemoryStream(System.Text.UnicodeEncoding.Unicode.GetBytes(s)));
            // So something with the XML we get back
        }
    }

So basically all we do is say download the string and make the action to
take when it is completed as c\_DownloadStringCompleted event handler.
You may want to do something different than place it in an xml reader
(in this case the string we are getting back corresponds to a non-xhtml
 xml file. Enjoy.

 </p>


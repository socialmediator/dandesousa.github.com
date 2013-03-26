Title: HowTo Fix: C# .NET BackgroundWorker.IsBusy Always True
Date: 2010-08-20 23:52
Author: Admin
Category: Technology
Tags: .net, C#, Threading

BackgroundWorker provides a great simplified mechanism for seperating
CPU intensive work from the UI thread in C\# .NET. Indeed[the MSDN
documentation does an excellent job detailing its usage][]. However, you
may come across a bug wherein you need to run the backgroundworker while
it is still running. You have code like this:

    :::csharp
    System.ComponentModel.BackgroundWorker backgroundWorker;
    public void someEvent()
    {
        while (backgroundWorker.IsBusy)
        {
            Thread.Yield();
        }
        backgroundWorker.RunWorkerAsync();
    }


But you may find that backgroundWorker.IsBusy is always true so the loop
never executes. It seems that simply yielding the thread will not force
the backgroundWorker to mark itself as done even though that worker
thread has successfully completed. In some situations you are blocking
the UI so it cannot mark itself complete. To resolve the problem, simply
include a call to System.Windows.Forms.Application.DoEvents(). You can
do this even if you are running an application under WPF. It should
force the UI to load a frame.

    :::c#
    using System.Windows.Forms;
    System.ComponentModel.BackgroundWorker backgroundWorker;
    public void someEvent()
    {
        while (backgroundWorker.IsBusy)
        {
            Thread.Yield();
            Application.DoEvents();
        }
        backgroundWorker.RunWorkerAsync();
    }


For more information on this method check out [the MSDN documentation on
Application.DoEvents()][].

[the MSDN documentation does an excellent job detailing its usage]: http://msdn.microsoft.com/en-us/library/system.componentmodel.backgroundworker.aspx
[the MSDN documentation on Application.DoEvents()]: http://msdn.microsoft.com/en-us/library/system.windows.forms.application.doevents.aspx

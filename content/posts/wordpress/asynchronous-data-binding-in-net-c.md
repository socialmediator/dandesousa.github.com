Title: Asynchronous Data Binding in .NET (C#)
Date: 2010-08-07 16:31
Author: Admin
Category: Programming
Tags: .net, C#, Programming

Asynchronous operations are prevalent in all manner of modern systems,
desktop and web applications. Doing this in .NET is relatively easy as
Microsoft has provided us with a built in mechanism for binding data.

Specifically in WPF, we can perform databinding simply by providing a
binding target and a binding source. The binding target is the object in
which the data belongs and the source is the property which it will be
placed (sort of backwards, but basically they refer to the two
endpoints). I won't write an entire article on Databinding but instead
point you to[MSDN's official documentation on the subject][].

Needless to say Databinding is immensely powerful and greatly simplifies
how we as developers deal with code in UI space. Now from the Microsoft
example, assume we have a databinding code snippet that looks like this:

    :::csharp
    MyData myDataObject = new MyData(DateTime.Now);
    Binding myBinding = new Binding("MyDataProperty");
    myBinding.Source = myDataObject;
    myText.SetBinding(TextBlock.TextProperty, myBinding);


Then if we want to load the data asynchronously we would simply add:

    :::csharp
    MyData myDataObject = new MyData(DateTime.Now);
    Binding myBinding = new Binding("MyDataProperty");
    myBinding.Source = myDataObject;
    myText.SetBinding(TextBlock.TextProperty, myBinding);
    // Load this asynchronously
    myText.IsAsync = true;


Which tells the binding to not wait for the value but instead move on
with any other work while it waits for the value to come in. If you want
to display a placeholder value, we can set that as well.
    
    :::csharp
    MyData myDataObject = new MyData(DateTime.Now);
    Binding myBinding = new Binding("MyDataProperty");
    myBinding.Source = myDataObject;
    myText.SetBinding(TextBlock.TextProperty, myBinding);
    // Load this asynchronously
    myText.IsAsync = true;
    myText.FallbackValue = "Loading..."


Which will initially display "Loading..." until the value is ready from
the bound property. This is useful in situations where you want to load
an image which may take a while but want to hold some placeholder image
until it is ready (we see in many mobile applications where data loading
may be unpredictable and slow).

If you want to load multiple levels of objects, you can create a
PriorityBinding object which can contain multiple bindings as above, and
set each individual Binding object to be asynchronous and it will load
them in order as it gets them. You can find details about this on
[Microsoft's PriorityBinding MSDN documentation page][].

Lastly, remember that just because a value is asynchronous does not mean
it is automatically loaded from a different thread. If you want to
ensure that the UI thread is not held up, whichever property you are
bound to must have its data dispatched from another thread or launch a
thread. This will ensure that retrieving the property will take slightly
long and make the UI thread run smooth (user interactions will take
precedent).

  [MSDN's official documentation on the subject]: http://msdn.microsoft.com/en-us/library/ms752347.aspx
  [Microsoft's PriorityBinding MSDN documentation page]: http://msdn.microsoft.com/en-us/library/system.windows.data.prioritybinding.aspx

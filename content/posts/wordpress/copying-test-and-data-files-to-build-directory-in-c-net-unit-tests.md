Title: Copying Test and Data Files to Build Directory in C# .NET Unit Tests
Date: 2010-10-02 08:20
Author: Admin
Category: Programming
Tags: .net, unit testing

Unit testing with VS2010's built in unit testing facilities is
especially convenient. However it is no always clear how to specific
that an entire directory should be copied into the build / test
directory as data. Aside from setting up pre- and post- build rules,
VS2010 comes with a way to automatically include any project or
referenced directories and files as part of the build deployment. To
specify this, you use what is known as the testconfigs file.

First, open up your unit testing project with visual studio, and from
the test menu item, select edit test configuration.

![][]

</p>
Then, in the window that appears, select deployment and make sure that
the enable deployment check box is **selected**.

![][1]

</p>

Finally, just select add/remove file or directory and select what you
want to copy.

</p>

![][2]

</p>

</p>

Now, each time you run or deploy your projects you can select that
directories contents to also be copied over.

</p>

[Download Code.][]

</p>

  []: http://dans-coding-examples.googlecode.com/files/testcopy-editsettings.png
    "Test Copy Tutorial Edit Test Settings"
  [1]: http://dans-coding-examples.googlecode.com/files/testcopy-editdeployment.png
    "Test Copy Deployment"
  [2]: http://dans-coding-examples.googlecode.com/files/testcopy-editselect.png
    "http://dans-coding-examples.googlecode.com/files/testcopy-editselect.png"
  [Download Code.]: http://dans-coding-examples.googlecode.com/files/UnitTestingProject.zip

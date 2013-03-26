Title: OpenGL Display Lists And Sub Windows
Date: 2010-03-06 21:02
Author: Admin
Category: Programming
Tags: graphics, opengl

I recently discovered after some needless frustration, that you need to
declare display lists that contain model drawing information in all
windows in which you wish to draw the model. For example, if I say:

<p>
    glutSetWindow(main_window);initDisplayLists();...void main_display(){   drawDisplayList();}

</p>

It will work just fine. But if I try to do the same in a display
function of the sub window it won't draw. You need to call whatever
init() function you create your models / display lists in AFTER setting
the window. For example

<p>
    glutSetWindow(main_window);// do stuffglutSetWindow(sub_window);initDisplayLists();...void sub_display(){    drawDisplayList();}

</p>

Hope that helps someone out there!

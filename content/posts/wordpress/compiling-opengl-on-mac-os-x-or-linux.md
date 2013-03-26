Title: Compiling OpenGL on Mac OS X or Linux
Date: 2010-01-16 21:50
Author: Admin
Category: Programming

Most linux distributions make it easy to compile programs using OpenGL.
Other systems, however, aren't so easy. Here are instructions on how to
get it running in both platforms.

**Ubuntu / Linux**

1.  Make sure you install the opengl-mesa packages for opengl
    development. On ubuntu you can get them all with the following
    invocation:

    ```
    sudo apt-get install freeglut3-dev
    ```
    
2.  You should include the following \#includes in your code referencing
    opengl:

        :::c
        #include <GL/gl.h>
        #include <GL/glu.h>
        #include <GL/glut.h>

3.  You should also have the following gcc cmdline flags in your
    makefile:

    ```
    gcc -o simple simple.c -lGL -lglut -lGLU
    ```

**Mac OS X (tested on Snow Leopard)**

1.  For this to work you will have to install gcc and Xcode, which
    should install all the required opengl/glut libraries. You can get
    it [here][].

2.  Now, you'll have to alter all the \#includes in your files to
    conform to the proper location. Change all your opengl \#includes to
    the following:<span style="font-family: monospace;"> </span>

        :::c
        #include <OpenGL/gl.h>
        #include <OpenGL/glu.h>
        #include <GLUT/glut.h>

3.  Additionally your gcc command line will need to contain the
    following flags to link, along with any others you might have:

    ```
    gcc -o simple simple.c -framework Carbon -framework OpenGL -framework GLUT
    ```

**Cross Platform Compatibility**

**<span style="font-weight: normal;">If you want your code to run on
both, you need to get the Makefile and code to load the proper libraries
depending on your system. </span>**

**<span style="font-weight: normal;">In all your OpenGL .c files, add
the following header instead of your linux/mac includes:</span>**

    :::c
    #ifdef __APPLE__
    #  include <OpenGL/gl.h>
    #  include <OpenGL/glu.h>
    #  include <GLUT/glut.h>
    #else
    #  include <GL/gl.h>
    #  include <GL/glu.h>
    #  include <GL/glut.h>
    #endif

Then in your makefile, add the following before your build targets:

    :::make
    #default cmdline flags
    LDFLAGS  = -lGL -lglut -lGLU
    # Mac OS alternate cmdline link options
    ifeq "$(OSTYPE)" "Darwin"
      LDFLAGS = -framework Carbon -framework OpenGL -framework GLUT
    endif

[here]: http://developer.apple.com/

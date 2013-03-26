Title: Timing Programs in C (Update)
Date: 2009-01-25 17:03
Author: Admin
Category: Programming

So I've decided to try and do at least one useful post a week to
hopefully help a random searcher out. Here is the the updated version of
how to get millisecond precise wall clock time in C.

\#include \<sys\\time.h\>

`gettimeofday(&tstart, NULL);`

`double t1=tstart.tv_sec+(tstart.tv_usec/1000000.0);`

</p>


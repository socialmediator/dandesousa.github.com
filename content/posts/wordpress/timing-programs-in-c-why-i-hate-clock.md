Title: Timing Programs in C (Why I hate clock())
Date: 2009-01-16 08:51
Author: Admin
Category: Programming

So in working on a parallel programming assignment for a grad class I
needed to time two algorithms, a sequential approach and a parallel
approach. In doing so I did something like this:

 

`clock_t start, finish;`

`start = clock(); `

`// do something finish = clock(); `

`printf("Time Elapsed: %f", ((double) finish - start) / CLOCKS_PER_SEC); `

However this code will give you the wrong time if you are trying to
compare the runtime between these two types of programs.

On a sequential algorithm it should produce a good approximation of the
wall-clock time, or the amount of time that would expire if you timed it
using a clock on the wall (or stopwatch). But in a parallel algorithm we
find that it actually gives you a larger time difference.

This is because in a multi-threaded program you are engaging multiple
processors (if you have them). Since the clock() gets the number of
clock ticks for the program, we get back almost 2x as many (on a
two-core machine).

Unfortunately I have yet to find a decent way of getting the
milliseconds for a C program accurately. You can use regular old time()
to get the seconds, or if you are running on UNIX you can use the time
command.

</p>


Title: OpenMP and GCC Optimization
Date: 2009-02-10 20:34
Author: Admin
Category: Articles

So I encountered and interesting little affect while compiling some C
code in OpenMP using GCC. Seems that my code ran fine without any
automatic optimization flags (-O2, -O3), but when I turned them on, went
haywire. The sequential version wasn't affected.

I tracked down the problem and found that it was actually do to my use
of the private variable in the OpenMP directive. Here is a sample of the
problem.

    :::c
    #pragma omp parallel
    { 
    #pragma omp for private(i, j, new_j, skip_next)
        for(i = 0; i < n; i++) {
            // Set each thread on one row of the loop
            skip_next = 0;
            for(j = 0; j < n; j++)
            {
            ...

The problem actually occured because I did not have 'skip\_next=0' on
line 5 of this code. This didn't seem to matter when optimization was
disabled but did cause incorrect semantics when I turned it on. Seems
like OpenMP says you must assume that all privates are uninitialized
when you start a new directive block. If you want them to be private but
start with some default value, do what I did above or add the variable
to the firstprivate() attribute instead of the private attribute:


    :::c
    #pragma omp for firstprivate(skip_next) private(i, j, new_j)


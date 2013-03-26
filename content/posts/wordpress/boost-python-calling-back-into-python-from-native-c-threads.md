Title: [Boost.Python] Calling back into python from native C++ threads
Date: 2011-12-11 21:46
Author: Admin
Category: Programming
Tags: python, c++, programming, boost

So I came across a particularly frustrating problem dealing with a boost
python wrapper around a library which is calling python functions from
native c++ threads (boost threads in this case). The problem was that
some calls to release the global interpreter lock would cause python to
through fatal errors and segmentation fault, despite seeming to acquire
the GIL properly. This is how I solved the problem.

As a quick overview, you need to make sure that any native threads
acquire the GIL (global interpreter lock) before any sort of python
resources are touched. You may not use any C Python API functions or
call into python until the GIL is acquired. A good practice is to follow
the RIAA method for acquiring the GIL like so:

    :::c++
    class ScopedGILRelease
    {
        public:
            inline ScopedGILRelease()
            {
                d_gstate = PyGILState_Ensure();
            }
            inline ~ScopedGILRelease()
            {
                PyGILState_Release(d_gstate);
            }
        private:
            PyGILState_STATE d_gstate;
    };

    void onData(const boost::shared_ptr<Data>::P & data, const void *
            closure)
    {
        ScopedGILRelease gil_lock;
        // invoke call_method to python
    }

In the above example we call the lock which invokes PyGILState\_Ensure()
to acquire the lock. Additionally we call PyGILState\_Release() on the
same thread state object when we go out of scope.

What bit me when developing this solution was that the api was not being
properly initialized. Originally I was calling two functions in my one
of my modules objects which I assumed was going to be called before any
threads were made.

    :::c++
    PyEval_InitThreads();
    PyEval_ReleaseLock();

Now according to the [python documentation][], the first thread should:

<p>
> Initialize and acquire the global interpreter lock. It should be
> called in the main thread before creating a second thread or engaging
> in any other thread operations such as PyEval_ReleaseLock() or
> PyEval_ReleaseThread(tstate). It is not needed before calling
> PyEval_SaveThread() or PyEval_RestoreThread().
</p>

However, that documentation is either incorrect or something very subtle
was going on in my library, since PyEval\_InitThreads() was being called
before any thread operations and the object was being created in the
main thread of the python interpreter. Perhaps I couldn't guarantee that
python wasn't spawning some sub-thread to handle that part of the
script. Anyway I found that I had to instead call PyEval\_InitThreads()
once in the module definition macro for boost python. Looking something
like this:

    :::c++
    BOOST_PYTHON_MODULE(ModuleName)
    {
        PyEval_InitThreads();
        ...
    }

As always a super simple solution to a super frustrating problem. This
information was extremely hard to find, so hopefully this helps someone
out there from losing hours of time. [Also, here is a link to the stack
overflow question I eventually posted and quickly subsequently
answered][].

Enjoy.

  [python documentation]: http://docs.python.org/c-api/init.html#PyEval_InitThreads
  [Also, here is a link to the stack overflow question I eventually posted and quickly subsequently answered]: http://stackoverflow.com/questions/8451334/why-is-pygilstate-release-throwing-fatal-python-errors/8469304#8469304

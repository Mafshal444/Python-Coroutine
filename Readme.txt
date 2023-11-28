In language like python where code is executed synchronously, coroutines are introduced which allow code to be paused and resume
at points.
A coroutine is a function/ program which can be resumed or paused.
In python code execution is on default synchronously means if there is a blocking code like network request, next block of code
will not execute untill previous response is returned. this will block whole program.
But with asyncio this behavior is eliminated using concurrent programing pradiagm. In this asyncio makes function async means
If we have any blocking code we can make it async/await and it will be executed in background without blocking the whole program.
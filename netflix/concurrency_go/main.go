// Implement a scheduled thread pool
//
// What is a scheduled thread pool?
// A scheduled thread pool is a thread pool that can schedule tasks to run after a delay, or to execute periodically.
//
// How does a scheduled thread pool work?
// A scheduled thread pool works by using a priority queue to store tasks that are scheduled to run in the future.
// The thread pool has a fixed number of worker threads that are used to execute tasks.
// When a task is scheduled to run, it is added to the priority queue, and the worker threads check the
// priority queue for tasks to execute. If a task is scheduled to run in the future, the worker threads
// wait until the scheduled time before executing the task.

// You need to implement it from scratch.
// I’d be looking for producer/consumer queue.  Thread safety.  Proper thread signaling.  Etc…

package main

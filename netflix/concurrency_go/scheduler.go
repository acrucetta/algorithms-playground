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

import (
	"fmt"
	"sync"
	"time"
)

type Task struct {
	value    string
	priority int
	index    int
	schedule time.Time
}

type PriorityQueue []*Task

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq *PriorityQueue) Push(x any) {
	n := len(*pq)
	item := x.(*Task)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() *Task {
	old := *pq
	n := len(old)
	item := old[n-1]
	// Clean up the variables
	old[n-1] = nil
	item.index = -1
	*pq = old[0 : n-1]
	return item
}

type SchedulerThreadPool struct {
	w          sync.Mutex
	cond       *sync.Cond
	taskQueue  PriorityQueue
	numWorkers int
	wg         sync.WaitGroup
}

func workUnit(pool *SchedulerThreadPool) {
	for {
		pool.w.Lock()
		if len(pool.taskQueue) == 0 && pool.numWorkers > 0 {
			pool.cond.Wait()
		}
		if pool.numWorkers == 0 {
			pool.w.Unlock()
			return
		}
		task := pool.taskQueue.Pop()
		pool.w.Unlock()

		// Execute
		fmt.Println("%s", task.value)

		time.Sleep(time.Second) // Simulate task execution

		pool.w.Lock()
		pool.cond.Signal()
		pool.w.Unlock()
	}
}

func NewThreadPool() *SchedulerThreadPool {
	pool := SchedulerThreadPool{}
	pool.w = sync.Mutex{}
	pool.cond = sync.NewCond(&pool.w)
	return &pool
}

func (pool *SchedulerThreadPool) Start() {
	// Kicks off the pool and adds each worker to
	// a wait group where they will be starting to grab tasks
	for i := 0; i < pool.numWorkers; i++ {
		pool.wg.Add(1)
		go func() {
			defer pool.wg.Done()
			workUnit(pool)
		}()
	}
}

func (pool *SchedulerThreadPool) Stop() {
	pool.w.Lock()
	pool.numWorkers = 0
	pool.cond.Broadcast()
	pool.w.Unlock()
	pool.wg.Wait()
}

func main() {
	tasks := map[string]int{
		"banana": 3, "apple": 2, "pear": 4, "tomato": 1,
		"pumpkin": 10,
	}

	threadPool := NewThreadPool()
	threadPool.numWorkers = 5

	// Add tasks to the PriorityQueuerity queue
	pq := PriorityQueue{}
	var taskList []Task
	i := 0

	for str, priority := range tasks {
		taskList = append(taskList, Task{str, priority, i, time.Now()})
	}

	threadPool.Start()

	for _, task := range taskList {
		threadPool.taskQueue.Push(&task)
	}

	// Wait for a specific duration or user input to stop the thread pool
	time.Sleep(5 * time.Second)

	threadPool.Stop()
}

package main

import (
	"fmt"
	"sync"
	"time"
)

var (
	lock       sync.Mutex
	sharedData int
)

func increment(duration time.Duration) {
	lock.Lock()
	<-time.After(duration)
	defer lock.Unlock()
	sharedData++
}

func worker() {
	fmt.Printf("Bob")
}

func producer(ch chan<- int) {
	for i := 0; i < 10; i++ {
		ch <- i
	}
	close(ch)
}

func consumer(ch <-chan int) {
	for i := range ch {
		fmt.Println(i)
	}
}

func main() {
	var wg sync.WaitGroup
	for i := 0; i < 5; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			increment(0)
		}()
	}
	wg.Wait()
	fmt.Printf("Shared data: %d\n", sharedData)
}

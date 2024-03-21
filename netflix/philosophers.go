package main

import (
	"fmt"
	"sync"
	"time"
)

const (
    numPhilosophers = 5
    numMeals        = 3
)

type Philosopher struct {
    id              int
    leftFork, rightFork *sync.Mutex
}

func (p Philosopher) eat() {
    for i := 0; i < numMeals; i++ {
        p.leftFork.Lock()
        p.rightFork.Lock()

        fmt.Printf("Philosopher %d is eating\n", p.id)
        time.Sleep(time.Second)

        p.rightFork.Unlock()
        p.leftFork.Unlock()

        fmt.Printf("Philosopher %d is thinking\n", p.id)
        time.Sleep(time.Second)
    }
}

func main() {
    forks := make([]*sync.Mutex, numPhilosophers)
    for i := 0; i < numPhilosophers; i++ {
        forks[i] = &sync.Mutex{}
    }

    philosophers := make([]*Philosopher, numPhilosophers)
    for i := 0; i < numPhilosophers; i++ {
        philosophers[i] = &Philosopher{
            id:        i,
            leftFork:  forks[i],
            rightFork: forks[(i+1)%numPhilosophers],
        }
    }

    var wg sync.WaitGroup
    wg.Add(numPhilosophers)

    for i := 0; i < numPhilosophers; i++ {
        go func(p *Philosopher) {
            p.eat()
            wg.Done()
        }(philosophers[i])
    }

    wg.Wait()
}
package main

import (
	"fmt"
	"sync"
)

func foo(ctx FooContext) {
	fmt.Print("foo")
	ctx.wg.Done()
}

func bar(ctx FooContext) {
	fmt.Print("bar\n")
	ctx.wg.Done()
}

type FooContext struct {
	wg *sync.WaitGroup
}

func main() {
	// We want to run foo first,
	// then bar, and to run it X amount
	// of times

	// To sequence the runs we might need a wait group
	// that prints the sequences in order
	ctx := FooContext{}
	ctx.wg = &sync.WaitGroup{}
	const n = 5
	for i := 0; i < n; i++ {
		ctx.wg.Add(1)
		go foo(ctx)
		ctx.wg.Wait()

		ctx.wg.Add(1)
		go bar(ctx)
		ctx.wg.Wait()
	}
}

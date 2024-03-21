package main

import "sync"

type RWLock struct {
	w           *sync.Mutex
	cond        *sync.Cond
	writerCount int32
	readerCount int32
}

const maxReaders = 32

func NewRWLock() *RWLock {
	rw := RWLock{}
	rw.readerCount = maxReaders
	rw.w = &sync.Mutex{}
	rw.cond = sync.NewCond(rw.w)
	return &rw
}

func (rw RWLock) AcquireReadLock() {
	rw.w.Lock()
	defer rw.w.Unlock()
	if rw.writerCount == 0 || rw.readerCount < 32 {
		rw.cond.Signal()
	} else {
		for rw.writerCount > 0 || rw.readerCount >= 32 {
			rw.cond.Wait()
		}
	}
	rw.readerCount++
}

func (rw RWLock) AcquireWriteLock() {
	rw.w.Lock()
	defer rw.w.Unlock()
	if rw.writerCount > 0 || rw.readerCount > 0 {
		rw.cond.Wait()
	}
	rw.writerCount++
	return
}
func (rw RWLock) ReleaseReadLock() {
	rw.w.Lock()
	defer rw.w.Unlock()
	rw.readerCount--
	rw.cond.Signal()
}

func (rw RWLock) ReleaseWriteLock() {
	rw.w.Lock()
	defer rw.w.Unlock()
	rw.writerCount--
	rw.cond.Signal()
}

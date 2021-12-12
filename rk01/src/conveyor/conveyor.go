package conveyor

import (
	"time"
)

func ParallelConveyor(inQueue *Queue) (*Queue, time.Duration) {
	mainToF := make(chan *Sleepyhead, inQueue.capacity)
	fToS := make(chan *Sleepyhead, inQueue.capacity)
	sToT := make(chan *Sleepyhead, inQueue.capacity)
	tToMain := make(chan int)
	res := CreateQueue(inQueue.capacity)

	first := func() {
		for {
			select {
			case c := <-mainToF:
				c.start1 = time.Now()
				time.Sleep(c.time1)
				c.end1 = time.Now()

				fToS <- c
			}
		}
	}

	second := func() {
		for {
			select {
			case c := <-fToS:
				c.start2 = time.Now()
				time.Sleep(c.time2)
				c.end2 = time.Now()

				sToT <- c

			}
		}
	}

	third := func() {
		for {
			select {
			case c := <-sToT:
				c.start3 = time.Now()
				time.Sleep(c.time3)
				c.end3 = time.Now()

				res.Push(c)
				if res.tail == res.capacity-1 {
					tToMain <- 0
				}
			}
		}
	}

	go first()
	go second()
	go third()

	cip := inQueue.Pop()
	for cip != nil {
		mainToF <- cip
		cip = inQueue.Pop()
	}

	start := time.Now()
	<-tToMain
	fullTime := time.Now().Sub(start)

	return res, fullTime
}

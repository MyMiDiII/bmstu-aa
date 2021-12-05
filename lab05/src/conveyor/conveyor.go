package conveyor

import (
	"time"
)

func LinearConveyor(inQueue *Queue) *Queue {
	res := CreateQueue(inQueue.capacity)

	c := inQueue.Pop()
	for c != nil {
		c.startMsg = time.Now()
		GenerateMsg(c)
		c.endMsg = time.Now()

		c.startReplace = time.Now()
		ReverseWords(c)
		c.endReplace = time.Now()

		c.startVegenere = time.Now()
		CodeByVegenere(c)
		c.endVegenere = time.Now()

		res.Push(c)
		c = inQueue.Pop()
	}

	return res
}

func ParallelConveyor(inQueue *Queue) *Queue {
	mainToF := make(chan *Cipher, inQueue.capacity)
	fToS := make(chan *Cipher, inQueue.capacity)
	sToT := make(chan *Cipher, inQueue.capacity)
	tToMain := make(chan int)
	res := CreateQueue(inQueue.capacity)

	first := func() {
		for {
			select {
			case c := <-mainToF:
				c.startMsg = time.Now()
				GenerateMsg(c)
				c.endMsg = time.Now()

				fToS <- c
			}
		}
	}

	second := func() {
		for {
			select {
			case c := <-fToS:
				c.startReplace = time.Now()
				ReverseWords(c)
				c.endReplace = time.Now()

				sToT <- c

			}
		}
	}

	third := func() {
		for {
			select {
			case c := <-sToT:
				c.startVegenere = time.Now()
				CodeByVegenere(c)
				c.endVegenere = time.Now()

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

	<-tToMain

	return res
}

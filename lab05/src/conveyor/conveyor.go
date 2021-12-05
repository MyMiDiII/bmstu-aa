package conveyor

import "time"

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

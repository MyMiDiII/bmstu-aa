package conveyor

type Queue struct {
	data     [](*Sleepyhead)
	tail     int
	capacity int
}

func CreateQueue(num int) *Queue {
	queue := new(Queue)
	queue.data = make([]*Sleepyhead, num, num)
	queue.tail = -1
	queue.capacity = num

	return queue
}

func (queue *Queue) Push(c *Sleepyhead) {
	if queue.tail != len(queue.data)-1 {
		queue.data[queue.tail+1] = c
		queue.tail++
	}
}

func (queue *Queue) Pop() *Sleepyhead {
	if queue.tail < 0 {
		return nil
	}

	next := queue.data[0]
	queue.data = queue.data[1:]
	queue.tail--

	return next
}

func (to *Queue) GetCopyBy(from *Queue) {
	to.data = make([]*Sleepyhead, from.capacity, from.capacity)

	for i, el := range from.data {
		to.data[i] = el
	}

	to.tail = from.tail
	to.capacity = from.capacity
}

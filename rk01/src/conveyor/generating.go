package conveyor

import (
	"math/rand"
	"time"
)

func genIntAB(a int, b int) int {
	return a + rand.Intn(b-a+1)
}

func GenerateRequests(num int, avgTimes [3]int, avgDeltaTimes [3]int) *Queue {
	queue := CreateQueue(num)

	for i := 0; i < num; i++ {
		sleepy := new(Sleepyhead)

		sleepy.SetTime1(time.Duration(genIntAB(avgTimes[0]-avgDeltaTimes[0],
			avgTimes[0]+avgDeltaTimes[0])) * time.Millisecond)
		sleepy.SetTime2(time.Duration(genIntAB(avgTimes[1]-avgDeltaTimes[1],
			avgTimes[1]+avgDeltaTimes[1])) * time.Millisecond)
		sleepy.SetTime3(time.Duration(genIntAB(avgTimes[2]-avgDeltaTimes[2],
			avgTimes[2]+avgDeltaTimes[2])) * time.Millisecond)

		queue.Push(sleepy)
	}

	return queue
}

package conveyor

import "math/rand"

func GenerateRequests(num int, min int, max int) (*Queue, *Queue) {
	queueL := CreateQueue(num)
	queueP := CreateQueue(num)

	for i := 0; i < num; i++ {
		msgL := new(Cipher)
		msgP := new(Cipher)

		words := min + rand.Intn(max-min+1)
		msgL.SetWordsNum(words)
		msgP.SetWordsNum(words)

		queueL.Push(msgL)
		queueP.Push(msgP)
	}

	return queueL, queueP
}

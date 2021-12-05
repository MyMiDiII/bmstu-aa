package main

import (
	"fmt"
	"math/rand"
	"time"

	. "github.com/logrusorgru/aurora"

	. "./conveyor"
)

func generateRequests(num int) (*Queue, *Queue) {
	MINNUM := 3
	MAXNUM := 8

	queueL := CreateQueue(num)
	queueP := CreateQueue(num)

	for i := 0; i < num; i++ {
		msgL := new(Cipher)
		msgP := new(Cipher)

		words := MINNUM + rand.Intn(MAXNUM-MINNUM+1)
		msgL.SetWordsNum(words)
		msgP.SetWordsNum(words)

		queueL.Push(msgL)
		queueP.Push(msgP)
	}

	return queueL, queueP
}

func main() {
	fmt.Println(Green("Конвейерная обработка\n"))

	fmt.Print("Введите количество заявок: ")
	var num int
	fmt.Scanf("%d", &num)

	if num == 0 {
		fmt.Println("Число заявок -- натуральное!")
		return
	}

	if num < 0 {
		num = -num
	}

	queueL, queueP := generateRequests(num)

	start := time.Now()
	resL := LinearConveyor(queueL)
	end := time.Now()

	PrintLog(start, end, resL, false)

	start = time.Now()
	resP := ParallelConveyor(queueP)
	end = time.Now()

	PrintLog(start, end, resP, true)
}

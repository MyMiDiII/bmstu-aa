package main

import (
	"fmt"
	"time"

	. "github.com/logrusorgru/aurora"

	. "./conveyor"
)

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

	queueL, queueP := GenerateRequests(num, 3, 8)

	start := time.Now()
	resL := LinearConveyor(queueL)
	end := time.Now()

	PrintLog(start, end, resL, false)

	start = time.Now()
	resP := ParallelConveyor(queueP)
	end = time.Now()

	PrintLog(start, end, resP, false)
}

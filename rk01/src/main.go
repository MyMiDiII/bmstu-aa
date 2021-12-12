package main

import (
	"fmt"

	. "github.com/logrusorgru/aurora"

	. "./conveyor"
)

func readNum() int {
	var num int
	fmt.Scanf("%d", &num)

	if num == 0 {
		fmt.Println("Число заявок -- натуральное!")
		return -1
	}

	if num < 0 {
		num = -num
	}

	return num
}

func readNotNeg() int {
	var num int
	fmt.Scanf("%d", &num)

	if num < 0 {
		num = -num
	}

	return num

}

func readNatural() int {
	var num int
	fmt.Scanf("%d", &num)

	if num == 0 {
		fmt.Println("Число должно быть натуральным!")
		return -1
	}

	if num < 0 {
		num = -num
	}

	return num
}

func main() {
	fmt.Println(Green("Конвейерная обработка\n"))

	fmt.Print("Введите число заявок: ")
	num := readNum()

	if num < 0 {
		return
	}

	avgTimes := [...]int{0, 0, 0}
	avgDeltaTimes := [...]int{0, 0, 0}

	for i := 0; i < 3; i++ {
		fmt.Println(i+1, "лента")
		fmt.Print("Введите среднее время обработки заявки: ")
		avgTimes[i] = readNum()

		if avgTimes[i] < 0 {
			return
		}

		fmt.Print("Введите разброс времени обработки заявки: ")
		avgDeltaTimes[i] = readNotNeg()

		if avgDeltaTimes[i] < 0 {
			return
		}
	}

	queue := GenerateRequests(num, avgTimes, avgDeltaTimes)

	res, fullTime := ParallelConveyor(queue)

	PrintLog(fullTime, res, true, true)
}

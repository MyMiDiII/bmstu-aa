package main

import (
	"fmt"

	. "github.com/logrusorgru/aurora"
)

func main() {
	fmt.Println(Green("Конвейерная обработка"))

	fmt.Print("Введите количество заявок: ")
	var num uint
	fmt.Scanf("%d", &num)

	if num == 0 {
		fmt.Println("Число заявок -- натуральное!")
		return
	}

	fmt.Println(num)
}

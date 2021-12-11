package conveyor

import (
	"fmt"
	"os"
	"sort"
	"time"

	"github.com/olekukonko/tablewriter"
)

type logRow struct {
	requestNum int
	stage      int
	start      time.Duration
	end        time.Duration
}

func PrintLog(full time.Duration, q *Queue, needSort bool,
	needTable bool) (time.Duration, time.Duration, time.Duration) {
	reqTime1 := time.Duration(0)
	reqTime2 := time.Duration(0)
	reqTime3 := time.Duration(0)

	tmp := new(Queue)
	tmp.GetCopyBy(q)
	log := make([]logRow, q.capacity*3, q.capacity*3)

	i := 0
	j := 0
	c := tmp.Pop()
	begin := c.start1
	for c != nil {
		log[j] = logRow{
			requestNum: i,
			stage:      1,
			start:      c.start1.Sub(begin),
			end:        c.end1.Sub(begin)}
		reqTime1 += log[j].end - log[j].start
		j++

		log[j] = logRow{
			requestNum: i,
			stage:      2,
			start:      c.start2.Sub(begin),
			end:        c.end2.Sub(begin)}
		reqTime2 += log[j].end - log[j].start
		j++

		log[j] = logRow{
			requestNum: i,
			stage:      3,
			start:      c.start3.Sub(begin),
			end:        c.end3.Sub(begin)}
		reqTime3 += log[j].end - log[j].start
		i++
		j++

		c = tmp.Pop()
	}

	if needSort {
		sort.Slice(log, func(i, j int) bool {
			f := log[i].stage == log[j].stage

			if f {
				return log[i].start < log[j].start
			}

			return log[i].stage < log[j].stage
		})
	} else {
		sort.Slice(log, func(i, j int) bool {
			return log[i].start < log[j].start
		})
	}

	if needTable {
		table := tablewriter.NewWriter(os.Stdout)
		table.SetHeader([]string{"#", "Stage", "Begin", "End"})

		for _, v := range log {
			f := fmt.Sprintf("%v", v.requestNum)
			s := fmt.Sprintf("%v", v.stage)
			t := fmt.Sprintf("%v", v.start)
			fo := fmt.Sprintf("%v", v.end)
			table.Append([]string{f, s, t, fo})
		}

		table.Render()
		fmt.Println("TOTAL: ", full)
	}

	fullLine1Time := log[q.capacity-1].end - log[0].start
	fullLine2Time := log[q.capacity*2-1].end - log[q.capacity].start
	fullLine3Time := log[q.capacity*3-1].end - log[q.capacity*2].start

	downTime1 := fullLine1Time - reqTime1
	downTime2 := fullLine2Time - reqTime2
	downTime3 := fullLine3Time - reqTime3

	fmt.Println("Время простоя 1 ленты:", downTime1)
	fmt.Println("Время простоя 2 ленты:", downTime2)
	fmt.Println("Время простоя 3 ленты:", downTime3)

	return downTime1, downTime2, downTime3
}

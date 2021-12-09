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

func PrintLog(start time.Time, end time.Time, q *Queue, needSort bool) {
	tmp := new(Queue)
	tmp.GetCopyBy(q)
	log := make([]logRow, q.capacity*3, q.capacity*3)

	i := 0
	j := 0
	c := tmp.Pop()
	begin := c.startMsg
	for c != nil {
		log[j] = logRow{
			requestNum: i,
			stage:      1,
			start:      c.startMsg.Sub(begin),
			end:        c.endMsg.Sub(begin)}
		j++

		log[j] = logRow{
			requestNum: i,
			stage:      2,
			start:      c.startReplace.Sub(begin),
			end:        c.endReplace.Sub(begin)}
		j++

		log[j] = logRow{
			requestNum: i,
			stage:      3,
			start:      c.startVegenere.Sub(begin),
			end:        c.endVegenere.Sub(begin)}
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

	table := tablewriter.NewWriter(os.Stdout)
	table.SetHeader([]string{"№", "Stage", "Begin", "End"})

	for _, v := range log {
		f := fmt.Sprintf("%v", v.requestNum)
		s := fmt.Sprintf("%v", v.stage)
		t := fmt.Sprintf("%v", v.start)
		fo := fmt.Sprintf("%v", v.end)
		table.Append([]string{f, s, t, fo})
	}
	table.Render()
	fmt.Println("TOTAL: ", end.Sub(start))
}

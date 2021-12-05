package conveyor

import (
	"fmt"
	"os"
	"sort"
	. "time"

	"github.com/olekukonko/tablewriter"
	//. "github.com/logrusorgru/aurora"
)

type logRow struct {
	requestNum int      `header:"№"`
	stage      int      `header:"stage"`
	start      Duration `header:"begin"`
	end        Duration `header:"end"`
}

func PrintLog(start Time, end Time, q *Queue) {
	tmp := new(Queue)
	tmp.GetCopyBy(q)
	//fmt.Println(q.data)
	//fmt.Println(tmp.data)
	log := make([]logRow, q.capacity*3, q.capacity*3)

	//dif := end.Sub(start)

	i := 0
	j := 0
	c := tmp.Pop()
	begin := c.startMsg
	for c != nil {
		//fmt.Println("q", q.data)
		//fmt.Println("tmp", tmp.data)
		//fmt.Println("log")
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

	//for _, l := range log {
	//	fmt.Println(l.requestNum, l.start)
	//}

	sort.Slice(log, func(i, j int) bool {
		return log[i].start < log[j].start
	})

	table := tablewriter.NewWriter(os.Stdout)
	table.SetHeader([]string{"№", "Stage", "Begin", "End"})

	for _, v := range log {
		f := fmt.Sprintf("%v", v.requestNum)
		s := fmt.Sprintf("%v", v.stage)
		t := fmt.Sprintf("%v", v.start)
		fo := fmt.Sprintf("%v", v.end)
		table.Append([]string{f, s, t, fo})
	}
	table.Render() // Send output

	//for _, l := range log {
	//	fmt.Println(l.requestNum, l.start)
	//}

	//fmt.Println(dif)
	//fmt.Println(log[0].stage)
}

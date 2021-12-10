package conveyor

import (
	"testing"
	"time"
)

func TestFindPrepare(t *testing.T) {
	reqNum := 10

	avgDeltaTimes := [...]int{0, 0, 0}

	for i := 1; i <= 1000; i *= 10 {
		avgTimes := [...]int{i, i, i}
		trueTime := time.Duration(12*i) * time.Millisecond
		q := GenerateRequests(reqNum, avgTimes, avgDeltaTimes)
		_, gotTime := ParallelConveyor(q)
		t.Log("True =", trueTime)
		t.Log("Got =", gotTime)
		t.Log("Dif =", gotTime-trueTime)
	}
}

func TestDeltas(t *testing.T) {
	reqNum := 10

	avgTimes := [...]int{1000, 1000, 1000}

	for i := 10; i < 920; i += 100 {
		t.Log("delta = ", i)
		avgDeltaTimes := [...]int{i, i, i}
		q := GenerateRequests(reqNum, avgTimes, avgDeltaTimes)
		res, gotTime := ParallelConveyor(q)
		PrintLog(gotTime, res, true, false)
	}
}

func Test111(t *testing.T) {
	reqNum := 10

	avgTimes := [...]int{1000, 1000, 1000}

	avgDeltaTimes := [...]int{200, 200, 200}
	q := GenerateRequests(reqNum, avgTimes, avgDeltaTimes)
	res, gotTime := ParallelConveyor(q)
	PrintLog(gotTime, res, true, false)
}

func Test211(t *testing.T) {
	reqNum := 10

	avgTimes := [...]int{2000, 1000, 1000}

	avgDeltaTimes := [...]int{200, 200, 200}
	q := GenerateRequests(reqNum, avgTimes, avgDeltaTimes)
	res, gotTime := ParallelConveyor(q)
	PrintLog(gotTime, res, true, false)
}

func Test121(t *testing.T) {
	reqNum := 10

	avgTimes := [...]int{1000, 2000, 1000}

	avgDeltaTimes := [...]int{200, 200, 200}
	q := GenerateRequests(reqNum, avgTimes, avgDeltaTimes)
	res, gotTime := ParallelConveyor(q)
	PrintLog(gotTime, res, true, false)
}

func Test112(t *testing.T) {
	reqNum := 10

	avgTimes := [...]int{1000, 1000, 2000}

	avgDeltaTimes := [...]int{200, 200, 200}
	q := GenerateRequests(reqNum, avgTimes, avgDeltaTimes)
	res, gotTime := ParallelConveyor(q)
	PrintLog(gotTime, res, true, false)
}

func Test221(t *testing.T) {
	reqNum := 10

	avgTimes := [...]int{2000, 2000, 1000}

	avgDeltaTimes := [...]int{200, 200, 200}
	q := GenerateRequests(reqNum, avgTimes, avgDeltaTimes)
	res, gotTime := ParallelConveyor(q)
	PrintLog(gotTime, res, true, false)
}

func Test122(t *testing.T) {
	reqNum := 10

	avgTimes := [...]int{1000, 2000, 2000}

	avgDeltaTimes := [...]int{200, 200, 200}
	q := GenerateRequests(reqNum, avgTimes, avgDeltaTimes)
	res, gotTime := ParallelConveyor(q)
	PrintLog(gotTime, res, true, false)
}

func Test212(t *testing.T) {
	reqNum := 10

	avgTimes := [...]int{2000, 1000, 2000}

	avgDeltaTimes := [...]int{200, 200, 200}
	q := GenerateRequests(reqNum, avgTimes, avgDeltaTimes)
	res, gotTime := ParallelConveyor(q)
	PrintLog(gotTime, res, true, false)
}

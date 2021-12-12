package conveyor

import "time"

type Sleepyhead struct {
	time1 time.Duration
	time2 time.Duration
	time3 time.Duration

	start1 time.Time
	start2 time.Time
	start3 time.Time
	end1   time.Time
	end2   time.Time
	end3   time.Time
}

func (s *Sleepyhead) SetTime1(t time.Duration) {
	s.time1 = t
}

func (s *Sleepyhead) SetTime2(t time.Duration) {
	s.time2 = t
}

func (s *Sleepyhead) SetTime3(t time.Duration) {
	s.time3 = t
}

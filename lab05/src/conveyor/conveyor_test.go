package conveyor

import "testing"

func BenchmarkPConv5(b *testing.B) {
	reqNum := 5

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		ParallelConveyor(q)
	}
}

func BenchmarkPConv10(b *testing.B) {
	reqNum := 10

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		ParallelConveyor(q)
	}
}

func BenchmarkPConv25(b *testing.B) {
	reqNum := 25

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		ParallelConveyor(q)
	}
}

func BenchmarkPConv50(b *testing.B) {
	reqNum := 50

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		ParallelConveyor(q)
	}
}

func BenchmarkPConv75(b *testing.B) {
	reqNum := 75

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		ParallelConveyor(q)
	}
}

func BenchmarkPConv100(b *testing.B) {
	reqNum := 100

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		ParallelConveyor(q)
	}
}

func BenchmarkPConv250(b *testing.B) {
	reqNum := 250

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		ParallelConveyor(q)
	}
}

func BenchmarkPConv500(b *testing.B) {
	reqNum := 500

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		ParallelConveyor(q)
	}
}

func BenchmarkPConv750(b *testing.B) {
	reqNum := 750

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		ParallelConveyor(q)
	}
}

func BenchmarkPConv1000(b *testing.B) {
	reqNum := 1000

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		ParallelConveyor(q)
	}
}

func BenchmarkLConv5(b *testing.B) {
	reqNum := 5

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		LinearConveyor(q)
	}
}

func BenchmarkLConv10(b *testing.B) {
	reqNum := 10

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		LinearConveyor(q)
	}
}

func BenchmarkLConv25(b *testing.B) {
	reqNum := 25

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		LinearConveyor(q)
	}
}

func BenchmarkLConv50(b *testing.B) {
	reqNum := 50

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		LinearConveyor(q)
	}
}

func BenchmarkLConv75(b *testing.B) {
	reqNum := 75

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		LinearConveyor(q)
	}
}

func BenchmarkLConv100(b *testing.B) {
	reqNum := 100

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		LinearConveyor(q)
	}
}

func BenchmarkLConv250(b *testing.B) {
	reqNum := 250

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		LinearConveyor(q)
	}
}

func BenchmarkLConv500(b *testing.B) {
	reqNum := 500

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		LinearConveyor(q)
	}
}

func BenchmarkLConv750(b *testing.B) {
	reqNum := 750

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		LinearConveyor(q)
	}
}

func BenchmarkLConv1000(b *testing.B) {
	reqNum := 1000

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 3, 8)

		b.StartTimer()
		LinearConveyor(q)
	}
}

func BenchmarkPConvRS5(b *testing.B) {
	reqNum := 50

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 5, 5)

		b.StartTimer()
		ParallelConveyor(q)
	}
}

func BenchmarkPConvRS10(b *testing.B) {
	reqNum := 50

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 10, 10)

		b.StartTimer()
		ParallelConveyor(q)
	}
}

func BenchmarkPConvRS25(b *testing.B) {
	reqNum := 50

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 25, 25)

		b.StartTimer()
		ParallelConveyor(q)
	}
}

func BenchmarkPConvRS50(b *testing.B) {
	reqNum := 50

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 50, 50)

		b.StartTimer()
		ParallelConveyor(q)
	}
}

func BenchmarkPConvRS75(b *testing.B) {
	reqNum := 50

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 75, 75)

		b.StartTimer()
		ParallelConveyor(q)
	}
}

func BenchmarkPConvRS100(b *testing.B) {
	reqNum := 50

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 100, 100)

		b.StartTimer()
		ParallelConveyor(q)
	}
}

func BenchmarkLConvRS5(b *testing.B) {
	reqNum := 50

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 5, 5)

		b.StartTimer()
		LinearConveyor(q)
	}
}

func BenchmarkLConvRS10(b *testing.B) {
	reqNum := 50

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 10, 10)

		b.StartTimer()
		LinearConveyor(q)
	}
}

func BenchmarkLConvRS25(b *testing.B) {
	reqNum := 50

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 25, 25)

		b.StartTimer()
		LinearConveyor(q)
	}
}

func BenchmarkLConvRS50(b *testing.B) {
	reqNum := 50

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 50, 50)

		b.StartTimer()
		LinearConveyor(q)
	}
}

func BenchmarkLConvRS75(b *testing.B) {
	reqNum := 50

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 75, 75)

		b.StartTimer()
		LinearConveyor(q)
	}
}

func BenchmarkLConvRS100(b *testing.B) {
	reqNum := 50

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		q, _ := GenerateRequests(reqNum, 100, 100)

		b.StartTimer()
		LinearConveyor(q)
	}
}

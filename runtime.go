package main
type Run struct {
    Time int // in milliseconds
    Results string
    Failed bool
}

// Get average runtime of successful runs in seconds
func (r *Run) GetAverageRuntime() float64 {
    var total int
    var count int
    for _, run := range r {
        if !run.Failed {
            total += run.Time
            count++
        }
    }
    return float64(total) / float64(count) / 1000
}   

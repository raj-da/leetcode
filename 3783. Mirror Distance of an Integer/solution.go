func mirrorDistance(n int) int {
    return int(math.Abs(float64(n - reverse(n))))
}

func reverse(n int) int {
    res := 0
    for n > 0 {
        res = res*10 + n%10
        n /= 10
    }
    return res
}

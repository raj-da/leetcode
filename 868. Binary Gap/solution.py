func binaryGap(n int) int {
    maxDistance := 0

    bits := []int{}
    for n > 0 {
        if n & 1 == 0 {
            bits = append(bits, 0)
        } else {
            bits = append(bits, 1)
        }
        n = n >> 1
    }

    n = len(bits)
    l := 0
    for l < n && bits[l] == 0 {
        l++
    }
    r := l + 1
    for r < n {
        for r < n && bits[r] == 0 {
            r++
        }
        if r < n {
            if r - l > maxDistance {
                maxDistance = r - l
            }
        }
        l = r
        r++
    }
    return maxDistance 
}   

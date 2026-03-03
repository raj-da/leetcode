func findKthBit(n int, k int) byte {
    if n == 1 {
        return '0'
    }

    mid := 1 << (n - 1)

    if k == mid {
        return '1'
    }

    if k < mid {
        return findKthBit(n-1, k)
    }

    mirrored := mid - (k - mid)
    bit := findKthBit(n-1, mirrored)

    if bit == '0' {
        return '1'
    }
    return '0'
}

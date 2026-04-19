func maxDistance(nums1 []int, nums2 []int) int {
    res := 0
    i, j := 0, 0

    for (i < len(nums1)) && (j < len(nums2)) {
        if nums1[i] <= nums2[j] {
            if j - i > res { res = j - i}
            j++
        } else { i++ }
    }
    
    return int(res)
}

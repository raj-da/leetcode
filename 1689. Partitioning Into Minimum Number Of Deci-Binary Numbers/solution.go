func minPartitions(n string) int {
    result := 0

	for _, ch := range n {
		digit := int(ch - '0')
		if digit > result {
			result = digit
		}
	}

    return result
}

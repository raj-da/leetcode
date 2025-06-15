class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # The longest possible common prefix can't be longer than the shortest string
        # in the input array. So, we find the length of the shortest string first.
        max_len = min([len(word) for word in strs])

        commonPrifix = [] # This list will store the characters of our common prefix

        # Iterate through each character position up to the maximum possible prefix length.
        for i in range(max_len):
            # Take the character at the current position 'i' from the first string
            # as our reference to compare against other strings.
            letter = strs[0][i]

            # Now, iterate through each string in the input array.
            for word in strs:
                # If the character at position 'i' in the current 'word' does not
                # match our 'letter' reference, it means we've found a mismatch.
                # At this point, the common prefix ends, so we join the characters
                # collected so far and return the result.
                if word[i] != letter:
                    return ''.join(commonPrifix)

            # If all strings have the same 'letter' at the current position 'i',
            # it means this 'letter' is part of the common prefix. So, we add it
            # to our commonPrifix list.
            commonPrifix.append(letter)

        # If we successfully iterate through all character positions up to 'max_len'
        # without finding any mismatches, it means the common prefix is the
        # entire shortest string. We join the collected characters and return it.
        return ''.join(commonPrifix)


    # Time complexity = O(n * m) n: length of string array, m: length min string
    # space complexity = O(1)
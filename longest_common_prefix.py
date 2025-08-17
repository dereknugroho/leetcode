class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize output string
        output = ''

        # Loop through characters in first string
        for i, c1 in enumerate(strs[0]):
            # Loop through strings in strs argument
            for j, word in enumerate(strs):
                # If the reference word is longer than any other word in strs
                # or the letter at i in reference word is not equal to letter at i in word
                if i > len(word) - 1 or c1 != word[i]:
                    return output
                # If all words in strs have the same char at i
                if j == len(strs) - 1:
                    # Append char at i to output string
                    output += c1
        
        return output

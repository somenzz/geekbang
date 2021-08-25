class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        result = list(s)
        n = len(result)

        for left in range(0,n, 2*k):
            right = left + k
            self.reverse(result,left,min(right,n) - 1)


        return "".join(result)

    def reverse(self, array, begin, end):
        while begin < end:
            array[begin], array[end] = array[end], array[begin]
            begin += 1
            end -= 1


if __name__ == '__main__':
    solution = Solution()
    # assert "cbadefg" == solution.reverseStr("abcdefg", 3)
    assert "gfedcba" == solution.reverseStr("abcdefg", 8)
    # assert "bacd" == solution.reverseStr("abcd", 2)
    # assert "dcba" == solution.reverseStr("abcd", 4)
    # assert "dcbaefg" == solution.reverseStr("abcdefg", 4)
    assert "fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqllgsqddebemjanqcqnfkjmi" == solution.reverseStr(
        "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl",
        39)

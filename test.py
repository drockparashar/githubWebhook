# Read only region start
class UserMainCode(object):
    @classmethod
    def maximumSplits(cls, input1, input2):
        def find(v, pref, i, j):
            if i >= j:
                return 0
            sumtot = pref[j + 1] - pref[i]
            for k in range(i, j):
                currsum = pref[k + 1] - pref[i]
                if currsum * 2 == sumtot:
                    return 1 + max(find(v, pref, i, k), find(v, pref, k + 1, j))
            return 0

        # Prefix sum calculation
        n = input1
        v = input2
        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + v[i - 1]

        return find(v, pref, 0, n - 1)


def main():
    # Example 1 from the problem description
    input1 = 8
    input2 = [8, 0, 0, 0, 2, 2, 2, 2]
    
    result = UserMainCode.maximumSplits(input1, input2)
    print(f"Input1: {input1}")
    print(f"Input2: {input2}")
    print(f"Output: {result}")
    print(f"Expected: 3")
    print()
    
    # Test case with no donations
    input1_test2 = 4
    input2_test2 = [0, 0, 0, 0]
    result_test2 = UserMainCode.maximumSplits(input1_test2, input2_test2)
    print(f"Test case 2 - No donations:")
    print(f"Input1: {input1_test2}")
    print(f"Input2: {input2_test2}")
    print(f"Output: {result_test2}")
    print(f"Expected: 0")
    print()
    
    # Test case with odd total
    input1_test3 = 3
    input2_test3 = [1, 2, 4]
    result_test3 = UserMainCode.maximumSplits(input1_test3, input2_test3)
    print(f"Test case 3 - Odd total:")
    print(f"Input1: {input1_test3}")
    print(f"Input2: {input2_test3}")
    print(f"Output: {result_test3}")
    print(f"Expected: 0 (since 7 is odd)")

if __name__ == "__main__":
    main()
class Solution:
    def reversed_k(num: int, k: int) -> int:
        rev = 0
        while num > 0:
            rev *= k
            rev += num % k
            num = int(num / k)
        return rev

    def kmirrorsgen(k: int):
        # len = 1
        for i in range(1, k):
            yield i

        prefix_len = 1
        while True:
            # prefix + rev(prefix)  # len = prefix_len * 2
            for prefix in range(k ** (prefix_len - 1), k ** prefix_len):
                yield prefix * (k ** prefix_len) + Solution.reversed_k(prefix, k)

            # prefix + mid_char + rev(prefix)  # len = prefix_len * 2 + 1
            for prefix in range(k ** (prefix_len - 1), k ** prefix_len):
                reversed_k_prefix = Solution.reversed_k(prefix, k)
                for mid in range(0, k):
                    yield (prefix * k + mid) * (k ** prefix_len) + reversed_k_prefix

            prefix_len += 1


    def isKMirror(num: int, k: int) -> bool:
        rev = Solution.reversed_k(num, k)
        while num > 0:
            if num % k != rev % k:
                return False
            num = int(num / k)
            rev = int(rev / k)
        return True
        
            
    def kMirror(self, k: int, n: int) -> int:
        nums_sum = 0
        found_nums = 0
        for num in Solution.kmirrorsgen(k):
            if Solution.isKMirror(num, 10):
                nums_sum += num
                found_nums += 1
                if found_nums == n:
                    break
        return nums_sum
        

class Solution:
    def utf8ByteCount(firstByte: int) -> int:
        bits = [(firstByte >> i) & 1 for i in [7, 6, 5, 4, 3]]
        if bits[0] == 0:
            return 1
        if bits[1] == 1:
            if bits[2] == 0:
                return 2
            elif bits[3] == 0:
                return 3
            elif bits[4] == 0:
                return 4
        return -1

    def utf8IsNextByte(byte: int) -> bool:
        return (byte >> 7) & 1 == 1 and (byte >> 6) & 1 == 0

    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        l = len(data)
        while i < l:
            char_len = Solution.utf8ByteCount(data[i])
            if char_len == -1:
                return False
            for j in range(1, char_len):
                if i + j >= l or not Solution.utf8IsNextByte(data[i + j]):
                    return False
            i += char_len
        return True


        

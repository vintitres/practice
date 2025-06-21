class Solution:
    def utf8ByteCount(firstByte: int) -> int:
        firstByte >>= 3
        if firstByte == 0b11110:
            return 4
        firstByte >>= 1
        if firstByte == 0b1110:
            return 3
        firstByte >>= 1
        if firstByte == 0b110:
            return 2
        firstByte >>= 2
        if firstByte == 0b0:
            return 1
        return -1

    def utf8IsNextByte(byte: int) -> bool:
        return (byte >> 6) & 3 == 2

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


        

class Solution:
    def utf8ByteCount(firstByte: int) -> int:
        """
        firstByte = firstByte >> 3
        if firstByte == 0b11110:
            return 4
            """
        if firstByte & 0b10000000 == 0b00000000:
            return 1
        if firstByte & 0b11100000 == 0b11000000:
            return 2
        if firstByte & 0b11110000 == 0b11100000:
            return 3
        if firstByte & 0b11111000 == 0b11110000:
            return 4
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


        

#!/usr/bin/python3


def validUTF8(data):
    i = 0
    while i < len(data):
        num = data[i]
        if num < 128:  # ASCII character
            i += 1
        elif 128 <= num <= 191:  # Continuation byte
            return False
        else:  # Multi-byte sequence
            # Determine the number of bytes in the sequence based on the leading ones
            if num < 224:  # Two-byte sequence
                expected_bytes = 2
            elif num < 240:  # Three-byte sequence
                expected_bytes = 3
            elif num < 248:  # Four-byte sequence
                expected_bytes = 4
            else:
                return False
            
            # Check if the following bytes are continuation bytes
            for j in range(1, expected_bytes):
                i += 1
                if i >= len(data) or not (128 <= data[i] <= 191):
                    return False
        i += 1
    
    return True
import math

def fft(nums):
    if not power_of(len(nums)):
        raise ValueError("fft only accepts lists with a length equal to a power of two")

    if len(nums) == 1:
        return nums

    fft_left = fft(nums[::2])
    fft_right = fft(nums[1::2])

    out = [None]*len(nums)
    root = nth_root_of_unity(len(nums))
    
    for i in range(len(nums)//2):
        out[i] = fft_left[i] + (root**i)*fft_right[i]
        out[i+len(nums)//2] = fft_left[i] - (root**i)*fft_right[i]
    return out

def ifft(nums):
    if not power_of(len(nums)):
        raise ValueError("ifft only accepts lists with a length equal to a power of two")
    
    if len(nums) == 1:
        return nums

    fft_left = fft(nums[::2])
    fft_right = fft(nums[1::2])

    out = [None]*len(nums)
    root = -nth_root_of_unity(len(nums))
    
    for i in range(len(nums)//2):
        out[i] = fft_left[i] + (root**i)*fft_right[i]
        out[i+len(nums)//2] = fft_left[i] - (root**i)*fft_right[i]

    for i in range(len(out)):
        out[i] /= len(out)
        
    return out
    

def power_of(x, base=2):
    while not x%base:
        x //= base
    return x == 1

def nth_root_of_unity(n, field=complex):
    if field == complex:
        return math.e**(2*math.pi*1j / n)
    else:
        raise ValueError("Field not supported")

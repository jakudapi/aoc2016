'''--- Day 16: Dragon Checksum ---
--- Part Two ---

The second disk you have to fill has length 35651584. Again using the initial state in your puzzle input, what is the correct checksum for this disk?

Your puzzle input is still 10011111011011001.'''


DISK_LENGTH = 35651584
INPUT = "10011111011011001"


def data_filler(data):
    '''
    input-
    data:str, ie "10001110000"
    output- str
    '''
    b = data[::-1]
    b = b.replace('0','x').replace('1','0').replace('x','1')
    return data + "0" + b


def checksum(data):
    sum = ""
    for n in range(int(len(data)/2)):
        first = data[2*n]
        second = data[2*n+1]
        if first == second:
            sum += "1"
        else:
            sum += "0"
    if len(sum)%2 == 0:
        return checksum(sum)
    else:
        return sum


if __name__ == "__main__":
    while len(INPUT) < DISK_LENGTH:
        INPUT = data_filler(INPUT)
    print(INPUT)
    print(checksum(INPUT[:DISK_LENGTH]))
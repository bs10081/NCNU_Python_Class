def main():
    data = list()
    try:
        while True:
            data = data + list(map(float, input().split()))     #input number to list

    except EOFError:
        pass
    avg, stdev = statistic(data)    # Use data to run statistic
    print(avg, stdev)   

def statistic(data):
    # Set length
    length = len(data)

    # Average's Logic
    blob = 0  
    for i in data:
        blob = blob + i

    avg = (blob/length)

    # Standard deviation's Logic
    var = 0
    for i in data:
        var = var + (i - avg) ** 2
    stdev = (var / length) ** 0.5
    return avg, stdev


if __name__ == "__main__":
    main()
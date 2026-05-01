data = [2, 4, 7, 9, 11, 19, 23]

N = 19

start = 0
end = len(data) - 1
cnt = 1

while start <= end:
    mid = (start + end) // 2
    if data[mid] == N:
        print(f"{cnt}, 찾았다")
        break
    elif data[mid] > N:
        end = mid - 1
    else:
        start = mid + 1

    cnt += 1

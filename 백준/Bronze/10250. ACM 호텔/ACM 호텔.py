for _ in range(int(input())):
    h, w, n = map(int, input().split())
    # 호 수
    room_num = (n-1) // h + 1 
    # 층 수
    floor = (n-1) % h + 1

    print(f"{floor}{room_num:02d}")

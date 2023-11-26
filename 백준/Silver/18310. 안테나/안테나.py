N = int(input())                            # 집의 수 ex) 4
position = list(map(int, input().split()))  # 집의 위치 ex) 5 1 7 9

mid_index = (len(position) - 1) // 2        # 중간 인덱스 찾기
sorted_position = sorted(position)          # position 리스트를 정렬하여 중간값을 찾음
mid_value = sorted_position[mid_index]      # 정렬된 position 리스트에서 중간값 찾기

print(mid_value)  # 중간값 출력

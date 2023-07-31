

# 18046. 4828. min & max

# T = int(input())   #테스트 케이스 개수
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     ans = 0
#     max_v = arr[0]
#     min_v = arr[0]
#     for i in range(1, N):
#         if max_v < arr[i]:
#             max_v = arr[i]
#         if min_v > arr[i]:
#             min_v = arr[i]
#
#     ans = max_v - min_v
#
#     print(f'#{tc} {ans}')



# 1206. view

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    num = 0
    for i in range(2, N-2):
        my_list = [arr[i-2], arr[i-1], arr[i], arr[i+1], arr[i+2]]
        max_v = arr[i]
        print(max_v)
        for j in my_list:
            if not j > max_v:
                my_list2 = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]
                max_v2 = 0
                for k in my_list2:
                    if k > max_v2:
                        max_v2 = k

                    else:
                        continue

                num += arr[i] - max_v2
            else:
                break

    print(f'#{tc} {num}')

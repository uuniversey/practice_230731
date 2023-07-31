# '''
# 9
# 7 4 2 0 0 6 0 7 0
# '''
#
# N = int(input())
# arr = list(map(int,input().split()))
#
# print(N)
# print(arr)



# # 버블 정렬
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     for i in range(N-1, 0, -1):     # i 구간의 마지막 인덱스
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
#     print(f'#{tc}', *arr)
my_list = [3,5,7,9]
for j in my_list:
    print (j)
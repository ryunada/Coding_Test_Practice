# Time Limit
# class Solution:
#     def max_counter(self, l):
#         max_cnt = 0
#         most_value = None
#         for i in set(l):
#             cnt = l.count(i)
#             if cnt > max_cnt:
#                 max_cnt = cnt
#                 most_value = i
#         return most_value, max_cnt
    
#     def minimumIndex(self, nums: List[int]) -> int:
#         most_value, max_cnt = self.max_counter(nums)
#         positions = [i for i, x in enumerate(nums) if x == most_value] # most_value 위치 인덱스

#         if max_cnt * 2 > len(nums):
#             for p in positions:
#                 if p == len(nums) -1: # 마지막 인덱스인 경우 제외
#                     continue

#                 left_max_cnt = nums[ : p + 1].count(most_value)
#                 right_max_cnt = nums[p + 1 : ].count(most_value)

#                 if (left_max_cnt * 2 > len(nums[:p+1])) and (right_max_cnt * 2 > len(nums[p+1:])):
#                     return p 
#             return -1
#         else:
#             return -1

from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # 전체 리스트에서 dominant element를 찾기
        counter = Counter(nums)
        most_value, max_cnt = counter.most_common(1)[0]

        # 조건을 만족하는 dominant element인지 확인
        if max_cnt * 2 <= len(nums):
            return -1
        
        # 왼쪽과 오른쪽의 카운트를 저장할 변수
        left_count = 0
        total_count = max_cnt
        
        # 왼쪽에서부터 탐색
        for i, num in enumerate(nums):
            if num == most_value:
                left_count += 1
            
            # 오른쪽의 카운트는 전체에서 왼쪽을 뺀 값
            right_count = total_count - left_count
            
            # dominant element 조건 체크
            if (left_count * 2 > (i + 1)) and (right_count * 2 > (len(nums) - i - 1)):
                return i  # 유효한 인덱스를 찾음
        
        return -1  # 유효한 인덱스를 찾지 못한 경우

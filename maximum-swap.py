class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = [int(x) for x in str(num)]
        max_index = len(num_list) - 1
        swap_from = len(num_list) - 1
        swap_to = len(num_list) - 1
        for i in range(len(num_list) - 1, -1, -1):
            if num_list[i] > num_list[max_index]:
                max_index = i
            elif num_list[i] < num_list[max_index]:
                swap_from = i
                swap_to = max_index
        num_list[swap_from], num_list[swap_to] = num_list[swap_to], num_list[swap_from]
        return int(''.join(list(map(str, num_list))))
        

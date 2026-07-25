class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted_numbers = {} ## [[num], [frecuency]]

        for number in nums:
            if number in counted_numbers:
                count = counted_numbers[number]
                count += 1
                counted_numbers[number] = count
            else:
                counted_numbers[number] = 1

        sorted_dict = dict(sorted(counted_numbers.items(), key=lambda item: item[1], reverse = True))
        output_list = []
        sorted_dict_keys = list(sorted_dict.keys())

        for i in range(0, k):
            output_list.append(sorted_dict_keys[i])

        return output_list

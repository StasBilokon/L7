#2 Sum_of _two
def sum_of_two(nums: list, target: int) -> list:
    dictionari_1 = {}
    for i in range(len(nums)):
        if target - nums[i] in dictionari_1:
            return [dictionari_1[target - nums[i]],i]
        else:
            dictionari_1[nums[i]] = i
                
result_2 = sum_of_two(nums=[3,2,4], target=6)
print(result_2)



# 2 test
def test_sum_of_two():
        result1 = sum_of_two([2,7,11,15], 9)
        assert result1 == [0, 1]

        result2 = sum_of_two([3,2,4], 6)
        assert result2 == [1, 2]

        result3 = sum_of_two(3, 3, 6)
        assert result3 == [0, 1]
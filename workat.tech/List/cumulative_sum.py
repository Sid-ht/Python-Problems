class Solution:
	def getCumulativeSum(self, arr: List[int]) -> List[int]:
		# add your logic here
		new_list = []
		cumulative_sum = 0
		for i in range(0,len(arr)):
			new_list.append((arr[i] + cumulative_sum))
			cumulative_sum += arr[i]
		return new_list

class Solution:
	def getSquareSortedArray(self, arr: List[int]) -> List[int]:
		# add your logic here
		arr = list(map(lambda x: x**2,arr))
		arr.sort()
		return arr

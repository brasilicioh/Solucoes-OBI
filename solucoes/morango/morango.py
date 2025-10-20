from sys import stdin as inp, stdout as out

nums = [int(inp.readline()) for _ in range(4)]

out.write(str(max(nums[0]*nums[1], nums[2]*nums[3])))
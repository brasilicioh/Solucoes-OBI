qtd = int(input())
nums = list(map(int, input().split()))

left = 0
right = qtd - 1

contracoes = 0

while left < right:
    if nums[left] == nums[right]:
        left += 1
        right -= 1
    elif nums[left] < nums[right]:
        nums[left + 1] += nums[left]
        left += 1
        contracoes += 1
    elif nums[left] > nums[right]:
        nums[right - 1] += nums[right]
        right -= 1
        contracoes += 1
    
print(contracoes)
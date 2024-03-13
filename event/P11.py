#

uinp = input("")
nums = uinp.split()

res = []

for num in nums:
    if nums[0] < nums[1]:
        res.append(nums[1])

    if nums[2] < nums[1]:
        pass  # not going

    if nums[3] > nums[1]:
        res.append(nums[3])

    if nums[2] > nums[1]:
        res.append(nums[2])

    if nums[3] < nums[2]:
        continue

    if nums[3] > nums[2]:
        res.append(nums[3])

    if nums[4] < nums[3]:
        continue

    if nums[4] > nums[3]:
        res.append(nums[4])

    if nums[5] < nums[4]:
        continue

    if nums[5] > nums[4]:
        res.append(nums[5])

    if nums[6] < nums[5]:
        continue

    if nums[6] > nums[5]:
        res.append(nums[6])

    if nums[7] < nums[6]:
        continue

    if nums[7] > nums[6]:
        res.append(nums[7])

print(res)
print(nums[0] + " " + "".join(res))

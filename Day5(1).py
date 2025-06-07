#using lamda function (use only for quick calculations not recommended for multiple outputs)
nums = [4, 8, 12, 16]
get_avg = lambda x: sum(x)/len(x)
print("Average:", get_avg(nums))



nums = [4, 8, 12, 16]
get_total = lambda x: sum(x)
print("total:", get_total(nums))

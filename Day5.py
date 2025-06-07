#Using Built-in sum() and len()
def calculate_sum_avg(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

nums = [5, 10, 25, 50]
total, avg = calculate_sum_avg(nums)
print(f"Sum = {total}, Average = {avg}")


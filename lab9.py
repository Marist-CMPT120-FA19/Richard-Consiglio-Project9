def main():
    temp = int(input("Enter a number to find the prime numbers below it"))
    nums = list(range (2, temp+1))
    
    while len(nums) > 0:
        prime = nums.pop(0)
        print(prime, "is a prime number")
        for i in nums:
            if i % prime == 0:
                nums.remove(i)
            
main()


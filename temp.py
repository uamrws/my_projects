from threading import RLock

r_lock = RLock()


def temp(nums):
    nums[0] += 1
    with r_lock:
        if nums[0] < 10:
            temp(nums)


if __name__ == '__main__':
    a = [0]
    temp(a)
    print(a)

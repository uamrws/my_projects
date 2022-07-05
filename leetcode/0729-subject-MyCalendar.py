"""
实现一个 MyCalendar 类来存放你的日程安排。如果要添加的日程安排不会造成 重复预订 ，则可以存储这个新的日程安排。

当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生 重复预订 。

日程可以用一对整数 start 和 end 表示，这里的时间是半开区间，即 [start, end), 实数x 的范围为， start <= x < end 。

实现 MyCalendar 类：

MyCalendar() 初始化日历对象。
boolean book(int start, int end) 如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 true 。否则，返回 false并且不要将该日程安排添加到日历中。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/my-calendar-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import bisect
from typing import List


class MyCalendar:

    def __init__(self):
        self.book_list: List[List[int]] = []

    def book(self, start: int, end: int) -> bool:
        bl = [start, end]
        if not self.book_list:
            self.book_list.append(bl)
            return True
        idx = bisect.bisect(self.book_list, bl)
        if (
                (idx == 0 or self.book_list[idx - 1][1] <= start)
                and (idx >= len(self.book_list) or self.book_list[idx][0] >= end)
        ):
            self.book_list.insert(idx, bl)
            return True
        return False


# 这个回答比较牛
class MyCalendar:
    def __init__(self):
        self.slot = []

    def book(self, start: int, end: int) -> bool:
        i = bisect.bisect_right(self.slot, start)
        if i & 1 or (i < len(self.slot) and self.slot[i] < end):
            return False
        self.slot[i:i] = [start, end]
        return True


if __name__ == '__main__':
    m = MyCalendar()
    print(m.book(47, 50))
    # print(m.book(33, 41))
    print(m.book(51, 59))

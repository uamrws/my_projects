"""
给定一个表示分数加减运算的字符串expression，你需要返回一个字符串形式的计算结果。

这个结果应该是不可约分的分数，即最简分数。如果最终结果是一个整数，例如2，你需要将它转换成分数形式，其分母为1。所以在上述例子中, 2应该被转换为2/1。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/fraction-addition-and-subtraction
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import operator

State = {
    "init": ["up", "", "", "up"],
    "up": ["", "", "sep", "up"],
    "sep": ["", "", "", "down"],
    "down": ["init", "init", "", "down"]
}
Symbol = {
    "-": 0,
    "+": 1,
    "/": 2,
}
Operate = {
    "-": operator.sub,
    "+": operator.add,
}


class Solution:
    state = 0

    def gcd(self, a, b):

        while b != 0:
            if a < b:
                a, b = b, a
            a, b = b, a % b
        return a

    def fractionAddition(self, expression: str) -> str:
        pre_up = 0
        pre_down = 1
        state = "init"
        cur_up = ""
        cur_down = ""
        op = "+"
        for i in expression:
            state = State[state][Symbol.get(i, 3)]
            if state == "up":
                cur_up += i
            if state == "down":
                cur_down += i
            if state == "init":
                cd = int(cur_down)
                cp = int(cur_up)
                pre_up = Operate[op](pre_up * cd, cp * pre_down)
                pre_down *= cd

                op = i
                cur_up = ""
                cur_down = ""
        cd = int(cur_down)
        cp = int(cur_up)
        pre_up = Operate[op](pre_up * cd, cp * pre_down)
        pre_down *= cd
        if pre_up == 0:
            ans = "0/1"
        else:
            d = self.gcd(abs(pre_up), abs(pre_down))
            ans = f"{int(pre_up / d)}/{int(pre_down / d)}"
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.fractionAddition("-1/2+1/2"))
    print(s.fractionAddition("-1/2+1/2+1/3"))
    print(s.fractionAddition("1/3-1/2"))

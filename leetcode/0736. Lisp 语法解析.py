"""
给你一个类似 Lisp 语句的字符串表达式 expression，求出其计算结果。

表达式语法如下所示:

表达式可以为整数，let 表达式，add 表达式，mult 表达式，或赋值的变量。表达式的结果总是一个整数。
(整数可以是正整数、负整数、0)
let 表达式采用"(let v1 e1 v2 e2 ... vn en expr)" 的形式，其中let 总是以字符串"let"来表示，接下来会跟随一对或多对交替的变量和表达式，也就是说，第一个变量v1被分配为表达式e1的值，第二个变量v2被分配为表达式e2的值，依次类推；最终 let 表达式的值为expr表达式的值。
add 表达式表示为"(add e1 e2)" ，其中add 总是以字符串"add" 来表示，该表达式总是包含两个表达式 e1、e2 ，最终结果是e1 表达式的值与e2表达式的值之 和 。
mult 表达式表示为"(mult e1 e2)"，其中mult 总是以字符串 "mult" 表示，该表达式总是包含两个表达式 e1、e2，最终结果是e1 表达式的值与e2表达式的值之 积 。
在该题目中，变量名以小写字符开始，之后跟随 0 个或多个小写字符或数字。为了方便，"add" ，"let" ，"mult" 会被定义为 "关键字" ，不会用作变量名。
最后，要说一下作用域的概念。计算变量名所对应的表达式时，在计算上下文中，首先检查最内层作用域（按括号计），然后按顺序依次检查外部作用域。测试用例中每一个表达式都是合法的。有关作用域的更多详细信息，请参阅示例。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/parse-lisp-expression
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import ChainMap


class Solution:
    global_map = ChainMap()

    def evaluate(self, expression: str) -> int:
        stack = []
        action = None
        local = {"stack": stack, "action": action}
        self.global_map = self.global_map.new_child(local)
        idx = 0
        n = len(expression)
        while idx < n:
            if action == "let" and len(stack) >= 2:
                val = stack.pop(1)
                if isinstance(val, int):
                    self.global_map[stack.pop(0)] = val
                else:
                    self.global_map[stack.pop(0)] = self.global_map[val]

            expr = expression[idx]
            if expr not in [" "]:
                if expr == "(":
                    m = 1
                    for i in range(idx + 1, n):
                        if expression[i] == "(":
                            m += 1
                        elif expression[i] == ")":
                            m -= 1
                        if m == 0:
                            expr = expression[idx + 1:i + 1]
                            idx += 1
                            break
                    stack.append(self.evaluate(expr))
                elif expr == ")":
                    break
                else:
                    for i in range(idx + 1, n):
                        if expression[i] in [" ", ")"]:
                            expr = expression[idx:i]
                            break
                    if expr in ["let", "add", "mult"]:
                        local["action"] = action = expr
                    else:
                        try:
                            val = int(expr)
                        except ValueError:
                            val = expr
                        stack.append(val)
            idx += len(expr)
        ans = 0

        if action == "add":
            for i in stack:
                if isinstance(i, int):
                    ans += i
                else:
                    ans += self.global_map[i]
        elif action == "mult":
            ans += 1
            for i in stack:
                if isinstance(i, int):
                    ans *= i
                else:
                    ans *= self.global_map[i]
        else:
            ans = stack[-1]
            if not isinstance(ans, int):
                ans = self.global_map[ans]
        self.global_map = self.global_map.parents
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))"))
    print(s.evaluate("(let x 1 y 2 x (add x y) (add x y))"))
    print(s.evaluate("(let x 3 x 2 x)"))
    print(s.evaluate("(add 1 2)"))

"""
TinyURL 是一种 URL 简化服务， 比如：当你输入一个 URLhttps://leetcode.com/problems/design-tinyurl时，它将返回一个简化的URLhttp://tinyurl.com/4e9iAk 。请你设计一个类来加密与解密 TinyURL 。

加密和解密算法如何设计和运作是没有限制的，你只需要保证一个 URL 可以被加密成一个 TinyURL ，并且这个 TinyURL 可以用解密方法恢复成原本的 URL 。

实现 Solution 类：

Solution() 初始化 TinyURL 系统对象。
String encode(String longUrl) 返回 longUrl 对应的 TinyURL 。
String decode(String shortUrl) 返回 shortUrl 原本的 URL 。题目数据保证给定的 shortUrl 是由同一个系统对象加密的。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/encode-and-decode-tinyurl
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Codec:
    seed = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    UrlDict = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = str(len(self.UrlDict))
        self.UrlDict[key] = longUrl
        return key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.UrlDict[shortUrl]


if __name__ == '__main__':
    # Your Codec object will be instantiated and called as such:
    url = "https://leetcode.com/problems/design-tinyurl"
    codec = Codec()
    codec.decode(codec.encode(url))
    import math

    print(math.factorial(62))

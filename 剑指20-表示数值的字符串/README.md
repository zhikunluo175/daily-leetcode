# 题目
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

# 思路
用了一个比较鸡贼的做法，python的float()，强制转换类型为float。再结合异常处理，不能转的返回False，否则返回True，就可以轻松解决此题。

# -*- codeing:utf-8 -*-
import difflib
import time

def levenshtein_dp(s: str, t: str) -> int:
    """
    计算莱文斯坦距离（Levenshtein distance），距离越小，说明两个单词越相近，时间复杂度为 O(mxn)
    :param s:
    :param t:
    :return:
    """
    m, n = len(s), len(t)
    table = [[0] * (n + 1) for _ in range(m + 1)]
    table[0] = [j for j in range(n + 1)]
    # print(table)
    for i in range(m + 1):
        table[i][0] = i
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            table[i][j] = min(
                1 + table[i - 1][j],
                1 + table[i][j - 1],
                int(s[i - 1] != t[j - 1]) + table[i - 1][j - 1],
            )
    return table[-1][-1]

def difflib_leven(str1, str2):
    '''
    使用difflib计算莱温斯坦距离
    '''
    leven_cost = 0
    s = difflib.SequenceMatcher(None, str1, str2)
    for tag, i1, i2, j1, j2 in s.get_opcodes():
        # print('{:7} a[{}: {}] --> b[{}: {}] {} --> {}'.format(tag, i1, i2, j1, j2, str1[i1: i2], str2[j1: j2]))
        if tag == "replace":
            leven_cost += max(i2 - i1, j2 - j1)
        elif tag == "insert":
            leven_cost += j2 - j1
        elif tag == "delete":
            leven_cost += i2 - i1
    return leven_cost


def common_substring_dp(s: str, t: str) -> int:
    m, n = len(s), len(t)
    table = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            table[i][j] = max(
                table[i - 1][j],
                table[i][j - 1],
                int(s[i - 1] == t[j - 1]) + table[i - 1][j - 1],
            )
    return table[-1][-1]


def get_right_word_from_leven(methods_name,all_words, input_word):
    """
      输入一个单词，返回计算莱文斯坦距离最小的单词
      :param input_word:
      :return:
      """
    words = all_words  # 获取所有正确的单词
    right_word = input_word
    min_distance = 99999
    for item in words:
        distance = methods_name(input_word, item)
        if distance == 0:
            return item
        elif min_distance > distance:
            min_distance = distance
            right_word = item
    return right_word


def get_right_word_from_common_substring(all_words, input_word):
    """
    输入一个单词，返回最长公共子串长度最大的单词
    :param input_word:
    :return:
    """
    words = all_words  # 获取所有正确的单词
    right_word = input_word
    len_origin = len(input_word)
    max_len = 0
    for item in words:
        length = common_substring_dp(input_word, item)
        if length >= len_origin:
            return item
        if max_len < length:
            max_len = length
            right_word = item
    return right_word


if __name__ == "__main__":
    all_words = []
    with open("dict.txt", encoding="utf-8", mode="r") as r:
        for line in r:
            word = line.strip().split(" ")[0]
            if word != "" and len(word) > 2:
                all_words.append(word)
    print(f"词典共有词语 {len(all_words)} 个")
    while True:
        input_word = input("请输入词语，q 退出：")
        if input_word == "q":
            break

        start = time.time()
        right_word = get_right_word_from_leven(difflib_leven, all_words, input_word)
        print("最小编辑距离的结果: ", right_word)
        print(f"编辑距离为：{difflib_leven(input_word,right_word)}")
        end = time.time()
        print(f"耗时 {round(end - start,4)} 秒")

        start = time.time()
        right_word = get_right_word_from_common_substring(all_words, input_word)
        print("最大公共子序列的结果：", right_word)
        print(f"最大公共子序列的长度：{common_substring_dp(input_word,right_word)}")
        end = time.time()
        print(f"耗时 {round(end - start,4)} 秒")
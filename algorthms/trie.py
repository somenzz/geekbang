# encoding = utf-8

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end = -1

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

        curNode = self.root
        for c in word:
            if not c in curNode:
                curNode[c] = {}
            curNode = curNode[c]
        curNode[self.end] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curNode = self.root
        for c in word:
            if not c in curNode:
                return False
            curNode = curNode[c]

        # Doesn't end here
        if not self.end in curNode:
            return False

        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curNode = self.root
        for c in prefix:
            if not c in curNode:
                return False
            curNode = curNode[c]

        return True

    def get_start(self,prefix):
        '''
        给出一个前辍，打印出所有匹配的字符串
        :param prefix:
        :return:
        '''
        def get_key(pre,pre_node):
            result = []
            if pre_node.get(self.end):
                result.append(pre)
            for key in pre_node.keys():
                if key != self.end:
                    result.extend(get_key(pre+key,pre_node.get(key)))
            return result


        if not self.startsWith(prefix):
            return []
        else:
            node = self.root
            for p in prefix:
                node = node.get(p)
            else:
                return get_key(prefix,node)
    @staticmethod
    def levenshtein_dp(s: str, t: str) -> int:
        '''
        计算莱文斯坦距离（Levenshtein distance），距离越小，说明两个单词越相近
        :param s:
        :param t:
        :return:
        '''
        m, n = len(s), len(t)
        table = [[0] * (n + 1) for _ in range(m + 1)]
        table[0] = [j for j in range(n + 1)]
        # print(table)
        for i in range(m + 1):
            table[i][0] = i
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                table[i][j] = min(1 + table[i - 1][j], 1 + table[i][j - 1],
                                  int(s[i - 1] != t[j - 1]) + table[i - 1][j - 1])
        for t in table:
            print(t)
        return table[-1][-1]

    def get_all_words_of_trie(self):
        words = []
        for k in self.root.keys():
            words.extend(self.get_start(k))
        return words

    def get_right_word(self,input_word):
        '''
        输入一个单词，返回正确的单词
        :param input_word:
        :return:
        '''
        words = self.get_all_words_of_trie()
        right_word = input_word
        min_distance = 99999
        for item in words:
            distance = self.levenshtein_dp(input_word,item)
            if min_distance >  distance:
                min_distance = distance
                right_word = item
        return right_word










if __name__ == "__main__":
    trie = Trie()
    trie.insert("中")
    trie.insert("中国")
    trie.insert("中国人")
    trie.insert("中华人民共和国")
    # print(trie.root)
    trie.insert("Python")
    trie.insert("Python 算法")
    trie.insert("Python web")
    trie.insert("Python web 开发")
    trie.insert("Python web 开发 视频教程")
    trie.insert("Python 算法 源码")
    trie.insert("Perl 算法 源码")
    # print(trie.search("Perl"))
    # print(trie.search("Perl 算法 源码"))
    # print((trie.get_start('P')))
    # print((trie.get_start('Python web')))
    # print((trie.get_start('Python 算')))
    # print(trie.get_all_words_of_trie())

    print(trie.levenshtein_dp("facbok","facebook"))
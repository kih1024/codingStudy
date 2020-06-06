# https://blog.ilkyu.kr/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-Trie-%ED%8A%B8%EB%9D%BC%EC%9D%B4-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
# https://m.post.naver.com/viewer/postView.nhn?volumeNo=26828891&memberNo=33264526
from collections import defaultdict


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.length = defaultdict(int)


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        curr_node.length[len(string)] += 1
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node.children[char].length[len(string)] += 1
            curr_node = curr_node.children[char]

        curr_node.data = string

    def search(self, prefix, length):
        curr_node = self.head

        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return 0

        return curr_node.length[length]


def solution(words, queries):
    global count
    answer = []
    trie_list = Trie()
    trie_listR = Trie()

    for word in words:
        trie_list.insert(word)
        trie_listR.insert(word[::-1])

    for q in queries:
        if q == "?" * len(q):
            answer.append(trie_list.head.length[len(q)])
        elif q[0] != "?":
            prefix = q.split("?")[0]
            answer.append(trie_list.search(prefix, len(q)))
        else:
            prefix = q[::-1].split("?")[0]
            answer.append(trie_listR.search(prefix, len(q)))
    print(answer)
    return answer


solution(
    ["frodo", "front", "frost", "frozen", "frame", "kakao"],
    ["fro??", "????o", "fr???", "fro???", "pro?"],
)

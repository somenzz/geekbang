## 数据结构与算法之美


#### 06 | 链表（上）：如何实现LRU缓存淘汰算法?

用双向链表 + Hash 表来实现 LRU 缓存淘汰策略

代码实现 [lru_use_link_table](./lru_use_link_table.py)

用 OrderedDict 表来实现 LRU 缓存淘汰策略

代码实现 [lru_use_ordered_dict](./lru_use_ordered_dict.py)


思考题：如果字符串是通过单链表来存储的，那该如何来判断是一个回文串呢？

```java
class Solution {
  public boolean isPalindrome(ListNode head) {
    if (head == null || head.next == null) {
      return true;
    }

    ListNode prev = null;
    ListNode slow = head;
    ListNode fast = head;

    while (fast != null && fast.next != null) {
      fast = fast.next.next;
      ListNode next = slow.next;
      slow.next = prev;
      prev = slow;
      slow = next;
    }

    if (fast != null) {
      slow = slow.next;
    }

    while (slow != null) {
      if (slow.val != prev.val) {
        return false;
      }
      slow = slow.next;
      prev = prev.next;
    }

    return true;
  }
}
```
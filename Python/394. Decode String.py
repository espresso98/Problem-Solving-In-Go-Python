# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
# O(n), O(n)
class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        cur_num = cur_str = ''
        
        for ch in s:
            if ch.isdigit():
                cur_num += ch
            elif ch == '[':
                st.append(cur_str)
                st.append(int(cur_num))
                cur_num = cur_str = ''
            elif ch.isalpha():
                cur_str += ch
            elif ch == ']':
                k = st.pop()
                prev_str = st.pop()  # ['', 3] ['aaa', 2]
                cur_str = prev_str + cur_str * k  # '' + 'a' * 3,  'aaa' + 'bc' * 2

        return cur_str
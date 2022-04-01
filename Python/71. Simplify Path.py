# Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, 
# convert it to the simplified canonical path.
# TC:O(N)/ SC:O(N)
        
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        names = path.split('/')
        
        for i in names:
            if i in ['', '.']:
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)  
        can_path = '/' + '/'.join(stack)
        return can_path
    
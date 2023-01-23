# BFS. TC: O(N*l), SC: O(N*l) where N is the number of urls and l is the length of url
# We can model the problem with a directed graph where each URL is a vertex/node, and links between them are edges.
# The problem is asking us to traverse the graph visiting only URLs with the same hostname as the one of the start URL.
import collections
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        def get_hostname(url):
            hostname = url.split('/')[2] 
            # ['http:', '', 'news.yahoo.com', 'news', 'topics', '']
            return hostname

        start_hostname = get_hostname(startUrl)
        queue = collections.deque([startUrl])
        visited = set([startUrl])
        while queue:
            url = queue.popleft()
            for nextUrl in htmlParser.getUrls(url):
                if get_hostname(nextUrl) == start_hostname and nextUrl not in visited:
                    queue.append(nextUrl)
                    visited.add(nextUrl)
                    
        return list(visited)

# print(queue)
# deque(['http://news.yahoo.com/news/topics/']) <- startUrl
# deque(['http://news.yahoo.com', 'http://news.yahoo.com/news'])
# deque(['http://news.yahoo.com/news', 'http://news.yahoo.com/us'])
# deque(['http://news.yahoo.com/us'])

# print(url, htmlParser.getUrls(url))
# http://news.yahoo.com/news/topics/ ['http://news.yahoo.com', 'http://news.yahoo.com/news']
# http://news.yahoo.com  ['http://news.yahoo.com/us']

# http://news.google.com  ['http://news.yahoo.com/news/topics/', 'http://news.yahoo.com/news', 'http://news.yahoo.com']

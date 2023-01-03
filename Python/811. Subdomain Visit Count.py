# O(N), O(N)
from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_cnt = defaultdict(int)
        for pair in cpdomains:
            cnt, domain = pair.split()
            cnt = int(cnt)

            subdomain = domain.split('.') 
            sub = ''
            for i in range(len(subdomain)):
                sub = '.'.join(subdomain[i:])
                domain_cnt[sub] += cnt
            
        return [f'{cnt} {sub}' for sub, cnt in domain_cnt.items()]

// Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.
// TC: O(n) / SC: O(n)

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:      
        result = set()    
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            result.add(local + '@' + domain)
        return len(result)
        
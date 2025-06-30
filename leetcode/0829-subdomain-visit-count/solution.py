class Solution:
    def subdomains(domain: str):
        yield domain
        next_dot = 0
        while True:
            print(next_dot, domain)
            next_dot = domain.find('.', next_dot)
            if next_dot == -1:
                break
            next_dot += 1
            yield domain[next_dot:]


    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits = defaultdict(int)
        for cpdomain in cpdomains:
            cpdomain = cpdomain.split(' ')
            count = int(cpdomain[0])
            domain = cpdomain[1]
        
            for subdomain in Solution.subdomains(domain):
                visits[subdomain] += count
        
        res = []
        for domain, count in visits.items():
            res.append(f"{count} {domain}")
        
        return res
            
        

# TLE
class Solution:
    def is_valid_integer(self, s):
        if len(s) == 0 or len(s) > 3:
            return False
        if len(s) > 1 and s[0] == '0':
            return False
        str_int = int(s)
        if str_int > 255:
            return False
        return True
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        cache = defaultdict(list)
        all_possible_ip_addresses = []
        self._restore_ip_addresses(s, all_possible_ip_addresses, cache)
        ip_addresses = filter(lambda x: len(x.split('.')) == 4,cache[s])
        return set(ip_addresses)
    
    def _restore_ip_addresses(self, s, all_possible_ip_addresses, cache):
        if not s:
            return ['']
        if s in cache:
            return cache[s]
        for i in range(3, -1, -1):
            prefix = s[:i]
            if self.is_valid_integer(prefix):
                for digit in self._restore_ip_addresses(s[i:], all_possible_ip_addresses, cache):
                    ip_string = prefix + '.' + digit if digit is not '' else prefix
                    all_possible_ip_addresses.append(ip_string)
                    cache[s].append(ip_string)
        return cache[s]

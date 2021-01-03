class Solution:
    def defang_IP_addr(self, address):
        defanged_address = ''

        for letter in address:
            if letter == '.':
                defanged_address += '[.]'
            else:
                defanged_address += letter

        return defanged_address

# Test cases

sol = Solution()

address1 = '1.1.1.1'
expected1 = '1[.]1[.]1[.]1'

address2 = '255.100.50.0'
expected2 = '255[.]100[.]50[.]0'

print(f'Input:    \'{address1}\'')
print(f'Output:   \'{sol.defang_IP_addr(address1)}\'')
print(f'Expected: \'{expected1}\'')
print('---')

print(f'Input:    \'{address2}\'')
print(f'Output:   \'{sol.defang_IP_addr(address2)}\'')
print(f'Expected: \'{expected2}\'')

class Solution:
    def defang_IP_addr(self, address):
        defanged_address = ''

        for letter in address:
            if letter == '.':
                defanged_address += '[.]'
            else:
                defanged_address += letter

        return defanged_address

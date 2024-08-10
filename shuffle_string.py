class Solution:
    def restore_string(self, s, indices):
        new_string = ''
        new_string_index = 0
        old_string_length = len(s)

        while new_string_index < old_string_length:
            for index, value in enumerate(indices):
                if new_string_index == value:
                    new_string += s[index]
                    new_string_index += 1

        return new_string

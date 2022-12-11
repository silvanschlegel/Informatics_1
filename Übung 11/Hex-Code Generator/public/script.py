#!/usr/bin/env python3

class GameRunner(object):

    def __init__(self):
        self.rows = 17
        self.columns = 2

    def generate_hex_codes(self):
        from random import choice
        options = "0123456789ABCDEF"
        hexcodes = []
        for i in range(self.columns*self.rows):
            code = "0x"
            for j in range(4):
                code += choice(options)
            hexcodes.append(code)
        '''different approach with List comprehension: 
        return ["0x" + "".join([choice("0123456789ABCDEF") for j in range(4)]) for i in range(self.columns * self.rows)]'''
        return hexcodes

a = GameRunner()
a.generate_hex_codes()
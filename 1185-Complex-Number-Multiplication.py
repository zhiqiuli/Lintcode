class Solution:
    """
    @param a: a string
    @param b: a string
    @return: a string representing their multiplication
    """
    def complex_number_multiply(self, a: str, b: str) -> str:
        a_real, a_img = self.str2complex(a)
        b_real, b_img = self.str2complex(b)

        c_real = a_real*b_real - a_img*b_img
        c_img  = a_real*b_img  + b_real*a_img

        return str(c_real) + '+' + str(c_img) + 'i'

    def str2complex(self, str):
        a1, a2 = str.split('+')
        str_real = int(a1)
        str_img  = int(a2[:-1])
        return str_real, str_img
        

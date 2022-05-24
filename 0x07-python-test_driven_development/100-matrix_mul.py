#!/usr/bin/python3
"""asd asd asd"""


def matrix_mul(m_a, m_b):
        """asd asd asd"""

        if m_a == [[]] or len(m_a) == 0 or len(m_a[0]) == 0:
                raise ValueError("m_a can't be empty")

        if m_b == [[]] or len(m_b) == 0 or len(m_b[0]) == 0:
                raise ValueError("m_b can't be empty")

        if type(m_a) is not list or type(m_a[0]) is not list:
                raise TypeError("m_a must be a list")

        if type(m_b) is not list or type(m_b[0]) is not list:
                raise TypeError("m_b must be a list")

        for x in m_a:
                if type(x) is not list:
                        raise TypeError("m_a must be a list")

                error_msg = "each x of m_a must be of the same size"
                if len(x) != len(m_a[0]):
                        raise TypeError(error_msg)

                error_msg = "m_a should contain only integers or floats"
                for n in x:
                        if type(n) is not float and type(n) is not int:
                                raise TypeError(error_msg)

        if len(m_a[0]) != len(m_b):
                raise ValueError("m_a and m_b can't be multiplied")

        for x in m_b:
                if type(x) is not list:
                        raise TypeError("m_b must be a list")

                error_msg = "each x of m_b must be of the same size"
                if len(x) != len(m_b[0]):
                        raise TypeError(error_msg)

        for n in x:
            if type(n) is not float and type(n) is not int:
                raise TypeError("m_b should contain only integers or floats")

        nl = []
        mtrx = []
        res = 0
        for x_ma in range(len(m_a)):
                nl = []
                for y_mb in range(len(m_b[0])):
                        for i in range(len(m_a[0])):
                                res += m_a[x_ma][i] * m_b[i][y_mb]
                        nl.append(res)
                        res = 0
                mtrx.append(nl)

        return mtrx

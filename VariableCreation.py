#!/usr/bin/python

''' Rules for creating Variables in python '''
# a-z, A-Z, A-Za-z,_,0-9,Cannot create variable name with numeric values as a prefix.

#Notice different combinations of both left and right operands.

FirstName = 'Sahas'
MIDDLENAME = "Van"
lastname = '''test_lname'''
Cap200="""y"""
_python_version = '3.7.1'

print(FirstName + MIDDLENAME + lastname + Cap200 + _python_version)
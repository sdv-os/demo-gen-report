import sys,os,time
from junit_xml import TestSuite, TestCase

test_cases = [TestCase('Test1', 'some.class.name', 123.345, 'I am stdout!', 'I am stderr!')]
ts = TestSuite("my test suite", test_cases)

with open('results.xml', 'w') as f:
    TestSuite.to_file(f, [ts], prettyprint=False)

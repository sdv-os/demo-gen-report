import sys,os,time
from junit_xml import TestSuite, TestCase

test_cases = [TestCase('Test1', 'some.class.name', 123.345, 'I am stdout!', 'I am stderr!')]

for item in range(10):
    tc_tmp = TestCase('TC%d' % item , 'some.class.name', 123.345 + item , 'I am stdout!', 'I am stderr!')
    if item % 2 == 0:
        tc_tmp.add_error_info(message="Skipped error", output="I skippäd with an error!")
        
    test_cases.append(tc_tmp)
    
ts = TestSuite("my test suite", test_cases)

with open('results.xml', 'w') as f:
    TestSuite.to_file(f, [ts], prettyprint=False)

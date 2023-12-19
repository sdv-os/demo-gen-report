import junit_xml_output

test_cases = []

for item in range(50):
    if item % 3 == 0:
        test_cases.append(junit_xml_output.TestCase("TC%d_failures" % item, "ASW Signal handler. DEMO:%d" % item,"failure"))
    else:
        test_cases.append(junit_xml_output.TestCase("TC%d_success" % item, "TEST CASE %d SUCCESS." % item,"success"))
junit_xml = junit_xml_output.JunitXml("example_usage", test_cases)
xml_cont = junit_xml.dump()
xml_cnt_lst = xml_cont.split('\n')
xml_dump = xml_cnt_lst[0] + "<testsuites>" + ''.join(xml_cnt_lst[1:]) + "</testsuites>"

fp = open("results.xml","w")
fp.write(xml_dump)
fp.close()

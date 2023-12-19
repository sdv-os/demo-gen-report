import junit_xml_output

test_cases = []

for item in range(50):
    if item % 3 == 0:
        test_cases.append(junit_xml_output.TestCase("TC%d" % item, "ASW Signal handler. DEMO:%d" % item,"failure"))
    else:
        test_cases.append(junit_xml_output.TestCase("TC%d" % item, "TEST CASE %d SUCCESS." % item,"pass"))
junit_xml = junit_xml_output.JunitXml("example_usage", test_cases)
#print (junit_xml.dump())
fp = open("results.xml","w")
fp.write(junit_xml.dump()+'\n')
fp.close()

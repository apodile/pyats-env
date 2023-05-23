from pyats.aetest import Testcase, test
from genie.testbed import load

Class ShowVersionTestcase(Testcase):
    @test
    def fetch_show_version(self):
        testbed = load('yaml/my_testbed.yaml')
        device = testbed.devices['SW01']
        device.connect()
        output = device.execute('show ip int brief')
        print(output)
        device.disconnect()
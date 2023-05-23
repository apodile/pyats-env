from genie.testbed import load
tb = load ('yaml/my_testbed.yaml')
dev = tb.devices['SW01']
dev.connect()
p1 = dev.parse('show ip int brief')
print(p1)

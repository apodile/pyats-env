from pyats.topology import loader
from genie.libs.ops.bgp.ios.bgp import Bgp
# Load testbed file
testbed = loader.load('yaml/my_testbed.yaml')
device = testbed.devices['SW01']
# Connect to the device
device.connect()
# Create a BGP object and learn BGP state
bgp = Bgp(device=device)
bgp.learn()
print("BGP Info:", bgp.info) # Debug print
# Access the default VRF BGP neighbors
bgp_vrf = bgp.info.get('instance', {}).get('default', {}).get('vrf', {}).get('default', {})
print("BGP VRF Data:", bgp_vrf) # Debug print
bgp_neighbors = bgp_vrf.get('neighbor', {})
print("BGP Neighbors:", bgp_neighbors) # Debug print
# Perform validation tests
for neighbor, neighbor_data in bgp_neighbors.items():
    print(f"Checking BGP neighbor: {neighbor}")
    print(f"Neighbor data: {neighbor_data}") # Debug print
# Test: BGP session state should be "established"
    is_established = neighbor_data['session_state'] == 'Established'
    print(f" BGP session established: {is_established}")
    assert is_established, f"BGP session not established for neighbor {neighbor}"
# Test: Check if 'session_uptime' key is present and the value is greater than 60
    if 'session_uptime' in neighbor_data and neighbor_data['session_uptime'] > 60:
        print(f" BGP session uptime greater than 60 seconds: True")
    else:
        print(f" BGP session uptime greater than 60 seconds: False")
# Handle the case when session uptime is less than 60 seconds
# Add your desired behavior or raise an exception if required
print(f" All tests passed for neighbor {neighbor}\n")
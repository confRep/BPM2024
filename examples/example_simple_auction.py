import os
from pnml_to_webppl.converter import convert_dpn_to_webPPL

# Initialize Path from examples data
path_pnml = os.path.abspath('../examples/data/simple_auction.pnml')

# Convert DPN to WebPPL
webPPL_file = convert_dpn_to_webPPL(path_pnml, verbose=False, simulation_steps=100, sample_size=50000)


# save as webPPL file in outpur folder
with open('simple_auction.wppl', 'w') as f:
    f.write(webPPL_file)

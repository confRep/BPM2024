# PNML to WebPPL
This tool provides an efficient way to convert Petri Net Markup Language (PNML) files into WebPPL (Probabilistic Programming Language) scripts. It aims to facilitate the analysis and simulation of data-aware petri nets defined in PNML through the powerful inference capabilities of WebPPL.


## Installation
To use the PNML to WebPPL Converter, ensure that you have Python 3.x installed on your system. Follow these steps to set up the converter:

1. Clone the repository to your local machine using the following command or by downloading the repository as a zip file and extracting it to a local directory:
```bash
git clone <repository-anonymized>
```

2. Navigate to the root directory of the repository: 
```bash
cd <repository-name>
```

3. Install the required dependencies using the following command:
```bash
pip install -r requirements.txt
```




## Usage
To convert a PNML file to a WebPPL script, follow the example provided below. This example assumes you have a valid PNML file located in the 'examples/data/' directory. New PNML Files can be added to the 'examples/data/' directory.
As an example to test the converter, you can run Python file in 'examples/example_simple_auction.py'. the content of the file is shown below. 
```python
import os
from pnml_to_webppl.converter import convert_dpn_to_webPPL

# Initialize Path for the PNML file
path_pnml = os.path.abspath('examples/data/simple_auction.pnml')

# Convert DPN to WebPPL
webPPL_file = convert_dpn_to_webPPL(path_pnml, verbose=False, simulation_steps=10)

print(webPPL_file)

# Save the WebPPL code to a file in the output folder
with open('simple_auction.wppl', 'w') as f:
    f.write(webPPL_file)
```
After execution a file named 'simple_auction.wppl' will be created in the directory. The content of the file will be the WebPPL script generated from the PNML file and can be pasted into the console of http://webppl.org to test it.


## Contributing
Due to the double-blind review process, we are unable to list specific contributing guidelines, authors, or the project's status. 

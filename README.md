# ssdtm 

This is a collection of synthetic CDISC SDTM data generators using sequence generators. 

The low-fidelity synethic SDTM data would be very valuable in multiple usecases.

1. Allow non-production teams within biopharma companies, CROs, and health technology companies to build the systems without access the sensitive data.
2. Provide low-fidelity data to default study database for testing purpose.
3. Test and validate the data pipelines before First-Patient-In within a study.
4. Overall assist with faster study startup time.


* Free software: MIT license


## Tutorial
--------


### How to install

```sh
$ pip install ssdtm
```

### Basic Usage

```sh
import ssdtm as sd

	
# Get synthetic data generated through random sequence generators
ae = sd.get_adverse_events(5)


# Save non-serious adverse events to excel file in local directory
lb = sd.get_lab_analytes(8,4)


# This generates and returns CDISC SDTM data for 7 domains
# The first param is number of patients and the second one specifies number of visits

data = sd.get_sdtm_data(8,4)

data['cm']
data['dm']
data['vs']

# This generates and saves the SDTM data for 7 common domains in the local directory
# The first param is number of patients and the second one specifies number of visits
sd.save_sdtm_data(8,4)

```

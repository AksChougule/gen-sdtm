"""
This is a list of function which can generate synthetic, low-fidelity CDISC SDTM Data
for individual domains or for all at once.
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta


def generate_dates(start_date, num_days, num_dates):
    dates = [start_date + timedelta(days=random.randint(0, num_days)) for _ in range(num_dates)]
    return dates


def get_demographics(num_patients):
	"""
	Create a fake CDISC SDTM dataset for demographics.

	Parameters:
	num_patients (int): The number of patients.

	Returns:
	pd.DataFrame: A dataframe with demographics data.
	"""
	# Constants for the dataset
	sexes = ['Male', 'Female']
	races = ['Asian', 'Black', 'White', 'Hispanic', 'Other']
	ethnicities = ['Hispanic or Latino', 'Not Hispanic or Latino']

	# Generating data
	data = {
    	'AGE': [random.randint(18, 100) for _ in range(num_patients)],
    	'SEX': [random.choice(sexes) for _ in range(num_patients)],
    	'RACE': [random.choice(races) for _ in range(num_patients)],
    	'ETHNIC': [random.choice(ethnicities) for _ in range(num_patients)],
    	'VISITDT': [(datetime.now() - timedelta(days=random.randint(0, 365))).date() for _ in range(num_patients)],
    	'PATID': [f'P{str(i).zfill(5)}' for i in range(1, num_patients + 1)]
	}

	# Creating DataFrame
	DM = pd.DataFrame(data)

	return DM


def get_conmed(num_patients):
	"""
	Create a fake CDISC SDTM dataset for concomitant medication.

	Parameters:
	num_patients (int): The number of patients.

	Returns:
	pd.DataFrame: A dataframe with concomitant medication data.
	"""
	# Constants for the dataset
	medications = ['Aspirin', 'Metformin', 'Lisinopril', 'Simvastatin', 'Amlodipine']
	dose_units = ['mg', 'g']
	freqs = ['Once daily', 'Twice daily', 'Three times daily']

	# Generating data
	data = {
                'PATID': [f'P{str(i).zfill(5)}' for i in range(1, num_patients + 1)],
                'CMTRT': [random.choice(medications) for _ in range(num_patients)],
    	        'CMDOSFRQ': [random.choice(freqs) for _ in range(num_patients)],
                'CMDOSU': [random.choice(dose_units) for _ in range(num_patients)],
    	        'CMSTDTC': [(datetime.now() - timedelta(days=random.randint(0, 365))).date() for _ in range(num_patients)],
    	        'CMENDTC': [(datetime.now() - timedelta(days=random.randint(0, 30))).date() for _ in range(num_patients)]
	}

	# Creating DataFrame
	CM = pd.DataFrame(data)

	return CM



def get_vital_signs(num_patients, num_visits):
    """
    Create a fake CDISC SDTM dataset for vital signs.

    Parameters:
    num_patients (int): The number of patients.
    num_visits (int): The number of visits per patient.

    Returns:
    pd.DataFrame: A dataframe with vital signs data.
    """
    # Constants for the dataset
    vital_signs = ['Heart Rate', 'Blood Pressure', 'Respiratory Rate', 'Temperature']

    # Generating data
    data = {'PATID': [], 'VSTESTCD': [], 'VSORRES': [], 'VSSTDTC': [], 'VISIT': []}

    for i in range(1, num_patients + 1):
        pat_id = f'P{str(i).zfill(5)}'
        for visit_num in range(1, num_visits + 1):
            visit_name = f'Visit {visit_num}'
            for signs in vital_signs:
                data['PATID'].append(pat_id)
                data['VSTESTCD'].append(signs)
                data['VSORRES'].append(random.randint(60,100)) # Random value for vital sign
                data['VSSTDTC'].append((datetime.now() - timedelta(days=random.randint(0,365))).date())  
                data['VISIT'].append(visit_name)

    # Creating DataFrame
    LB = pd.DataFrame(data)

    return LB



def get_exposure(num_patients):
	"""
	Create a fake CDISC SDTM dataset for exposure.

	Parameters:
	num_patients (int): The number of patients.

	Returns:
	pd.DataFrame: A dataframe with exposure data.
	"""
	# Constants for the dataset
	treatments = ['Treatment A', 'Placebo']
	dose_units = ['mg', 'ml']

	# Generating data
	data = {
    	    'PATID': [f'P{str(i).zfill(5)}' for i in range(1, num_patients + 1)],
    	    'EXTRT': [random.choice(treatments) for _ in range(num_patients)],
    	    'EXDOSE': [random.randint(10, 100) for _ in range(num_patients)],
    	    'EXDOSU': [random.choice(dose_units) for _ in range(num_patients)],
    	    'EXSTDTC': [(datetime.now() - timedelta(days=random.randint(0, 365))).date() for _ in range(num_patients)],
    	    'EXENDTC': [(datetime.now() - timedelta(days=random.randint(0, 30))).date() for _ in range(num_patients)]
	}

	# Creating DataFrame
	EX = pd.DataFrame(data)

	return EX




def get_lab_analytes(num_patients, num_visits):
    """
    Create a fake CDISC SDTM dataset for lab analytes.

    Parameters:
    num_patients (int): The number of patients.
    num_visits_per_patient (int): The number of visits per patient.

    Returns:
    pd.DataFrame: A dataframe with lab analytes data.
    """
    # Constants for the dataset
    analytes = ['Hemoglobin', 'Cholesterol', 'Glucose', 'Calcium', 'Potassium']
    units = ['g/dL', 'mg/dL', 'mg/dL', 'mg/dL', 'mmol/L']

    # Generating data
    data = {'PATID': [], 'LBTEST': [], 'LBSTRESU': [], 'LBSTRESN': [], 'LBORRES': [], 'VISITNUM': [], 'VISIT': []}

    for i in range(1, num_patients + 1):
            pat_id = f'P{str(i).zfill(5)}'
            for visit_num in range(1, num_visits + 1):
                for analyte, unit in zip(analytes, units):
                    data['PATID'].append(pat_id)
                    data['LBTEST'].append(analyte)
                    data['LBSTRESU'].append(unit)
                    data['LBSTRESN'].append(random.uniform(0, 10))  # Random numeric result
                    data['LBORRES'].append(f'{random.uniform(0, 10):.2f}')  # Random result in string format
                    data['VISITNUM'].append(visit_num)
                    data['VISIT'].append(f'Visit {visit_num}')
    # Creating DataFrame
                    
    LB = pd.DataFrame(data)

    return LB



def get_adverse_events(num_patients):
    """
    Create an extended fake CDISC SDTM dataset for adverse events.

    Parameters:
    num_patients (int): The number of patients.

    Returns:
    pd.DataFrame: A dataframe with extended adverse events data.
    """
    # Constants for the dataset
    adverse_events = ['Headache', 'Nausea', 'Dizziness', 'Fatigue', 'Rash', 'Fever']
    severity_levels = ['Mild', 'Moderate', 'Severe']
    toxicity_grades = ['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4']
    outcomes = ['Recovered', 'Improving', 'Unchanged', 'Worsened', 'Death']
    actions = ['Dose not changed', 'Dose reduced', 'Drug withdrawn']
    serious = ['Y', 'N']
    aesdth = ['Y', 'N']

    # Generating data
    data = {
        'PATID': [], 'AETERM': [], 'AESEV': [], 'AESTDTC': [], 'AEENDTC': [], 
        'AETOXGR': [], 'AEOUT': [], 'AEACT': [], 'AESER': [], 'AESDTH': []
    }

    for i in range(1, num_patients + 1):
        pat_id = f'P{str(i).zfill(5)}'
        # Random number of adverse events for each patient between 2 and 6
        num_events = np.random.randint(2, 7)
        for _ in range(num_events):
            data['PATID'].append(pat_id)
            data['AETERM'].append(np.random.choice(adverse_events))
            data['AESEV'].append(np.random.choice(severity_levels))
            start_date = datetime.now() - timedelta(days=np.random.randint(1, 365))
            data['AESTDTC'].append(start_date.date())
            end_date = start_date + timedelta(days=np.random.randint(1, 30))
            data['AEENDTC'].append(end_date.date())
            data['AETOXGR'].append(np.random.choice(toxicity_grades))
            data['AEOUT'].append(np.random.choice(outcomes))
            data['AEACT'].append(np.random.choice(actions))
            data['AESER'].append(np.random.choice(serious))
            data['AESDTH'].append(np.random.choice(aesdth))

    # Creating DataFrame
    AE = pd.DataFrame(data)

    return AE

#region RS - Response data

def get_response(num_patients):
    """
    Create a fake CDISC SDTM dataset for response to treatment.

    Parameters:
    num_patients (int): The number of patients.

    Returns:
    pd.DataFrame: A dataframe with response data.
    """
    # Constants for the dataset
    responses = ['Complete Response', 'Partial Response', 'Stable Disease', 'Progressive Disease']
    visit_nums = [1, 2, 3, 4, 5]

    # Generating data
    data = {'PATID': [], 'VISITNUM': [], 'RESPONSE': []}

    for i in range(1, num_patients + 1):
        pat_id = f'P{str(i).zfill(5)}'
        for visit_num in visit_nums:
            data['PATID'].append(pat_id)
            data['VISITNUM'].append(visit_num)
            data['RESPONSE'].append(random.choice(responses))

    # Creating DataFrame
    RS = pd.DataFrame(data)

    return RS


#endregion

def get_response(num_patients):
    """
    Create a fake CDISC SDTM dataset for response to treatment.

    Parameters:
    num_patients (int): The number of patients.

    Returns:
    pd.DataFrame: A dataframe with response data.
    """
    rs_data = []
    for i in range(1, num_patients + 1):
        patient_id = f"P{i:05d}"
        for visit in range(1, 6):  # Assuming 5 visits per patient
            date = generate_dates(datetime(2023, 1, 1), 365, 1)[0]
            rs_data.append({
                "USUBJID": patient_id,
                "RSSEQ": visit,
                "RSDTC": date.strftime("%Y-%m-%d"),
                "RSDY": (date - datetime(2023, 1, 1)).days,
                "RSORRES": random.choice(["CR", "PR", "SD", "PD"]),
                "RSSTRESC": random.choice(["Complete Response", "Partial Response", "Stable Disease", "Progressive Disease"]),
            })
    return pd.DataFrame(rs_data)

def get_tumor_identification(num_patients):
    tu_data = []
    for i in range(1, num_patients + 1):
        patient_id = f"P{i:05d}"
        num_tumors = random.randint(1, 5)  # Each patient can have 1 to 5 tumors
        for tumor in range(1, num_tumors + 1):
            tu_data.append({
                "USUBJID": patient_id,
                "TUSEQ": tumor,
                "TULOC": random.choice(["Lung", "Liver", "Brain", "Bone"]),
                "TUMETHOD": random.choice(["CT Scan", "MRI", "Ultrasound"]),
            })
    return pd.DataFrame(tu_data)

def get_tumor_results(num_patients):
    tr_data = []
    for i in range(1, num_patients + 1):
        patient_id = f"P{i:05d}"
        num_tumors = random.randint(1, 5)  # Each patient can have 1 to 5 tumors
        for tumor in range(1, num_tumors + 1):
            for visit in range(1, 6):  # Assuming 5 visits per patient
                date = generate_dates(datetime(2023, 1, 1), 365, 1)[0]
                tr_data.append({
                    "USUBJID": patient_id,
                    "TRSEQ": visit,
                    "TRDTC": date.strftime("%Y-%m-%d"),
                    "TRDY": (date - datetime(2023, 1, 1)).days,
                    "TRLINKID": f"TUMOR{tumor:03d}",
                    "TRORRES": random.uniform(0.5, 10.0),  # Tumor size in cm
                    "TRSTRESC": random.uniform(0.5, 10.0),  # Tumor size in cm (standardized)
                })
    return pd.DataFrame(tr_data)

def generate_sdtm_data(num_patients):
    rs_df = get_response(num_patients)
    tu_df = get_tumor_identification(num_patients)
    tr_df = get_tumor_results(num_patients)
    
    rs_df.to_csv("RS.csv", index=False)
    tu_df.to_csv("TU.csv", index=False)
    tr_df.to_csv("TR.csv", index=False)
    
    print("SDTM data files generated: RS.csv, TU.csv, TR.csv")

# Specify the number of patients
num_patients = 100
generate_sdtm_data(num_patients)



def save_sdtm_data(num_patients, num_visits=5, therapeutic_area=None):
    """
    Create and save low-fidelity synthetic CDISC SDTM dataset for 9 common domains.

    Parameters:
    num_patients (int): The number of patients.
    num_rows (int): The number of visits per patient
    therapeutic_area (text): Disease Segment (e.g. therapeutic_area = 'oncology')

    Returns:
    NA
    """
    # create adverse events
    ae = get_adverse_events(num_patients)
    ae.to_csv("ae.csv")

    # create concomitant medication
    cm = get_conmed(num_patients)
    cm.to_csv("cm.csv")

    # create demographics
    dm = get_demographics(num_patients)
    dm.to_csv("dm.csv")

    # create exposure data
    ex = get_exposure(num_patients)
    ex.to_csv("ex.csv")

    # create lab analytes
    lb = get_lab_analytes(num_patients, num_visits)
    lb.to_csv("lb.csv")

    # create vital signs
    vs = get_vital_signs(num_patients, num_visits)
    vs.to_csv("vs.csv")

    if therapeutic_area=='oncology':
        rs_df = get_response(num_patients)
        tu_df = get_tumor_identification(num_patients)
        tr_df = get_tumor_results(num_patients)
        
        rs_df.to_csv("rs.csv", index=False)
        tu_df.to_csv("tu.csv", index=False)
        tr_df.to_csv("tr.csv", index=False)


def get_sdtm_data(num_patients, num_visits=5, therapeutic_area=None):
    """
    Create a fake CDISC SDTM dataset for 9 common domains.

    Parameters:
    num_patients (int): The number of patients.
    num_rows (int): The number of visits per patient
    therapeutic_area (text): Disease Segment (e.g. therapeutic_area = 'oncology')
   
    Returns:
    Dictionary of pandas df, each df is associated with a domain
    """
    # create adverse events
    ae = get_adverse_events(num_patients)

    # create concomitant medication
    cm = get_conmed(num_patients)

    # create demographics
    dm = get_demographics(num_patients)

    # create exposure data
    ex = get_exposure(num_patients)

    # create lab analytes
    lb = get_lab_analytes(num_patients, num_visits)

    # create vital signs
    vs = get_vital_signs(num_patients, num_visits)

    if therapeutic_area=='oncology':
        rs = get_response(num_patients)
        tu = get_tumor_identification(num_patients)
        tr = get_tumor_results(num_patients)
    
        data = {'ae':ae,'cm':cm,'dm':dm,'ex':ex,'lb':lb,'vs':vs,'rs':rs,'tu':tu,'tr':tr}
        return data
    
    if therapeutic_area==None:
        data = {'ae':ae,'cm':cm,'dm':dm,'ex':ex,'lb':lb,'vs':vs}
        return data

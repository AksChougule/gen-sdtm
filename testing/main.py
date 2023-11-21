import pandas as pd
import sdtm_generators as gs

def create_sdtm_data(num_patients, num_visits=5):
    
    # create adverse events
    ae = gs.create_sdtm_adverse_events(num_patients)
    ae.to_csv("ae.csv")
    
    # create concomitant medication
    cm = gs.create_sdtm_conmed(num_patients)
    cm.to_csv("cm.csv")

    # create demographics
    dm = gs.create_sdtm_demographics(num_patients)
    dm.to_csv("dm.csv")

    # create exposure data
    ex = gs.create_sdtm_exposure(num_patients)
    ex.to_csv("ex.csv")

    # create lab analytes
    lb = gs.create_sdtm_lab_analytes(num_patients, num_visits)
    lb.to_csv("lb.csv")
    
    # create vital signs
    vs = gs.create_sdtm_vital_signs(num_patients, num_visits)
    vs.to_csv("vs.csv")

    # create response data
    rs = gs.create_sdtm_response(num_patients)
    rs.to_csv("rs.csv")

create_sdtm_data(6,4)

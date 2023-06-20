def get_nok(nok):
    return {
         "NOK_NAME": {
             "FIRST_NAME": nok.full_name,
             "MIDDLE_NAME": "",
             "LAST_NAME": ""
         },
        "RELATIONSHIP": nok.relationship,
        "ADDRESS": nok.address,
        "PHONE_NUMBER": str(nok.phone_number),
        "SEX": "",
        "DATE_OF_BIRTH": "",
        "CONTACT_ROLE": ""
    }


def get_patient_payload(patient):
    payload = {
        "MESSAGE_HEADER": {
            "SENDING_APPLICATION": "KENYAEMR",
            "SENDING_FACILITY": "12438",
            "RECEIVING_APPLICATION": "IL",
            "RECEIVING_FACILITY": "12438",
            "MESSAGE_DATETIME": "20230412082230",
            "SECURITY": "",
            "MESSAGE_TYPE": "ADT^A04",
            "PROCESSING_ID": "P"
        },
        "PATIENT_IDENTIFICATION": {
            "EXTERNAL_PATIENT_ID": {
                "ID": "",
                "IDENTIFIER_TYPE": "GODS_NUMBER",
                "ASSIGNING_AUTHORITY": "MPI"
            },
            "INTERNAL_PATIENT_ID": [
                {
                    "ID": patient.patient_number,
                    "IDENTIFIER_TYPE": "CCC_NUMBER",
                    "ASSIGNING_AUTHORITY": "CCC"
                }
            ],
            "PATIENT_NAME": {
                "FIRST_NAME": patient.first_name,
                "MIDDLE_NAME": patient.last_name,
                "LAST_NAME": "TEST"
            },
            "MOTHER_NAME": {
                "FIRST_NAME": "",
                "MIDDLE_NAME": "",
                "LAST_NAME": ""
            },
            "DATE_OF_BIRTH": patient.date_of_birth.timestamp(),
            "SEX": "M" if patient.gender == 'male' else 'F',
            "PATIENT_ADDRESS": {
                "PHYSICAL_ADDRESS": {
                    "VILLAGE": "TEST",
                    "WARD": "",
                    "SUB_COUNTY": "ISUKHA WEST",
                    "COUNTY": "KAKAMEGA",
                    "GPS_LOCATION": "",
                    "NEAREST_LANDMARK": ""
                },
                "POSTAL_ADDRESS": patient.address
            },
            "PHONE_NUMBER": str(patient.phone_number),
            "MARITAL_STATUS": patient.marital_status.status,
            "DEATH_DATE": "",
            "DEATH_INDICATOR": "",
            "DATE_OF_BIRTH_PRECISION": "ESTIMATED"
        },
        "NEXT_OF_KIN": [get_nok(nok) for nok in patient.next_of_keen.all()],
        "PATIENT_VISIT": {
            "VISIT_DATE": "20230412",
            "PATIENT_SOURCE": "VCT",
            "HIV_CARE_ENROLLMENT_DATE": "20230412",
            "PATIENT_TYPE": "ART"
        },
        "OBSERVATION_RESULT": [
            {
                "UNITS": "",
                "VALUE_TYPE": "NM",
                "OBSERVATION_VALUE": "1",
                "OBSERVATION_DATETIME": "20230412",
                "CODING_SYSTEM": "",
                "ABNORMAL_FLAGS": "N",
                "OBSERVATION_RESULT_STATUS": "F",
                "SET_ID": "",
                "OBSERVATION_IDENTIFIER": "WHO_STAGE"
            }
        ]
    }
    return payload
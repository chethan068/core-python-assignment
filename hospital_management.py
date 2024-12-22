def search_patients_by_disease(patients, disease):
    """
    Search for patients with a specific disease and return their names.
    """
    result = [patient["Name"] for patient in patients if patient["Disease"].lower() == disease.lower()]
    return result

def main():
    
    patients = [
        {"Name": "Alice", "Age": 30, "Disease": "Flu"},
        {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
        {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
    ]
    
  
    search_disease = "Flu"
    
    
    patients_with_disease = search_patients_by_disease(patients, search_disease)
   
    print(f"Patients with {search_disease}: {patients_with_disease}")


main()

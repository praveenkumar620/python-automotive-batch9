import xml.etree.ElementTree as ET

def get_medical_issues():
    tree = ET.parse("disease.xml")
    root = tree.getroot()

    issues = []

    # Extract medical issues
    for patient in root.findall("patient"):
        issue = patient.find("issue").text
        issues.append(issue)

    # Sort alphabetically
    issues.sort()
    return issues


# Run only when file is executed directly
if __name__ == "__main__":
    result = get_medical_issues()
    print("Medical Issues in Alphabetical Order:")
    for issue in result:
        print(issue)

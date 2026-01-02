from disease import get_medical_issues

def test_medical_issues_sorted():
    result = get_medical_issues()

    # Expected output (alphabetical order)
    expected = ["Allergy", "Asthma", "Diabetes", "Hypertension","Fever"]

    assert result == expected

import Lab2.BMI as cat # Import the Lab2.BMI module

def test_bmi_normal_weight():
    result = []
    height = 1.57 #input parameter for testing
    weight = 57 #actual result for testing
    test = 0

    result = cat.BMI(height, weight)

    assert (result == test) 
    
def test_bmi_over_weight():
    result = []
    height = 1.57 #input parameter for testing
    weight = 90 #actual result for testing
    test = 1

    result = cat.BMI(height, weight)

    assert (result == test)


def test_bmi_under_weight():
    result = []
    height = 1.57 #input parameter for testing
    weight = 15 #actual result for testing
    test = -1

    result = cat.BMI(height, weight)

    assert (result == test)
    
    

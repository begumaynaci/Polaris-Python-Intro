from password_control import control_pass

def test_strongPass():
    assert control_pass("Begum123.") == True

def test_missingNumberPass():
    assert control_pass("Beg.") == False

def test_missingSymbolPass():
    assert control_pass("Begum12") == False

def test_missingUppercasePass():
    assert control_pass("begum12.") == False

    

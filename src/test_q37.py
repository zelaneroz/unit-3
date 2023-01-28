import pytest
from q37 import AccountingProgram

def test_empty_account():
    ac=AccountingProgram()
    assert ac.principal==0
    assert ac.rate==0
    assert ac.years==0

def test_set_values():
    ac=AccountingProgram()
    assert ac.set_rate(3)=="Rate set to 3"
    assert ac.set_years(2)=="Number of years set to 2"
    assert ac.set_principal(5)=="Principal value set to 5"
    assert ac.calculate_interest()=="Calculated interest is 80"

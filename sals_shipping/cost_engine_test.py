# Tests
import pytest
from cost_engine import *

def test_ground_shipping_breakpoints():
    assert g_s_cost(1) == 21.5
    assert g_s_cost(3) == 29
    assert g_s_cost(7) == 48
    assert g_s_cost(12) == 77
    assert g_s_cost(8.4)==53.60
   

def test_drone_shipping_breakpoints():
    assert d_s_cost(1) == 4.5
    assert d_s_cost(3) == 27
    assert d_s_cost(7) == 84
    assert d_s_cost(12) == 171
    assert d_s_cost(1.5) == 6.75


    
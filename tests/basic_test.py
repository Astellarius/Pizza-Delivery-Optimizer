import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pizza_delivery.test1 import mycode


def test_answer():
    assert mycode.principle_fire == 9999
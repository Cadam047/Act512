import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from smells1 import calculate_total_price


def test_calculate_total_price_empty():
    assert calculate_total_price([]) == 0


def test_calculate_total_price_unknown_item():
    assert calculate_total_price(["kiwi"]) == 0


def test_calculate_total_price_no_discount():
    assert calculate_total_price(["apple", "banana", "cherry"]) == 2.25


def test_calculate_total_price_with_discount():
    assert calculate_total_price(["apple"] * 10) == 9

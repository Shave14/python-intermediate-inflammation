"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

import inflammation.models as im
#from inflammation.models import daily_mean


"""
# Writing the tests individually
def test_daily_max_equal():
    "Test that max function works when inputs are equal.""
    "
    
    test_input = np.array([[1,4],
                           [1,4],
                           [1,4]
                          ])
    test_result = np.array([1,4])
    
    npt.assert_array_equal(im.daily_max(test_input), test_result)

def test_daily_max_variable():
    ""
    "Test that max function works when inputs are equal."
    ""
    
    test_input = np.array([[1,6],
                           [2,5],
                           [3,4]
                          ])
    test_result = np.array([3,6])
    
    npt.assert_array_equal(im.daily_max(test_input), test_result)
    
    
def test_daily_min_equal():
    ""
    "Test that max function works when inputs are equal."
    ""
    
    test_input = np.array([[1,4],
                           [1,4],
                           [1,4]
                          ])
    test_result = np.array([1,4])
    
    npt.assert_array_equal(im.daily_min(test_input), test_result)
    
    
def test_daily_min_variable():
    ""
    "Test that max function works when inputs are equal."
    ""
    
    test_input = np.array([[1,6],
                           [2,5],
                           [3,4]
                          ])
    test_result = np.array([1,4])
    
    npt.assert_array_equal(im.daily_min(test_input), test_result)
    
    
def test_daily_min_bad_equal():
    ""
    "Test that max function works when inputs are equal."
    ""
    
    test_input = np.array([[1,4],
                           [1,4],
                           [1,4]
                          ])
    test_result = np.array([1,4])
        
    npt.assert_array_equal(im.daily_max(test_input), test_result)
        
## Could have tested negative numbers

def test_daily_min_string():
    ""
    "Test for TypeError when passing strings"
    ""

    with pytest.raises(TypeError): 
        # with is a context manager, which creates an isolated context. Often 
        # used to read files, because it automatically closes the file once read
        error_expected = im.daily_min([['Hello', 'there'], ['General', 'Kenobi']])
        
"""


@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    npt.assert_array_equal(im.daily_mean(np.array(test)), np.array(expected))
    
@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [1, 4], [1, 4], [1, 4] ], [1, 4]),
        ([ [1, 6], [2, 5], [3, 4] ], [3, 6]),
        ([ [1, 1], [-1, -1], [1, -1]], [1,1])
    ])
def test_daily_max(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    npt.assert_array_equal(im.daily_max(np.array(test)), np.array(expected))
    
@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [1, 4], [1, 4], [1, 4] ], [1, 4]),
        ([ [1, 6], [2, 5], [3, 4] ], [1, 4]),
        ([ [1, 1], [-1, -1], [1, -1]], [-1,-1])
    ])
def test_daily_min(test, expected):
    """Test min function works for array of zeroes and positive integers."""
    npt.assert_array_equal(im.daily_min(np.array(test)), np.array(expected))
    
def test_daily_min_string():
    ""
    "Test for TypeError when passing strings"
    ""

    with pytest.raises(TypeError): 
        # with is a context manager, which creates an isolated context. Often 
        # used to read files, because it automatically closes the file once read
        error_expected = im.daily_min([['Hello', 'there'], ['General', 'Kenobi']])
        

####example to parameterise functions

@pytest.mark.parametrize(
    "func, test, expected",
    [
     (im.daily_mean, [ [0, 0], [0, 0], [0, 0] ], [0, 0])
     ])
def test_daily_stats(func, test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    npt.assert_array_equal(func(np.array(test)), np.array(expected))


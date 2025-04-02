"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

import inflammation.models as im
#from inflammation.models import daily_mean

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(im.daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(im.daily_mean(test_input), test_result)

def test_daily_max_equal():
    """Test that max function works when inputs are equal."""
    
    test_input = np.array([[1,4],
                           [1,4],
                           [1,4]
                          ])
    test_result = np.array([1,4])
    
    npt.assert_array_equal(im.daily_max(test_input), test_result)

def test_daily_max_variable():
    """Test that max function works when inputs are equal."""
    
    test_input = np.array([[1,6],
                           [2,5],
                           [3,4]
                          ])
    test_result = np.array([3,6])
    
    npt.assert_array_equal(im.daily_max(test_input), test_result)
    
    
def test_daily_min_equal():
    """Test that max function works when inputs are equal."""
    
    test_input = np.array([[1,4],
                           [1,4],
                           [1,4]
                          ])
    test_result = np.array([1,4])
    
    npt.assert_array_equal(im.daily_min(test_input), test_result)
    
    
def test_daily_min_variable():
    """Test that max function works when inputs are equal."""
    
    test_input = np.array([[1,6],
                           [2,5],
                           [3,4]
                          ])
    test_result = np.array([1,4])
    
    npt.assert_array_equal(im.daily_min(test_input), test_result)
    
    
def test_daily_min_bad_equal():
    """Test that max function works when inputs are equal."""
    
    test_input = np.array([[1,4],
                           [1,4],
                           [1,4]
                          ])
    test_result = np.array([1,4])
        
    npt.assert_array_equal(im.daily_max(test_input), test_result)
        
## Could have tested negative numbers

def test_daily_min_string():
    """Test for TypeError when passing strings"""

    with pytest.raises(TypeError): 
        # with is a context manager, which creates an isolated context. Often 
        # used to read files, because it automatically closes the file once read
        error_expected = im.daily_min([['Hello', 'there'], ['General', 'Kenobi']])
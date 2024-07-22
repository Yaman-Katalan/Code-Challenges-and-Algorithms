# Write your test here
import pytest
from challenge02 import first_repeated_word  # Replace with your actual module name

def test_first_repeated_word_example1():
    input_str = "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    expected_output = "ASAC"
    assert first_repeated_word(input_str) == expected_output

def test_first_repeated_word_example2():
    input_str = "I am learning programming at ASAC."
    expected_output = "No Repetition"
    assert first_repeated_word(input_str) == expected_output

def test_first_repeated_word_no_repetition():
    input_str = "No words are repeated in this sentence."
    expected_output = "No Repetition"
    assert first_repeated_word(input_str) == expected_output

def test_first_repeated_word_mixed_case():
    input_str = "Hello hello"
    expected_output = "No Repetition"
    assert first_repeated_word(input_str) == expected_output

def test_first_repeated_word_empty_string():
    input_str = ""
    expected_output = "No Repetition"
    assert first_repeated_word(input_str) == expected_output

if __name__ == "__main__":
    pytest.main()

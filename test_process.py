import pytest
import process

@pytest.mark.state
@pytest.mark.parametrize(
    'value,expected',
    [
        ([8],['positivo','par']),
    ]
)
def test_statement_coverage(value, expected):
    result = process.process(value)
    assert result == expected

@pytest.mark.branch
@pytest.mark.parametrize(
    'value,expected',
    [
        ([10,-3],['positivo','par']),
        ([],[])
    ]
)
def test_branch_coverage(value, expected):
    result = process.process(value)
    assert result == expected

@pytest.mark.path
@pytest.mark.parametrize(
    'value,expected',
    [
        ([6,12],['positivo','par','positivo','par']),
        ([4,9],['positivo','par','positivo']),
        ([20,0],['positivo','par','par']),
        ([2,-5],['positivo','par']),
        ([3,14],['positivo','positivo','par']),
        ([5,11],['positivo','positivo']),
        ([7,-8],['positivo','par']),
        ([1,-9],['positivo']),
        ([-4,16],['par','positivo','par']),
        ([0,13],['par','positivo']),
        ([-2,-6],['par','par']),
        ([-10,-1],['par']),
        ([-7,8],['positivo','par']),
        ([-3,15],['positivo']),
        ([-11,0],['par']),
        ([-5,-13],[]),
    ]
)
def test_path_coverage(value, expected):
    result = process.process(value)
    assert result == expected




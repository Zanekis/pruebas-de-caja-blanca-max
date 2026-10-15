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



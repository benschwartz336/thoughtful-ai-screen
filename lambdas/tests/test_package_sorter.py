from src.package_sorter.handler import lambda_handler


def test_lambda_handler_valid_input_standard():
    event = {"width": "10", "height": "10", "length": "10", "mass": "1"}
    result = lambda_handler(event, None)
    assert result["statusCode"] == 200
    assert result["body"] == "STANDARD"


def test_lambda_handler_valid_input_special_bulky():
    event = {"width": "150", "height": "10", "length": "10", "mass": "10"}
    result = lambda_handler(event, None)
    assert result["statusCode"] == 200
    assert result["body"] == "SPECIAL"


def test_lambda_handler_valid_input_special_heavy():
    event = {"width": "10", "height": "10", "length": "10", "mass": "20"}
    result = lambda_handler(event, None)
    assert result["statusCode"] == 200
    assert result["body"] == "SPECIAL"


def test_lambda_handler_valid_input_rejected():
    event = {"width": "150", "height": "10", "length": "10", "mass": "20"}
    result = lambda_handler(event, None)
    assert result["statusCode"] == 200
    assert result["body"] == "REJECTED"


def test_lambda_handler_invalid_input_missing_key():
    event = {
        "width": "10",
        "height": "10",
        "length": "10",
        # Missing 'mass'
    }
    result = lambda_handler(event, None)
    assert result["statusCode"] == 400
    assert "Missing or invalid input" in result["body"]


def test_lambda_handler_invalid_input_non_numeric():
    event = {"width": "ten", "height": "10", "length": "10", "mass": "5"}
    result = lambda_handler(event, None)
    assert result["statusCode"] == 400
    assert "Missing or invalid input" in result["body"]


def test_lambda_handler_negative_values():
    event = {"width": "-10", "height": "10", "length": "10", "mass": "5"}
    result = lambda_handler(event, None)
    assert result["statusCode"] == 400
    assert (
        result["body"]
        == "Negative values are not allowed for width, height, length, or mass."
    )

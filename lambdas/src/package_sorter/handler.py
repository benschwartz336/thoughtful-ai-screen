from src.lib.helpers import sort_package
from src.lib.logger import get_logger

logger = get_logger()


def lambda_handler(event, context):
    """
    AWS Lambda handler to sort a package.
    Expects 'width', 'height', 'length', and 'mass' in the event payload.

    Example event:
    {
      "width": "10",
      "height": "20",
      "length": "30",
      "mass": "5"
    }
    """
    try:
        width = float(event["width"])
        height = float(event["height"])
        length = float(event["length"])
        mass = float(event["mass"])

        if any(val < 0 for val in [width, height, length, mass]):
            return {
                "statusCode": 400,
                "body": "Negative values are not allowed for width, height, length, or mass.",
            }

    except (KeyError, ValueError) as e:
        # KeyError: Missing one of the keys in the event.
        # ValueError: Conversion to float failed (invalid numeric input).
        return {"statusCode": 400, "body": f"Missing or invalid input: {str(e)}"}

    result = sort_package(width, height, length, mass)

    return {"statusCode": 200, "body": result}

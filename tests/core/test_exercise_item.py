import pytest

from sales_taxes_problem.core import ExerciseItem, ExerciseTaxCalculator
from tests.core.helpers import ITEM_NAME, ITEM_PRICE, ITEM_QUANTITY, ItemInfo


def test_exercise_tax_calculator_init() -> None:
    """
    Test the ExerciseTaxCalculator constructor.
    """
    ex_tax_calculator = ExerciseTaxCalculator()
    assert ex_tax_calculator is not None


@pytest.mark.parametrize(
    "amount,rounded",
    [
        (12.230, 12.25),
        (12.231, 12.25),
        (12.232, 12.25),
        (12.233, 12.25),
        (12.234, 12.25),
        (12.235, 12.25),
        (12.236, 12.25),
        (12.237, 12.25),
        (12.238, 12.25),
        (12.239, 12.25),
        (12.200, 12.20),
        (12.201, 12.25),
        (12.202, 12.25),
    ],
)  # type: ignore[misc]
def test_exercise_tax_calculator_round_up(amount: float, rounded: float) -> None:
    """
    Test the rounding is correctly computed.
    """
    ex_tax_calculator = ExerciseTaxCalculator()
    assert ex_tax_calculator.round_up(amount) == rounded


@pytest.mark.parametrize(
    "item_name,item_price,expected_tax",
    [
        ("book", 12.49, 0),
        ("music", 14.99, 1.5),
        ("chocolate bar", 0.85, 0),
        ("imported box of chocolate", 10, 0.5),
        ("imported bottle of perfume", 47.5, 7.15),
        ("bottle of perfume", 18.99, 1.9),
        ("packet of headache pills", 9.75, 0),
        ("box of imported chocolates", 11.25, 0.6),
    ],
)  # type: ignore[misc]
def test_exercise_tax_calculator_compute_tax(
    item_name: str, item_price: float, expected_tax: float
) -> None:
    """
    Test the taxes are correctly computed.
    """
    ex_tax_calculator = ExerciseTaxCalculator()
    assert ex_tax_calculator.compute_tax(item_name=item_name, item_price=item_price) == expected_tax


def test_exercise_item_init() -> None:
    """
    Test the ExerciseItem constructor.
    """
    ex_item = ExerciseItem(name=ITEM_NAME, quantity=ITEM_QUANTITY, price=ITEM_PRICE)
    assert ex_item is not None
    assert ex_item.name == ITEM_NAME
    assert ex_item.price == ITEM_PRICE
    assert ex_item.quantity == ITEM_QUANTITY


@pytest.mark.parametrize(
    "item_info,expected_taxes",
    [
        (ItemInfo(quantity=0, price=14.99, name="music"), 1.5),
        (ItemInfo(quantity=1, price=14.99, name="music"), 1.5),
        (ItemInfo(quantity=2, price=14.99, name="music"), 1.5),
        (ItemInfo(quantity=2, price=14.99, name="music"), 1.5),
        (ItemInfo(quantity=2, price=14.99, name="chocolate bar"), 0),
        (ItemInfo(quantity=2, price=10, name="imported box of chocolate"), 0.5),
    ],
)  # type: ignore[misc]
def test_exercise_item_get_taxes(item_info: ItemInfo, expected_taxes: float) -> None:
    """
    Test the taxes are correctly computed.
    """
    assert (
        ExerciseItem(
            name=item_info.name, quantity=item_info.quantity, price=item_info.price
        ).get_taxes()
        == expected_taxes
    )
from typing import Any

import pytest

from maloident.models import IdentificationParameter, ResultNegative, ResultPositive

from .example_jsons import negative_response_body, positive_response_body, request_body


@pytest.mark.parametrize(
    "json_dict",
    [
        request_body,
    ],
)
def test_request_model(json_dict: dict[str, Any]) -> None:
    model = IdentificationParameter.model_validate(json_dict)
    re_serialized = model.model_dump(mode="json")
    assert re_serialized == json_dict


@pytest.mark.parametrize(
    "json_dict",
    [
        positive_response_body,
    ],
)
def test_positive_response_model(json_dict: dict[str, Any]) -> None:
    model = ResultPositive.model_validate(json_dict)
    re_serialized = model.model_dump(mode="json")
    assert re_serialized == json_dict


@pytest.mark.parametrize(
    "json_dict",
    [
        negative_response_body,
    ],
)
def test_negative_response_model(json_dict: dict[str, Any]) -> None:
    model = ResultNegative.model_validate(json_dict)
    re_serialized = model.model_dump(mode="json")
    assert re_serialized == json_dict

from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
import jsonschema


class JSONSchemaValidator(BaseValidator):
    def compare(self, value, schema):
        try:
            jsonschema.validate(value, schema)
        except jsonschema.exceptions.ValidationError:
            ValidationError(
                f"{value} is not a valid JSON schema",
                code="invalid",
                params={"value": value},
            )

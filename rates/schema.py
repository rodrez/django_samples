RATE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "headers": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "name": {"type": "string"},
                        "error": {"type": ["string", "null"]},
                    },
                    "required": ["id", "name"],
                },
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "name": {"type": "string"},
                    },
                    "required": ["id", "name"],
                },
            ],
        },
        "yearRanges": {
            "type": "array",
            "minItems": 1,
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "startingYear": {
                            "type": "object",
                            "properties": {
                                "value": {"type": "integer"},
                                "error": {"type": ["string", "null"]},
                            },
                            "required": ["value"],
                        },
                        "endingYear": {
                            "type": "object",
                            "properties": {
                                "value": {"type": "integer"},
                                "error": {"type": ["string", "null"]},
                            },
                            "required": ["value"],
                        },
                        "rows": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "string"},
                                        "months": {
                                            "type": "object",
                                            "properties": {
                                                "value": {"type": "integer"},
                                                "error": {"type": ["string", "null"]},
                                            },
                                            "required": ["value"],
                                        },
                                        "cells": {
                                            "type": "array",
                                            "items": [
                                                {
                                                    "type": "object",
                                                    "properties": {
                                                        "id": {"type": "string"},
                                                        "value": {"type": "string"},
                                                        "error": {
                                                            "type": ["string", "null"]
                                                        },
                                                    },
                                                    "required": ["id", "value"],
                                                },
                                                {
                                                    "type": "object",
                                                    "properties": {
                                                        "id": {"type": "string"},
                                                        "value": {"type": "string"},
                                                    },
                                                    "required": ["id", "value"],
                                                },
                                            ],
                                        },
                                    },
                                    "required": ["id", "months", "cells"],
                                }
                            ],
                        },
                    },
                    "required": ["id", "startingYear", "endingYear", "rows"],
                }
            ],
        },
        "focusedInput": {
            "type": ["object", "null"],
            "properties": {"id": {"type": "string"}, "position": {"type": "integer"}},
        },
    },
}

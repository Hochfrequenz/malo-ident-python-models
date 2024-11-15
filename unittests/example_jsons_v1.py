# raw jsons copied from swagger hub
# + manual post-processing to fix the errors in the official docs

request_body = {
    "identificationDateTime": "2023-08-02T22:00:00Z",
    "energyDirection": "consumption",
    "identificationParameterId": {
        "maloId": "57685676748",
        "tranchenIds": ["57685676742"],
        "meloIds": ["DE00014545768S0000000000000003054"],
        "meterNumbers": ["1SM-8465929523"],
        "customerNumber": "V567345345",
    },
    "identificationParameterAddress": {
        "name": {"surnames": "Becker", "firstnames": "Michael", "title": "Prof.Dr.", "company": "BDEW & Co. KG"},
        "address": {
            "countryCode": "DE",
            "zipCode": "12117",
            "city": "Berlin",
            "street": "Reinhardtstraße",
            "houseNumber": 32,
            "houseNumberAddition": "F",
        },
        "landParcels": [{"districtName": "string", "lotNumber": "string", "subLotNumber": "string"}],
        "geographicCoordinates": {
            "latitude": "string",
            "longitude": "string",
            "east": "string",
            "north": "string",
            "zone": "UTMZone31",
            "northing": "string",
            "easting": "string",
        },
    },
}

positive_response_body = {
    "dataMarketLocation": {
        "maloId": "57685676748",
        "energyDirection": "consumption",
        "measurementTechnologyClassification": "intelligentMeasuringSystem",
        "optionalChangeForecastBasis": "possible",
        "dataMarketLocationProperties": [
            {
                "marketLocationProperty": "measured",
                "executionTimeFrom": "2023-08-01T22:00:00Z",
                "executionTimeUntil": "2023-08-01T22:00:00Z",
            }
        ],
        "dataMarketLocationNetworkOperators": [
            {
                "marketPartnerId": 9900987654321,
                "executionTimeFrom": "2023-08-01T22:00:00Z",
                "executionTimeUntil": "2023-08-01T22:00:00Z",
            }
        ],
        "dataMarketLocationMeasuringPointOperators": [
            {
                "marketPartnerId": 9900987654321,
                "executionTimeFrom": "2023-08-01T22:00:00Z",
                "executionTimeUntil": "2023-08-01T22:00:00Z",
            }
        ],
        "dataMarketLocationTransmissionSystemOperators": [
            {
                "marketPartnerId": 9900987654321,
                "executionTimeFrom": "2023-08-01T22:00:00Z",
                "executionTimeUntil": "2023-08-01T22:00:00Z",
            }
        ],
        "dataMarketLocationSuppliers": [
            {
                "marketPartnerId": 9900987654321,
                "executionTimeFrom": "2023-08-01T22:00:00Z",
                "executionTimeUntil": "2023-08-01T22:00:00Z",
            }
        ],
        "dataMarketLocationName": {
            "surnames": "Becker",
            "firstnames": "Michael",
            "title": "Prof.Dr.",
            "company": "BDEW & Co. KG",
        },
        "dataMarketLocationAddress": {
            "countryCode": "DE",
            "zipCode": "12117",
            "city": "Berlin",
            "street": "Reinhardtstraße",
            "houseNumber": 32,
            "houseNumberAddition": "F",
        },
        "dataMarketLocationLandParcels": [{"districtName": "string", "lotNumber": "string", "subLotNumber": "string"}],
        "dataMarketLocationGeographicCoordinates": {
            "latitude": "string",
            "longitude": "string",
            "east": "string",
            "north": "string",
            "zone": "UTMZone31",
            "northing": "string",
            "easting": "string",
        },
    },
    "dataTranches": [
        {
            "tranchenId": "57685676742",
            "proportion": "percent",
            "percent": 75.912,
            "dataTrancheSuppliers": [
                {
                    "marketPartnerId": 9900987654321,
                    "executionTimeFrom": "2023-08-01T22:00:00Z",
                    "executionTimeUntil": "2023-08-01T22:00:00Z",
                }
            ],
        }
    ],
    "dataMeterLocations": [
        {
            "meloId": "DE00014545768S0000000000000003054",
            "meterNumber": "1SM-8465929523",
            "dataMeterLocationMeasuringPointOperators": [
                {
                    "marketPartnerId": 9900987654321,
                    "executionTimeFrom": "2023-08-01T22:00:00Z",
                    "executionTimeUntil": "2023-08-01T22:00:00Z",
                }
            ],
        }
    ],
    "dataTechnicalResources": [{"trId": "D1234848431"}],
    "dataControllableResources": [
        {
            "srId": "C1234848431",
            "dataControllableResourceMeasuringPointOperators": [
                {
                    "marketPartnerId": 9900987654321,
                    "executionTimeFrom": "2023-08-01T22:00:00Z",
                    "executionTimeUntil": "2023-08-01T22:00:00Z",
                }
            ],
        }
    ],
    "dataNetworkLocations": [
        {
            "neloId": "E1234848431",
            "dataNetworkLocationMeasuringPointOperators": [
                {
                    "marketPartnerId": 9900987654321,
                    "executionTimeFrom": "2023-08-01T22:00:00Z",
                    "executionTimeUntil": "2023-08-01T22:00:00Z",
                }
            ],
        }
    ],
}

positive_response_body["dataMarketLocation"]["dataMarketLocationProperties"][0][  # type:ignore[index]
    "marketLocationProperty"
] = "standard"  # not "measured", because the official example doesn't match their own schema

negative_response_body = {
    "decisionTree": "E_0594",
    "responseCode": "A10",
    "reason": "Ich bin ein Freitext.",
    "networkOperator": 9900987654321,
}

import os
import requests


BASE_URL = "https://qa-sample-neha-eman.up.railway.app"

OFFLINE_DEVICE_ID = "0JM1M6210063"


def get_token():
    response = requests.post(
        f"{BASE_URL}/api/auth/signin",
        json={
            "email": os.getenv("TEST_EMAIL"),
            "password": os.getenv("TEST_PASSWORD"),
        },
    )

    assert response.status_code == 200

    return response.json()["token"]


def test_offline_device_command_does_not_return_500():
    token = get_token()

    response = requests.post(
        f"{BASE_URL}/api/devices/command",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "devices": [OFFLINE_DEVICE_ID],
            "command_name": "update_core_services",
            "params": {
                "command_version": "6.4.10"
            },
        },
    )

    data = response.json()

    # Offline device is an expected business condition, so it should not be treated as an internal server error.
    assert response.status_code < 500, (
        f"Expected a non-5xx response for offline device, "
        f"but got {response.status_code}: {data}"
    )

    # Internal implementation details should not be exposed.
    assert "stack" not in data, (
        f"API response exposed an internal stack trace: {data}"
    )

from onfido import Passkey, PasskeyUpdater, PasskeysList

SAMPLE_USERNAME = "sample-username"
SAMPLE_PASSKEY_ID = "00000000-0000-0000-0000-000000000000"


def test_list_passkeys(onfido_api):
    passkeys = onfido_api.list_passkeys(SAMPLE_USERNAME)

    assert isinstance(passkeys, PasskeysList)
    assert len(passkeys.passkeys) > 0

    sample_passkey = next(
        (passkey for passkey in passkeys.passkeys if passkey.id == SAMPLE_PASSKEY_ID),
        passkeys.passkeys[0],
    )

    assert isinstance(sample_passkey, Passkey)
    assert sample_passkey.application_domain is not None
    assert sample_passkey.state is not None
    assert sample_passkey.created_at is not None
    assert sample_passkey.model_dump_json(by_alias=True, exclude_none=True) is not None


def test_find_passkey(onfido_api):
    passkey = onfido_api.find_passkey(SAMPLE_USERNAME, SAMPLE_PASSKEY_ID)

    assert isinstance(passkey, Passkey)
    assert passkey.id == SAMPLE_PASSKEY_ID
    assert passkey.application_domain is not None
    assert passkey.state is not None
    assert passkey.created_at is not None
    assert passkey.model_dump_json(by_alias=True, exclude_none=True) is not None


def test_update_passkey_state(onfido_api):
    updated_passkey = onfido_api.update_passkey(
        SAMPLE_USERNAME,
        SAMPLE_PASSKEY_ID,
        PasskeyUpdater(state="INACTIVE"),
    )

    assert isinstance(updated_passkey, Passkey)
    assert updated_passkey.id == SAMPLE_PASSKEY_ID
    assert updated_passkey.state == "INACTIVE"


def test_delete_passkey_success(onfido_api):
    response = onfido_api.delete_passkey_with_http_info(
        SAMPLE_USERNAME,
        SAMPLE_PASSKEY_ID,
    )

    assert response.status_code == 204


def test_delete_passkeys_success(onfido_api):
    response = onfido_api.delete_passkeys_with_http_info(SAMPLE_USERNAME)

    assert response.status_code == 204

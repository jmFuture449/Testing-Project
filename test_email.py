import pytest

from email_utils import (
	get_domain,
	is_valid_email,
	local_part,
	masked_email,
)


@pytest.mark.parametrize(
	"email",
	[
		"user@example.com",
		"first.last@example.org",
		"user@mail.example.com",  # Sub-domain edge case
	],
)
def test_is_valid_email_accepts_valid_addresses(email):
	assert is_valid_email(email) is True


@pytest.mark.parametrize(
	"email",
	[
		"plainaddress",
		"user@",
		"@example.com",
	],
)
def test_is_valid_email_rejects_invalid_addresses(email):
	assert is_valid_email(email) is False


@pytest.mark.parametrize(
	"email",
	[
		"user@example.com trailing",
		"user@example.com!",
		None,
	],
)
def test_is_valid_email_rejects_partial_or_non_string_matches(email):
	assert is_valid_email(email) is False


@pytest.mark.parametrize("address", ["plainaddress", "user@", "@example.com"])
def test_email_helpers_reject_malformed_addresses(address):
	with pytest.raises(ValueError, match="Invalid email address"):
		get_domain(address)
	with pytest.raises(ValueError, match="Invalid email address"):
		local_part(address)
	with pytest.raises(ValueError, match="Invalid email address"):
		masked_email(address)


def test_email_parts_are_extracted():
	assert get_domain("first.last@mail.example.com") == "mail.example.com"
	assert local_part("first.last@mail.example.com") == "first.last"


def test_masked_email_masks_only_the_local_part():
	assert masked_email("john@example.com") == "jo**@example.com"
	assert masked_email("john@example.com", show=0) == "****@example.com"

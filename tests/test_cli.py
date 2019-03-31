import os
import pytest
from click.testing import CliRunner
from mock import patch

from numerapi import cli


@pytest.fixture(scope='function', name="login")
def login():
    os.environ["NUMERAI_PUBLIC_ID"] = "foo"
    os.environ["NUMERAI_SECRET_KEY"] = "bar"
    yield None
    # teardown
    del os.environ["NUMERAI_PUBLIC_ID"]
    del os.environ["NUMERAI_SECRET_KEY"]


@patch('numerapi.NumerAPI.download_current_dataset')
def test_download_dataset(mocked):
    result = CliRunner().invoke(cli.download_dataset)
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.get_dataset_url')
def test_dataset_url(mocked):
    result = CliRunner().invoke(cli.dataset_url, ['--tournament', 1])
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.get_leaderboard')
def test_leaderboard(mocked):
    result = CliRunner().invoke(cli.leaderboard, ['--tournament', 1])
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.get_staking_leaderboard')
def test_staking_leaderboard(mocked):
    result = CliRunner().invoke(cli.staking_leaderboard, ['--tournament', 1])
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.get_competitions')
def test_competitions(mocked):
    result = CliRunner().invoke(cli.competitions, ['--tournament', 1])
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.get_current_round')
def test_current_round(mocked):
    result = CliRunner().invoke(cli.current_round, ['--tournament', 1])
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.get_submission_ids')
def test_submission_ids(mocked):
    result = CliRunner().invoke(cli.submission_ids, ['--tournament', 1])
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.get_rankings')
def test_rankings(mocked):
    result = CliRunner().invoke(cli.rankings)
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.get_user_activities')
def test_user_activities(mocked, login):
    result = CliRunner().invoke(cli.user_activities, 'username')
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.get_submission_filenames')
def test_submission_filenames(mocked):
    result = CliRunner().invoke(cli.submission_filenames, ['--tournament', 1])
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.get_staking_cutoff')
def test_staking_cutoff(mocked):
    result = CliRunner().invoke(cli.staking_cutoff, ['--tournament', 1])
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.check_new_round')
def test_check_new_round(mocked):
    result = CliRunner().invoke(cli.check_new_round, ['--tournament', 1])
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.get_user')
def test_user(mocked, login):
    result = CliRunner().invoke(cli.user)
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.get_payments')
def test_payments(mocked, login):
    result = CliRunner().invoke(cli.payments)
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.submission_status')
def test_submission_status(mocked, login):
    result = CliRunner().invoke(cli.submission_status, ['subm_id'])
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.get_transactions')
def test_transactions(mocked):
    result = CliRunner().invoke(cli.transactions)
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.get_stakes')
def test_stakes(mocked):
    result = CliRunner().invoke(cli.stakes)
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.get_tournaments')
def test_tournaments(mocked):
    result = CliRunner().invoke(cli.tournaments)
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.tournament_number2name')
def test_tournament_number2name(mocked):
    result = CliRunner().invoke(cli.tournament_number2name, ["1"])
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.tournament_name2number')
def test_tournament_name2number(mocked):
    result = CliRunner().invoke(cli.tournament_name2number, ["frank"])
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.check_submission_successful')
def test_submission_successful(mocked, login):
    result = CliRunner().invoke(cli.submission_successful, ["subm_id"])
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.stake')
def test_stake(mocked, login):
    result = CliRunner().invoke(cli.stake, ["0.1", "1"])
    # just testing if calling works fine
    assert result.exit_code == 0


@patch('numerapi.NumerAPI.submit')
def test_submit(mocked):
    result = CliRunner().invoke(cli.submit, ['--tournament', 1])
    # just testing if calling works fine
    assert result.exit_code == 0


def test_version():
    result = CliRunner().invoke(cli.version)
    # just testing if calling works fine
    assert result.exit_code == 0
#!/usr/bin/python3

from peerfeedback.interfaces import Candidate, CandidateMap
from peerfeedback import output
import pytest


@pytest.fixture
def test_map():
    """CandidateMap test data."""
    return CandidateMap(
        {
            Candidate("hans.wurst@stud.leuphana.de"): (
                Candidate("darth.vader@stud.leuphana.de"),
                Candidate("boris.becker@stud.leuphana.de"),
            ),
            Candidate("darth.vader@stud.leuphana.de"): (
                Candidate("boris.becker@stud.leuphana.de"),
                Candidate("donald.duck@stud.leuphana.de"),
            ),
            Candidate("boris.becker@stud.leuphana.de"): (
                Candidate("donald.duck@stud.leuphana.de"),
                Candidate("luke.skywalked@stud.leuphana.de"),
            ),
            Candidate("donald.duck@stud.leuphana.de"): (
                Candidate("luke.skywalked@stud.leuphana.de"),
                Candidate("hans.wurst@stud.leuphana.de"),
            ),
            Candidate("luke.skywalked@stud.leuphana.de"): (
                Candidate("hans.wurst@stud.leuphana.de"),
                Candidate("darth.vader@stud.leuphana.de"),
            ),
        }
    )


def test_get_providers(test_map):
    expected_vader = (
        Candidate("hans.wurst@stud.leuphana.de"),
        Candidate("luke.skywalked@stud.leuphana.de"),
    )
    expected_becker = (
        Candidate("hans.wurst@stud.leuphana.de"),
        Candidate("darth.vader@stud.leuphana.de"),
    )
    assert (
        output.get_providers(Candidate("darth.vader@stud.leuphana.de"), test_map)
        == expected_vader
    )
    assert (
        output.get_providers(Candidate("boris.becker@stud.leuphana.de"), test_map)
        == expected_becker
    )


def test_get_recipients(test_map):
    for candidate, pair in test_map.mappings.items():
        assert pair == output.get_recipients(candidate, test_map)


def test_generate_row(test_map):
    hans = Candidate("hans.wurst@stud.leuphana.de")

    expected = (
        "hans.wurst@stud.leuphana.de",
        "darth.vader@stud.leuphana.de",
        "boris.becker@stud.leuphana.de",
        "donald.duck@stud.leuphana.de",
        "luke.skywalked@stud.leuphana.de",
    )
    out = output.generate_row(hans, test_map)
    assert out == expected


@pytest.mark.destructive
def test_write_to_file(test_map):
    rows = [output.generate_row(stud, test_map) for stud in test_map.mappings.keys()]
    output.write_to_file(rows, "peerfeedbackmatcher.xlsx")


def test_create_output_filename():
    input_filename = "abc.xlsx"
    assert output.create_output_filename(input_filename) == "abc_output.xlsx"

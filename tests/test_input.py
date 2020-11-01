#!/usr/bin/python3

from peerfeedback import input
from peerfeedback.interfaces import Candidate


def test_read_students_from_file():
    filename = "peerfeedbackmatcher.xlsx"
    expected = [
        Candidate("hans.wurst@stud.leuphana.de"),
        Candidate("darth.vader@stud.leuphana.de"),
        Candidate("boris.becker@stud.leuphana.de"),
        Candidate("donald.duck@stud.leuphana.de"),
        Candidate("luke.skywalked@stud.leuphana.de"),
    ]

    assert input.read_candidates_from_file(filename) == expected


def test_parse_student():
    test_string = "hans.wurst@stud.leuphana.de"
    test_string2 = "hans.wurst2@stud.leuphana.de"

    assert input.parse_candidate(test_string) == Candidate(test_string)
    assert input.parse_candidate(test_string2) == Candidate(test_string2)
    assert input.parse_candidate("") == None
    assert input.parse_candidate("michal@gmail.com") == None
    assert input.parse_candidate("@stud.leuphana.de") == None

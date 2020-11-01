#!/usr/bin/python3

from peerfeedback import matcher
from peerfeedback.interfaces import Candidate, CandidateMap


def test_create_map():
    candidate_list = [
        Candidate("hans.wurst@stud.leuphana.de"),
        Candidate("darth.vader@stud.leuphana.de"),
        Candidate("boris.becker@stud.leuphana.de"),
        Candidate("donald.duck@stud.leuphana.de"),
        Candidate("luke.skywalked@stud.leuphana.de"),
    ]

    expected = CandidateMap({
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
    })

    assert matcher.create_map(candidate_list) == expected

from grandpybot_app import Rhetoric


def test_parser():
    """Tests the user entry parser"""

    entry = "dis-moi papy, sais tu ou ce trouve la gare à bordeaux?"
    assert Rhetoric.parse_entry(entry) == "gare bordeaux"
    entry = "DIS-MOI PAPY, SAIS TU OU CE TROUVE LA GARE A BORDEAUX?"
    assert Rhetoric.parse_entry(entry) == "gare bordeaux"
    entry = "Hey Grandpy, je compte jusqu'à 3 et tu me réponds!!!"
    assert Rhetoric.parse_entry(entry) == ""

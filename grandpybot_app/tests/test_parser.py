from grandpybot_app import Rhetoric


def test_irrelevant_words():
    query = "Hey Grandpy, je compte jusqu'à 3 et tu me réponds!!!"
    parsed_result = Rhetoric.parse_entry(query)
    assert parsed_result == ""


def test_lower_words():
    query = "DIS-MOI PAPY, SAIS TU OU CE TROUVE LA GARE A BORDEAUX?"
    parsed_result = Rhetoric.parse_entry(query)
    assert parsed_result.islower()


def test_parser_result():
    query = "dis-moi papy, sais tu ou ce trouve la gare à bordeaux?"
    parsed_result = Rhetoric.parse_entry(query)
    assert parsed_result == "gare bordeaux"

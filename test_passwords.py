""" Test cases for our python password cracker """


def possible_passwords(first, last, dob, date2, mothers_maiden, spouse, date3,
                       pet1, pet2, first_love, child1, child2):
    '''Function takes a list of possible data values and returns a list of
    possible passwords'''
    return []


def test_Isaiah():
    result = possible_passwords("Isaiah", "Bailey", "03/29/1956",
                                "03/27/1951", "Morgan", "Brody", "09/20/1954",
                                "Sparky", "Mia", "Ava", "Serenity", "Nevaeh")

    assert("Sparky" in result, "crack in not finding pet as password")


def test_first_love():
    "check if first love is returned as a possible password"
    passwords = possible_passwords('Isaiah', 'Bailey', '03/29/1956', '03/27/1951', 'Morgan',
                                   'Brody', '09/20/1954', 'Sparky', 'Mia', 'Ava', 'Serenity', 'Nevaeh')
    
    assert 'Ava' in passwords, 'Did not find FirstLove in possible passwords'


def test_first_love1():
    "check if first love + # is returned as a possible password"
    passwords = possible_passwords('Isaiah', 'Bailey', '03/29/1956', '03/27/1951', 'Morgan',
                                   'Brody', '09/20/1954', 'Sparky', 'Mia', 'Ava', 'Serenity', 'Nevaeh')
    
    assert 'Ava1' in passwords, 'Did not find FirstLove1 in possible passwords'

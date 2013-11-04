import animals


def test_read_animals():
    ref_dates = ['2011-04-22', '2011-04-23', '2011-04-23', '2011-04-23', '2011-04-23']
    ref_times = ['21:06', '14:12', '10:24', '20:08', '18:46']
    ref_species = ['Grizzly', 'Elk', 'Elk', 'Wolverine', 'Muskox']
    ref_counts = [36, 25, 26, 31, 20]

    dates,times,species,counts = animals.read_animals('animals.txt')

    assert dates == ref_dates
    assert times == ref_times
    assert species == ref_species
    assert counts == ref_counts

def test_mean():
    ref_ints  = [5, 6, 7, 8, 9]
    ref_floats = [2.5, 3.5, 4.5]
    ref_strings = ['nan', 4, 'what', 7]

    assert animals.mean(ref_ints) == 7.0
    assert animals.mean(ref_floats) == 3.5
    




def test_filter_animals():
    date, time, species, count = animals.read_animals('animals.txt')
    kind = 'Grizzly'
    d, t, s, c = animals.filter_animals_by_kind(kind, date, time, species, count)

    assert d == ['2011-04-22']
    assert t == ['21:06']
    assert s == ['Grizzly']
    assert c == [36]

    kind = 'Elk'
    d, t, s, c = animals.filter_animals_by_kind(kind, date, time, species, count)

    assert d == ['2011-04-23', '2011-04-23']
    assert t == ['14:12', '10:24']
    assert s == ['Elk', 'Elk']
    assert c == [25, 26]


def test_mean_animals():
    mean = animals.mean_animals('animals.txt', 'Grizzly')
    assert mean == 36

    mean = animals.mean_animals('animals.txt', 'Elk')
    assert mean == 25.5


import psycopg2


def test_database():

    conn = psycopg2.connect("host=db dbname=postgres user=postgres password=postgres")
    assert conn is not None

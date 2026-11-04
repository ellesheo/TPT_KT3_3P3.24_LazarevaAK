import sqlite3

import pytest


def string_length(text):
    if not isinstance(text, str):
        raise TypeError
    return len(text)


def save_to_file(text, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def add_user(conn, name, age):
    conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()


@pytest.fixture(params=["", "привет", "   ", "первая\nвторая"], ids=["empty", "word", "spaces", "multiline"])
def text(request):
    return request.param


@pytest.fixture
def db(tmp_path):
    conn = sqlite3.connect(tmp_path / "test.db")
    conn.execute("CREATE TABLE users (name TEXT NOT NULL, age INTEGER NOT NULL CHECK (age >= 0))")
    yield conn
    conn.execute("DELETE FROM users")
    conn.commit()
    conn.close()


@pytest.mark.parametrize("value, expected", [
    ("", 0),
    ("hello", 5),
    ("   ", 3),
    ("a\nb\nc", 5),
], ids=["empty", "word", "spaces", "multiline"])
def test_string_length(value, expected):
    assert string_length(value) == expected


def test_save_to_file(tmp_path, text):
    path = tmp_path / "result.txt"
    save_to_file(text, path)
    assert path.read_text(encoding="utf-8") == text


@pytest.mark.parametrize("name, age", [("Alina", 19), ("Ivan", 0)])
def test_add_user(db, name, age):
    add_user(db, name, age)
    assert db.execute("SELECT name, age FROM users").fetchall() == [(name, age)]


@pytest.mark.parametrize("name, age", [("Oleg", -1), (None, 20)])
def test_add_user_error(db, name, age):
    with pytest.raises(sqlite3.IntegrityError):
        add_user(db, name, age)

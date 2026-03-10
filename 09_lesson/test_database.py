from sqlalchemy import create_engine, inspect, text
import pytest

db_connection_string = "sqlite:///C:/sqlite/mydatabase.db"
db = create_engine(db_connection_string)

def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO student(user_id, level, education_form, subject_id) VALUES (:new_user_id, :new_level, :new_education_form, :new_subject_id)")
    connection.execute(sql, {
        "new_user_id": 111111111111111, 
        "new_level": "Advanced", 
        "new_education_form": "group", 
        "new_subject_id": 1
        })
    
    sql_statement = text("SELECT * FROM student WHERE user_id = :id")
    result = connection.execute(sql_statement, {
        "id": 111111111111111
        })
    rows = result.mappings().all()

    assert rows[0]["level"] == "Advanced" 
    
    sql = text("DELETE FROM student WHERE user_id = :id")
    connection.execute(sql, {
        "id": 111111111111111
        })

    transaction.commit()
    connection.close()

def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO student(user_id, level, education_form, subject_id) VALUES (:new_user_id, :new_level, :new_education_form, :new_subject_id)")
    connection.execute(sql, {
        "new_user_id": 111111111111111, 
        "new_level": "Advanced", 
        "new_education_form": "group", 
        "new_subject_id": 1
        })

    sql = text("UPDATE student SET level = :new_level WHERE user_id = :id")
    connection.execute(sql, {
        "new_level": 'Pre-Intermediate', 
        "id": 111111111111111
        })
    
    sql_statement = text("SELECT * FROM student WHERE user_id = :id")
    result = connection.execute(sql_statement, {
        "id": 111111111111111
        })
    rows = result.mappings().all()

    assert rows[0]["level"] == "Pre-Intermediate" 
    
    sql = text("DELETE FROM student WHERE user_id = :id")
    connection.execute(sql, {
        "id": 111111111111111
        })

    transaction.commit()
    connection.close()

def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO student(user_id, level, education_form, subject_id) VALUES (:new_user_id, :new_level, :new_education_form, :new_subject_id)")
    connection.execute(sql, {
        "new_user_id": 111111111111111, 
        "new_level": "Advanced", 
        "new_education_form": "group", 
        "new_subject_id": 1
        })

    sql = text("DELETE FROM student WHERE user_id = :id")
    connection.execute(sql, {
        "id": 111111111111111
        })
    
    sql_statement = text("SELECT * FROM student WHERE user_id = :id")
    result = connection.execute(sql_statement, {
        "id": 111111111111111
        })
    rows = result.mappings().all()

    assert len(rows) == 0

    transaction.commit()
    connection.close()
# from graph import *
from ClassRoom import data_for_graph, get_PS, avg, top_five, bottom_five
from student import faculty, student
import pytest

ps = get_PS()


@pytest.fixture
def s():
    return student(99003709)


def test_student(s):
    assert s.getScore() == [[10, 8, 9, 9, 9, 8], [10, 9, 7, 9, 8, 7], [
        7, 9, 8, 7, 9, 7], [10, 7, 9, 8, 9, 7]]
    assert s.classAverage() == [[8.1, 15.7, 23.5, 30.8, 38.8, 46.2], [8.0, 16.1, 23.9, 31.9, 39.2, 47.0], [
        7.5, 15.9, 23.9, 31.4, 39.4, 47.0], [8.6, 16.9, 24.8, 32.6, 39.2, 47.1]]


@pytest.fixture
def f():
    return faculty(ps)


def test_faculty(f):
    assert f.getAvg() == [[8.1, 15.7, 23.5, 30.8, 38.8, 46.2], [8.0, 16.1, 23.9, 31.9, 39.2, 47.0], [
        7.5, 15.9, 23.9, 31.4, 39.4, 47.0], [8.6, 16.9, 24.8, 32.6, 39.2, 47.1]]
    assert f.get_top_five() == [53, 52, 48, 47, 46]
    assert f.get_bottom_five() == [40, 41, 44, 45, 46]
    assert f.get_mail() == ['ashish.pareek@ltts.com', 'lalit.bhardwaj@ltts.com', 'ashish.nayak@ltts.com', 'prashantsudhir.bagal@ltts.com', 'aakarsh.mehta@ltts.com', 'yash.jhajharia@ltts.com',
                            'manzar.hussain@ltts.com', 'digendrakumar.sahu@ltts.com', 'ankitkumar.yadav@ltts.com', 'manu.nadar@ltts.com']

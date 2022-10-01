try:
    from a06 import text_count
except ImportError:
    pass

try:
    from a06 import copy_lines
except ImportError:
    pass

def test_text_count_s_1():
    assert text_count('.', 'essay.txt') == 455

def test_text_count_s_3():
    assert text_count('.', 'essay.txt', True) == 392

def test_text_count_s_5():
    assert text_count('.', 'essay.txt', False, True) == 2632

def test_copy_lines_s_2():
    copy_lines('essay.txt', 'out.txt', 1)
    with open('out.txt', 'r') as f:
        assert f.read() == """Write a title that summarizes the specific problem"""
        

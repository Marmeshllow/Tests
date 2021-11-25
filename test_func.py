import pytest
from func import show_document_info, remove_doc_from_shelf, add_new_shelf, add_new_doc, append_doc_to_shelf, delete_doc
from func import documents, directories
test_keys_add_shelf = [
    ('1', ('1', False)),
    ('-1', ('-1', False)),          # incorrect
    ('10', ('10', True))
]
test_keys_append_doc = [
    ('11-2', '3'),
    ('10006', '4'),                 # incorrect
    ('0000', '1'),                  # incorrect
]
test_del = [
    ('10006', ('10006', True)),
    ('11-3', None)
]


class TestMainFunc:
    def test_show_document_info(self):
        assert show_document_info(documents[1]) == 'invoice "11-2" "Геннадий Покемонов"'

    def test_remove_doc_from_shelf(self):
        assert remove_doc_from_shelf('10006') not in directories.values()

    @pytest.mark.parametrize('shelf_num, ex_res', test_keys_add_shelf)
    def test_add_new_shelf(self, shelf_num, ex_res):
        assert add_new_shelf(shelf_num) == ex_res

    def test_add_new_doc(self):
        type_ = 'passport'
        num_ = 666
        name_ = 'test_name'
        add_new_doc(type_, num_, name_, 1)
        assert type_ in documents[-1].values() and\
               num_ in documents[-1].values() and\
               name_ in documents[-1].values()

    @pytest.mark.parametrize('dock_num, shelf_num', test_keys_append_doc)
    def test_append_doc_to_shelf(self, dock_num, shelf_num):
        append_doc_to_shelf(dock_num, shelf_num)
        assert dock_num in directories[shelf_num]

    @pytest.mark.parametrize('dock_num, res', test_del)
    def test_delete_doc(self, dock_num, res):
        assert delete_doc(dock_num) == res

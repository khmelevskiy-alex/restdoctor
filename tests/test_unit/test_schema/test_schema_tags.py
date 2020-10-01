from tests.test_unit.test_schema.stubs import DefaultViewSet, ViewSetWithTags


def test_schema_with_tags_success_case(get_create_view_func):
    create_view = get_create_view_func('test', ViewSetWithTags, 'test')

    view = create_view('/test/', 'GET')
    operation = view.schema.get_operation('/test/', 'GET')

    assert operation['tags'] == ['tag1', 'tag2']


def test_schema_without_tags_success_case(get_create_view_func):
    create_view = get_create_view_func('test', DefaultViewSet, 'test')

    view = create_view('/test/', 'GET')
    operation = view.schema.get_operation('/test/', 'GET')

    assert 'tags' not in operation.keys()

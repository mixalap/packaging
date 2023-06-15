def test__get_all(useful_repo, useful_entity1, useful_entity2):
    result = useful_repo.get_all()

    assert result == [useful_entity1, useful_entity2]

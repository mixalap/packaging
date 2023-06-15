from unittest.mock import Mock


def test__run(useful, useful_repo, useful_entity):
    useful_repo.get_all.return_value = [useful_entity]
    useful._log_entity = Mock()

    result = useful.run()

    call_args, call_kwargs = useful_repo.get_all.call_args
    assert call_args == ()
    assert call_kwargs == {}

    call_args = [args for args, _ in useful._log_entity.call_args_list]
    call_kwargs = [kwargs for _, kwargs in useful._log_entity.call_args_list]
    assert call_args == [(useful_entity, )]
    assert call_kwargs == [{}]

    assert result is None


def test__run__entities_are_missing(useful, useful_repo):
    useful_repo.get_all.return_value = []
    useful._log_entity = Mock()

    result = useful.run()

    call_args, call_kwargs = useful_repo.get_all.call_args
    assert call_args == ()
    assert call_kwargs == {}

    call_args = [args for args, _ in useful._log_entity.call_args_list]
    call_kwargs = [kwargs for _, kwargs in useful._log_entity.call_args_list]
    assert call_args == []
    assert call_kwargs == []

    assert result is None

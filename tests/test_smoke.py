from hiboo import main


def test_main_prints_greeting(capsys):
    main()
    captured = capsys.readouterr()
    assert "hiboo" in captured.out.lower()

.PHONY: integration_tests unit_tests

integration_tests:
	docker-compose run --rm python main.py examples/01.bf \
		&& docker-compose run --rm python main.py examples/02.bf \
		&& docker-compose run --rm python main.py examples/03.bf

unit_tests:
	docker-compose run --rm python main_test.py

all:
	echo TELEGRAM_TOKEN=${TELEGRAM_TOKEN} > .env
	docker compose up --build --force-recreate -d

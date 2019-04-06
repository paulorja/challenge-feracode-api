run:
	docker-compose up

check: #todo
	docker exec -it diapers "python manage.py test"

shell:
	docker exec -it diapers /bin/bash

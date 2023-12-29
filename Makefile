.PHONY: help
help: ## Help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort -d | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: migrate
migrate:  ## Run migrations
	@docker compose exec web aerich upgrade

.PHONY: up-local
up:  ## Start project
	@docker compose up --build -d

.PHONY: logs-local
logs: ## Logs backend
	@docker compose logs web -f $(serv)

.PHONY: uninstall-local
uninstall: ## Uninstall local services
	@docker compose $(LOCAL_DOCKER_COMPOSES) down --remove-orphans --volumes


.PHONY: make-migration
make-migration:  ## Make migration
	@docker compose exec web aerich migrate --name add_title_to_order

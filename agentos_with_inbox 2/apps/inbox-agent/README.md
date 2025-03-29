# Inbox Agent

Módulo de comunicação interna para o AgentOS.

### Endpoints disponíveis:
- `POST /inbox/send` – envia uma nova mensagem
- `GET /inbox?user=nome` – retorna a caixa de entrada do usuário
- `PATCH /inbox/{id}/read` – marca a mensagem como lida
- `PATCH /inbox/{id}/archive` – arquiva a mensagem

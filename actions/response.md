# response
Essa ação serve para retornar alguma resposta para o endpoint.

Ex:
```json
{
    "id": "3",
    "action": "response",
    "data": {
        "status": 400,
        "headers": {},
        "data": {
            "success": "false",
            "msg": "Something happened and your flow can't be created :(",
            "data": "${response.data}"
        }
    },
    "next_action": null
}
```

Quando essa action é executada, ela para imediatamente a execução da pipeline e retorna a resposta definida dentro do `data`
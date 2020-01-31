# workspace_var
Diferente do [flow_var](flow_var.md), essa ação serve para definir variáveis que estaram disponíveis para todos os fluxos executados em sequência. 

Ex:
```json
{
    "id": "2",
    "action": "workspace_var",
    "data": {
        "response": "${response.data}"
    },
    "next_action": "3"
}
```

Depois de definida, a variável pode ser recuperada em qualquer ação do fluxo seguinte.

Ex:
```json
{
    "id": "32",
    "action": "response",
    "data": {
        "avg_price": "${function.util.avg_price(workspace.response)}"
    },
    "next_action": "${pipeline.next_action}"
}
```
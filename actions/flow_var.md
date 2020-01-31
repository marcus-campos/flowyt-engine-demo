# flow_var
Essa ação serve para definir variáveis que estaram disponíveis apenas no fluxo. 

Ex:
```json
{
    "id": "2",
    "action": "flow_var",
    "data": {
        "url": "${env.baseUrl}/users"
    },
    "next_action": "3"
}
```

Depois de definida, a variável pode ser recuperada em qualquer ação do fluxo.

Ex:
```json
{
    "id": "3",
    "action": "request",
    "data": {
        "url": "${flow.url}",
        "method": "get",
        "headers": {},
        "data": {},
        "next_action_success": "4",
        "next_action_fail": "5"
    },
    "next_action": "${pipeline.next_action}"
}
```
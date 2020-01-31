# jump
Essa ação serve para "saltar" entre fluxos. É utilizada para dar sequência ao processamento em um outro fluxo.

Ex:
```json
{
    "id": "5",
    "action": "jump",
    "data": {
        "next_flow": "nome-do-fluxo-seguinte"
    },
    "next_action": null
}
```
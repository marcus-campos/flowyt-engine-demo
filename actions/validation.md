# validation
Essa ação foi baseada no [cerberus](https://docs.python-cerberus.org/en/stable/usage.html), basicamente é possível escrever validações utilizando as [regras](https://docs.python-cerberus.org/en/stable/validation-rules.html) disponíveis no cerberus

```json
{
    "id": "2",
    "action": "validation",
    "data": {
        "schema": {
            "name": {"type": "string"},
            "age": {"type": "integer"}
        },
        "next_action_success": "3",
        "next_action_fail": "4"
    },
    "next_action": "${pipeline.next_action}"
}
```
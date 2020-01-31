# switch
Essa ação é utilizada para se tomar decições dentro do fluxo:

Ex:
```json
{
    "id": "1",
    "action": "switch",
    "data": {
        "conditions": [
            {
                "operator": "equal",
                "first_expression": "value 1",
                "second_expression": "value 2",
                "next_action": "3"
            },
            {
                "operator": "different",
                "first_expression": "value 1",
                "second_expression": "value 2",
                "next_action": "3"
            },
            {
                "operator": "greater_than",
                "first_expression": "value 1",
                "second_expression": "value 2",
                "next_action": "3"
            },
            {
                "operator": "less_than",
                "first_expression": "value 1",
                "second_expression": "value 2",
                "next_action": "3"
            }
        ],
        "next_action_else": "4"
    },
    "next_action": "${pipeline.next_action}"
}
```
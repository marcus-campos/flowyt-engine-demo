# request
Essa ação serve para fazer requests HTTP para outros serviços. 

Ex:
```json
{
    "id": "2",
    "action": "request",
    "data": {
        "url": "${env.baseUrl}/document?collection=users",
        "method": "get",
        "headers": {},
        "data": {},
        "next_action_success": "3",
        "next_action_fail": "4"
    },
    "next_action": "${pipeline.next_action}"
}
```
# Tempalte literals
Durante a execução de um fluxo é possível utilizar de template literals para executar alguns "helpers" e trexos de código python.

Ex: `${env.baseUrl}`, neste caso ele vai buscar das variáveis de ambiente definidas nas configurações do workspace a variável `baseUrl`

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

Ex2: `${response.data}` neste caso ele irá pegar tudo do dicionário `data` e atribuir a key `users`
```json
{
    "id": "3",
    "action": "response",
    "data": {
        "status": 200,
        "headers": {},
        "data": {
            "users": "${response.data}"
        }
    },
    "next_action": null
}
```

Ex3: `${True if response.data.approved == 'true' else False}` neste caso ele irá fazer uma operação ternária e atribuir a key `approved` o valor `yes` caso a `response.data.approved` seja igual a `true`
```json
{
    "id": "3",
    "action": "response",
    "data": {
        "status": 200,
        "headers": {},
        "data": {
            "approved": "${'yes' if response.data.approved == 'true' else 'no'}"
        }
    },
    "next_action": null
}
```

Ex4: `${[student for student in response.data if student.approved=='true']}` neste caso ele irá filtrar todos os alunos aprovados e atribuir a lista a key `approved_students`
```json
{
    "id": "3",
    "action": "response",
    "data": {
        "status": 200,
        "headers": {},
        "data": {
            "approved_students": "${[student for student in response.data if student.approved=='true']}"
        }
    },
    "next_action": null
}
```

Ex5: `${function.students.approved_list(response.data)}` neste caso ele irá buscar dentro do workspace na pasta `functions` no arquivo `students` a função `approved_list` e vai executa-la. O retorno da execução será atribuido a key `approved_students`
```json
{
    "id": "3",
    "action": "response",
    "data": {
        "status": 200,
        "headers": {},
        "data": {
            "approved_students": "${function.students.approved_list(response.data)}"
        }
    },
    "next_action": null
}
```
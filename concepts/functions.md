# Funções
Em todo workspace existe uma pasta chamada `functions`, nessa pasta é possível adicionar funções escritas em python, que poderão ser executadas dentro de um fluxo.

Ex: `${function.students.approved_list(response.data)}` neste caso ele irá buscar dentro do workspace na pasta `functions` no arquivo `students` a função `approved_list` e vai executa-la. O retorno da execução será atribuido a key `approved_students`

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

Função:


```python
def approved_list(students):
    new_data = []
    for student in students:
        if student.approved:
            new_data.append({
                "name": item.name
            })
    return new_data
```

```
workspaces
│
└───example1
│   │
│   └───config
│   |   │ ...
|   |
|   └───flows
|   |   | ...
|   |
|   └───functions
|   |   | studdents.py
|   |
|   | routes.json
│   
...
```
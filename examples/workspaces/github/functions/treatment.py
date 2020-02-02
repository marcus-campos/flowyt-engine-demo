def get_new_data(data):
    new_data = []
    for item in data:
        new_data.append(
            {
                "name": item.name,
                "private": item.private,
                "url": item.html_url,
                "stars": item.stargazers_count,
                "language": item.language,
            }
        )
    return new_data

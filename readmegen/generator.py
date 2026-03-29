def generate_readme(data):
    """
    Generate README.md content from user input data
    """

    structure_section = (
        f"\n##  Project Structure\n{data['structure']}\n"
        if data.get("structure")
        else ""
    )

    return f"""# {data['name']}

##  Description
{data['description']}

##  Installation
```bash
{data['installation']}
️ Usage
{data['usage']}

{structure_section}

 Contributing

{data['contributing']}

 License

{data['license']}
"""
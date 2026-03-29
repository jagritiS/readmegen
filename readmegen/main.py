from readmegen.generator import generate_readme


def main():
    print("\n README Generator CLI\n")

    try:
        data = {
            "name": input("Project Name: ").strip(),
            "description": input("Description: ").strip(),
            "installation": input("Installation command (e.g. pip install ...): ").strip(),
            "usage": input("Usage command (e.g. python main.py): ").strip(),
            "structure": input("Project structure (optional, press Enter to skip): ").strip(),
            "contributing": input("Contribution guidelines: ").strip(),
            "license": input("License (MIT/Apache/GPL): ").strip(),
        }

        # Validate required fields
        if not data["name"] or not data["description"]:
            print("\n Project Name and Description are required!")
            return

        # Generate README content
        content = generate_readme(data)

        # Write to file
        with open("README.md", "w", encoding="utf-8") as file:
            file.write(content)

        print("\n README.md generated successfully!")

    except KeyboardInterrupt:
        print("\n\n Operation cancelled by user.")


if __name__ == "__main__":
    main()
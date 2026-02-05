contact = {
    "Yashu": "9988776655",
    "Kruthi": "8877665544",
    "Sumith": "7876989986",
    "Jaanu": "6364287474"
}
contact["Supritha"] = "6364298550"
contact["Yashu"] = "7788996655"
existing_contact = contact.get("Yashu", "contact found")
non_existing_contact = contact.get("James", "Contact Not Found")
print("Yashu:",existing_contact )
print("James:", non_existing_contact )
print("\nContact List:")
for name, phone in contact.items():
    print(f"Contact:{name} | Phone: {phone}")
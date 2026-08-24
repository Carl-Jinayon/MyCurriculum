contacts = {
    "maria": "+63-932-555-0356",
    "juana": "+63-909-555-5646",
    "tessa": "+63-929-555-5505",
    "marga": "+63-932-555-2287",
    "caloy": "+63-933-555-1146"
}

# Retrieve value using key and .get()
contacts.get("caloy")

contacts["potpot"] = "+63-919-555-1754"

contacts["aira"] = contacts.get("potpot")

del contacts["potpot"]

for name, phone in contacts.items():
    print(f"{name}: {phone}")
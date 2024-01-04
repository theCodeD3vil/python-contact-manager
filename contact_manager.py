def create_contact(contacts,name, phone_number, email):
    contact = {
        "name": name,
        "phone_number": phone_number,
        "email": email
    }
    contacts.append(contact)
    return contacts


def get_contact(contacts, name):
    for contact in contacts:
        if contact["name"] == name:
            return contact
    return None

def get_contact_index(contacts, name):
  for contact in contacts:
      if contact["name"] == name:
          return contacts.index(contact)
  return None


def delete_contact(contacts, index):
  new_contacts = contacts
  new_contacts.pop(index)
  return new_contacts
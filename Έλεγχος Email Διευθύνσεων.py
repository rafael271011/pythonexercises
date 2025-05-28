valid_emails = []


for i in range(5):
    email = input(f"Εισάγετε email #{i+1}: ").strip()

    
    if '@' in email and (email.endswith('.com') or email.endswith('.cy') or email.endswith('.gr')):
        print(f"{email} → VALID ✅")
        valid_emails.append(email)
    else:
        print(f"{email} → INVALID ❌")


with open('valid_emails.txt', 'w', encoding='utf-8') as f:
    for email in valid_emails:
        f.write(email + '\n')

print("\nΤα valid emails αποθηκεύτηκαν στο αρχείο valid_emails.txt.")

emails=["tom.ev@gmail.com","tom.ev@gmail.com", "sadhika0409@gmail.com","a123@yahoo.com", "jenniferl@outlook.com", "alice.sven@gmail.com", 
        "charlie.reynolds@yahoo.com", "sadhika0409@gmail.com", "chris22tho@yahoo.com", "a123@yahoo.com"]
print("Original email list:\n", emails)

s=set(emails)
print("Unique emails:",s)

#duplicate emails
duplicate_emails=set([email for email in emails if emails.count(email) > 1])
print("Duplicate emails:",duplicate_emails)



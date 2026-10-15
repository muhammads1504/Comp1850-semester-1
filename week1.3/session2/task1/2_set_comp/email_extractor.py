# Week 1.3, Session 2: Email Extractor

raw_emails = ["UserA@gmail.com", "admin@site.com", "usera@gmail.com", "UserB@yahoo.com", "admin@site.com"]
new_emails = {s.lower() for s in raw_emails}
print(new_emails)
# we use the sets notation to get rid of the repeating ones


# set comprehension to extract a clean, unique set of lowercase email addresses


# print the clean set of email addressed


# Optional - consider the case where some of the emails are not valid (i.e., without the @ in the email address).
# raw_emails2 = ["UserA@gmail.com", "SYSTEM_ALERT", "usera@gmail.com", "admin@site.com", "UserB@yahoo.com"]
# write another set comprehension for this case to extract a clean, unique set of valid, lowercase email addresses

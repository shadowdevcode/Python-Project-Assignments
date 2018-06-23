# Extract the user id, domain name and suffix from the following email addresses.
# emails = "zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"
# desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]

emails = ["zuck26@facebook.com", "page33@google.com", "jeff42@amazon.com"]


def email_split(email):
    username = email.split('@')[0]
    domain = email.split('@')[1]
    domain_name = domain.split('.')[0]
    domain_type = domain.split('.')[1]
    print('Desired Output: ', username + ',', domain_name + ',', domain_type)

for email in emails:
    email_split(email)

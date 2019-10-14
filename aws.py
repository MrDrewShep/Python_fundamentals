"""

Linux EC2
- create non-root users to login
- give user sudo rights
- switch to that user
- mkdir for .ssh, make it private to only that user
(https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/managing-users.html#create-user-account)
- used powershell to generate ssh-keygen.exe
- saved something about both private and public(which came from AWS's website) keys
- make it so we can only ssh in via ...?
- remote access...?
- remove ubuntu file system (overkill, not necessary)


To do:
- firewall
- nginx (alt: apache)
- proxy

heroku - for deploying webapps

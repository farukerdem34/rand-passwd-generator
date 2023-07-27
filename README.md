# Random Password Generator
## Usage
### Completly Random Passwords
`main.py -a AMOUNT -t LENGHT`

`main.py --amount AMOUNT --total-lenght LENGHT`

### Generate Password(s) With Arguments
`main.py -a AMOUNT -n NUMBER -u UPPER_CASE -l LOWER_CASE -s SPECIAL_CHAR -o PASSFILE`
#### Help
`main.py -h`

`main.py --help`

### Saving Passwords To File
**If you set False to the output file argument, the passwords are not saved in any file.**
### Sending E-Mail (Optional)
`--sender MAIL_ADDRESS --password MAIL_PASSWORD --receiver RECEIVER --subject SUBJECT --body BODY --smtp-server SERVER --smtp-port PORT`
> Subject and body is optional

***To send passwords by e-mail, you have to save to file. This is already standard operation, if you set the file save operation to False, the e-mail operation will not work. ***

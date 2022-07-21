Since this is a form with the message "Get this question right to get to the flag!," we might expect that the flag will be stored in the HTML source. Indeed, typing anything into the form field prompts us "Nope! Try inspect element!"

By viewing the page source and searching for `uwctf` (which we know must be part of the flag), we immediately see that the flag is readable directly from the source code.

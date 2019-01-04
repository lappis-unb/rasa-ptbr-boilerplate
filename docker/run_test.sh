echo "Waiting bot container up."
until ping -c1 bot &>/dev/null; do :; done
echo "Bot container up."

echo "Waiting bot up."
until curl bot:5005 &>/dev/null; do :; done
echo "Bot up."

pytest -s test.py

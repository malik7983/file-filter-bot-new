if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/malik7983/file-filter-bot-new.git /file-filter-bot-new
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /file-filter-bot-new
fi
cd /file-filter-bot-new
pip3 install -U -r requirements.txt
echo "Starting Bot....💥"
python3 bot.py

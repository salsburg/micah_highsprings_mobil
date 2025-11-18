# Upload and Run - PythonAnywhere Setup

## Quick Setup (5 minutes total)

### Step 1: Upload the Setup Script (1 minute)

1. **Go to Files tab**: https://www.pythonanywhere.com/user/salsburg/files/
2. Make sure you're in `/home/salsburg/` directory (should be default)
3. Click **"Upload a file"** button
4. Select `pythonanywhere_auto_setup.py` from your computer
5. Click **"Upload"**

---

### Step 2: Run the Setup Script (1 minute)

1. **Go to Consoles tab**: https://www.pythonanywhere.com/user/salsburg/consoles/
2. Click **"Bash"** to start a new console
3. Type this ONE command:

```bash
python3 pythonanywhere_auto_setup.py
```

4. Press Enter
5. Wait 1-2 minutes while it sets everything up
6. You'll see "✅ SETUP COMPLETE!" when done

---

### Step 3: Create Web App (2 minutes)

The script will show you exact instructions, but here's the summary:

1. **Go to Web tab**: https://www.pythonanywhere.com/user/salsburg/webapps/
2. Click **"Add a new web app"**
3. Click **"Next"** (domain will be salsburg.pythonanywhere.com)
4. Choose **"Manual configuration"**
5. Select **"Python 3.10"**
6. Click **"Next"**

---

### Step 4: Configure WSGI (1 minute)

1. On Web tab, find **"Code"** section
2. Click the **WSGI configuration file** link (blue text)
3. **Delete everything** in that file
4. **Paste this**:

```python
import sys
import os

project_home = '/home/salsburg/micah_highsprings_mobil'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ['ENVIRONMENT'] = 'production'

from app import app as application
```

5. Click **"Save"** (top right)

---

### Step 5: Set Virtual Environment (30 seconds)

1. Still on Web tab, scroll to **"Virtualenv"** section
2. Enter exactly: `/home/salsburg/.virtualenvs/micah-mobil-env`
3. Click the checkmark ✓

---

### Step 6: Launch! (10 seconds)

1. Scroll to top of Web tab
2. Click the big green **"Reload salsburg.pythonanywhere.com"** button
3. Click your URL to visit: **https://salsburg.pythonanywhere.com**

---

## ✅ Done!

Your Flask app is now live at:
**https://salsburg.pythonanywhere.com**

**Test the endpoints:**
- Home: https://salsburg.pythonanywhere.com/
- Health: https://salsburg.pythonanywhere.com/api/health
- Status: https://salsburg.pythonanywhere.com/api/status

---

## Alternative: If You Don't Want to Upload

If the upload doesn't work, just run this one command in a Bash console:

```bash
git clone https://github.com/salsburg/micah_highsprings_mobil.git && cd micah_highsprings_mobil && mkvirtualenv --python=/usr/bin/python3.10 micah-mobil-env && pip install -r requirements.txt
```

Then continue from Step 3 above.

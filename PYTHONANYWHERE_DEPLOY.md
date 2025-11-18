# Deploy Flask App to PythonAnywhere

## Step 1: Create Account (2 minutes)

1. Go to: https://www.pythonanywhere.com/registration/register/beginner/
2. Choose a username (e.g., `salsburg` or `micahsalsburg`)
3. Enter email: `salsburg@hotmail.com`
4. Create password
5. Click "Register"
6. Verify email if prompted

---

## Step 2: Open Bash Console (30 seconds)

1. After login, go to: https://www.pythonanywhere.com/user/YOUR_USERNAME/consoles/
2. Click **"Bash"** under "Start a new console"
3. A terminal will open

---

## Step 3: Clone Your GitHub Repo (1 minute)

In the Bash console, run:

```bash
# Clone your repository
git clone https://github.com/salsburg/micah_highsprings_mobil.git

# Navigate into the directory
cd micah_highsprings_mobil

# Verify files are there
ls -la
```

You should see: `app.py`, `requirements.txt`, `wsgi.py`, etc.

---

## Step 4: Create Virtual Environment (1 minute)

```bash
# Create virtual environment
mkvirtualenv --python=/usr/bin/python3.10 micah-mobil-env

# Activate it (should auto-activate after creation)
workon micah-mobil-env

# Install dependencies
pip install -r requirements.txt
```

---

## Step 5: Configure Web App (2 minutes)

1. Go to: https://www.pythonanywhere.com/user/YOUR_USERNAME/webapps/
2. Click **"Add a new web app"**
3. Click **"Next"** (on the domain page - you'll get `YOUR_USERNAME.pythonanywhere.com`)
4. Select **"Manual configuration"**
5. Choose **Python 3.10**
6. Click **"Next"**

---

## Step 6: Configure WSGI File (2 minutes)

1. On the Web app configuration page, scroll to **"Code"** section
2. Click on the **WSGI configuration file** link (something like `/var/www/YOUR_USERNAME_pythonanywhere_com_wsgi.py`)
3. **DELETE ALL THE CONTENTS** of that file
4. **REPLACE WITH**:

```python
import sys
import os

# Replace YOUR_USERNAME with your actual PythonAnywhere username
project_home = '/home/YOUR_USERNAME/micah_highsprings_mobil'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variables
os.environ['ENVIRONMENT'] = 'production'

# Import the Flask app
from app import app as application
```

5. Click **"Save"** (top right)

---

## Step 7: Set Virtual Environment Path (1 minute)

1. Go back to the **Web** tab: https://www.pythonanywhere.com/user/YOUR_USERNAME/webapps/
2. Scroll to **"Virtualenv"** section
3. Enter the path: `/home/YOUR_USERNAME/.virtualenvs/micah-mobil-env`
4. Click the checkmark ✓

---

## Step 8: Reload and Test (30 seconds)

1. Scroll to top of Web tab
2. Click the big green **"Reload YOUR_USERNAME.pythonanywhere.com"** button
3. Click the link to your site: **`https://YOUR_USERNAME.pythonanywhere.com`**

---

## ✅ Your App Should Now Be Live!

**Test these URLs:**
- `https://YOUR_USERNAME.pythonanywhere.com/` - Home page
- `https://YOUR_USERNAME.pythonanywhere.com/api/health` - Health check
- `https://YOUR_USERNAME.pythonanywhere.com/api/status` - Status

---

## Troubleshooting

### If you see an error:

1. Go to Web tab → **Error log** (click to view)
2. Go to Web tab → **Server log** (click to view)
3. Common issues:
   - Wrong username in WSGI file
   - Wrong virtualenv path
   - Missing dependencies (run `pip install -r requirements.txt` again)

### To Update Your App Later:

```bash
# In Bash console
cd ~/micah_highsprings_mobil
git pull origin main
workon micah-mobil-env
pip install -r requirements.txt --upgrade

# Then reload from Web tab
```

---

## Summary

- **Your URL**: `https://YOUR_USERNAME.pythonanywhere.com`
- **Always on**: No spin down
- **Cost**: $0
- **To update**: `git pull` and reload

---

That's it! Your Flask app is now deployed and running 24/7 for free.

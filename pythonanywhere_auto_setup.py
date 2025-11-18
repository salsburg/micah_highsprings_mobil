#!/usr/bin/env python3
"""
PythonAnywhere Auto Setup Script
Run this once to set up the Flask app automatically
"""

import os
import subprocess
import sys

def run_command(cmd, description):
    """Run a shell command and print status"""
    print(f"\n{'='*60}")
    print(f"📝 {description}")
    print(f"{'='*60}")
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print(f"✅ SUCCESS")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ ERROR: {e}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False

def main():
    print("\n" + "="*60)
    print("🚀 PythonAnywhere Flask App Auto Setup")
    print("="*60)

    home_dir = os.path.expanduser("~")
    project_dir = os.path.join(home_dir, "micah_highsprings_mobil")

    # Step 1: Clone repository
    if not os.path.exists(project_dir):
        if not run_command(
            "git clone https://github.com/salsburg/micah_highsprings_mobil.git ~/micah_highsprings_mobil",
            "Cloning GitHub repository"
        ):
            print("\n❌ Failed to clone repository. Exiting.")
            sys.exit(1)
    else:
        print(f"\n✅ Repository already exists at {project_dir}")

    # Step 2: Create virtual environment
    venv_path = os.path.join(home_dir, ".virtualenvs", "micah-mobil-env")
    if not os.path.exists(venv_path):
        if not run_command(
            "mkvirtualenv --python=/usr/bin/python3.10 micah-mobil-env",
            "Creating virtual environment"
        ):
            print("\n❌ Failed to create virtual environment. Exiting.")
            sys.exit(1)
    else:
        print(f"\n✅ Virtual environment already exists")

    # Step 3: Install dependencies
    os.chdir(project_dir)
    activate_cmd = f"source {venv_path}/bin/activate"
    install_cmd = f"{activate_cmd} && pip install -r requirements.txt"

    if not run_command(install_cmd, "Installing Python dependencies"):
        print("\n❌ Failed to install dependencies. Exiting.")
        sys.exit(1)

    # Step 4: Display next steps
    print("\n" + "="*60)
    print("✅ SETUP COMPLETE!")
    print("="*60)
    print("\n📋 NEXT STEPS:")
    print("\n1. Go to: https://www.pythonanywhere.com/user/salsburg/webapps/")
    print("2. Click 'Add a new web app'")
    print("3. Click 'Next' (domain: salsburg.pythonanywhere.com)")
    print("4. Choose 'Manual configuration'")
    print("5. Select 'Python 3.10'")
    print("6. Click 'Next'")
    print("\n7. On the Web tab, click the WSGI configuration file")
    print("8. Delete everything and paste this:")
    print("\n" + "-"*60)
    print("""import sys
import os

project_home = '/home/salsburg/micah_highsprings_mobil'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ['ENVIRONMENT'] = 'production'

from app import app as application""")
    print("-"*60)
    print("\n9. Save the WSGI file")
    print("\n10. Back on Web tab, in Virtualenv section, enter:")
    print("    /home/salsburg/.virtualenvs/micah-mobil-env")
    print("\n11. Click the Reload button")
    print("\n12. Visit: https://salsburg.pythonanywhere.com")
    print("\n" + "="*60)
    print("🎉 Your Flask app will be live!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()

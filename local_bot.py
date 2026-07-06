import time
import subprocess
import sys

print("==================================================")
print("🐍 Local Snake Game Auto-Improver Bot")
print("This script runs on your computer and pushes to GitHub.")
print("It is MUCH more reliable than GitHub Actions.")
print("==================================================\n")

def run_cmd(cmd):
    try:
        subprocess.run(cmd, check=True, shell=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {cmd}")
        return False

# Ensure we are up to date
print("Pulling latest changes from GitHub...")
run_cmd("git pull --rebase origin master")

run_count = 1
while True:
    print(f"\n▶️ Starting Run #{run_count}...")
    
    # 1. Run the improve script to generate 10 commits (with 25s delays)
    # The improve script already commits the files locally.
    success = run_cmd("python scripts/improve.py")
    
    if success:
        print("\n✅ Run complete! Pushing all new commits to GitHub...")
        # 2. Push to GitHub
        # We rebase first just in case there are remote changes
        run_cmd("git pull --rebase origin master")
        push_success = run_cmd("git push origin master")
        
        if push_success:
            print("🚀 Successfully pushed to GitHub!")
        else:
            print("⚠️ Failed to push. Will try again next run.")
    else:
        print("⚠️ Improve script failed. Will try again next run.")
        
    print("\n⏳ Waiting 5 minutes before next run...")
    print("   (Press Ctrl+C to stop the bot at any time)")
    
    # Wait 5 minutes before repeating
    try:
        time.sleep(300)
    except KeyboardInterrupt:
        print("\n\n🛑 Bot stopped by user. Goodbye!")
        sys.exit(0)
    
    run_count += 1

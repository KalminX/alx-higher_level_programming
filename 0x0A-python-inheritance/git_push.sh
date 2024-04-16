#!/bin/bash

# Get the commit message from the user
echo "Enter the commit message:"
read commit_message

# Add all changes to the staging area
git add .

# Commit the changes
git commit -m "$commit_message"

# Push the changes to the remote repository
git push
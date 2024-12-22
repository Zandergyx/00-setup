# PY2 Exercises

## Getting Started

Follow these steps to set up your environment, configure your repository, and submit your exercises.

---

### Step 1: Accept the Collaboration Invitation  

Check your email for the invitation to collaborate on the repository. Once you receive it, click the link and accept the invitation to be added as a collaborator.

---

### Step 2: Set Up the Repository  

#### Configure Git

Set up your Git username and email by running the following commands in your terminal:

```bash
git config --global user.name "FIRST_NAME LAST_NAME"
git config --global user.email "EMAIL@example.com"
```

#### Initialize the Repository

Run the following commands to configure your repository:

```bash
git init
git add .
git branch -M main
git remote add origin https://github.com/lcclstudents/PY2-<USERNAME>-<NAME>.git
```

#### Commit and Push  

Use the following commands to commit your changes and push them to the remote repository:

```bash
git commit -m 'setup'
git push -u origin main
```

> **Note:** If the `git commit/push` command does not work, you can commit and push using VSCode instead.

---

### Step 3: Add Exercise Files

1. Place any previously completed exercises (those without testcases) into the `old/` folder and run the following command

```bash
git add old/

git commit -m 'add old exercise'
git push -u origin main
```

> **Note:** If the `git commit/push` command does not work, you can commit and push using VSCode instead.

2. Extract the new exercise files into the repository directory.

---

## Submitting  

Once you have completed the exercises and passed all test cases:

1. Open the Source Control view in VSCode
2. Click on the ➕ icon for the completed exercise (to stage the file)
    - You should see the file appear under a section called (Staged Changes)
    - ONLY stage the file you have completed
3. Add a meaningful commit message
4. Press '✔ commit'
5. Press '🔄 Sync changes' to push the exercises to github

> **Note:** Ensure all test cases pass before submission.

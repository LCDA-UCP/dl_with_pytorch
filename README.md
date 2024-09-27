# Deep Learning (DL) with Pytorch


This repository contains a collection of exercises and practice materials for DL classes.

## Curricular Unit
Aprendizagem Profunda, Licenciatura em Ciência de Dados Aplicada, Universidade Católica Portuguesa, 2024-2025.

## Syllabus

| **Module** | **Topic**            | **Lecture**                          | **Exercises**                    |
|------------|----------------------|--------------------------------------|----------------------------------|
| 1          | Course Introduction  | [lecture](lectures/DL-Session01.pdf) | -                                |
| 2          | NumPy Fundamentals   | [lecture](lectures/DL-Session02.pdf) | [exercises](exercises/session02) |
| 3          | The Perceptron       | [lecture](lectures/DL-Session03.pdf) | [exercises](exercises/session03) |
| 4          | PyTorch Introduction | [lecture](lectures/DL-Session04.pdf) | [exercises](exercises/session04) |
| 5          | -                    | -                                    | -                                |
| 6          | -                    | -                                    | -                                |

## Setup

First, clone the repository from GitHub into your local machine. You can do this by running the following command in your terminal:

```bash
git clone https://github.com/LCDA-UCP/dl_with_pytorch.git
```

Open the repository in your favorite IDE and install the dependencies (if missing):
```bash
pip install -r requirements.txt
```

**Note: If you are using a virtual environment, make sure to activate it before running the command above. Using a conda environment is recommended.**

You can now commit and push your changes to your forked repository.

## Create a branch with your name

To create a branch with your name, run the following command in your terminal:

```bash
git checkout -b your_name
```

This will create a new branch with your name and switch to it.

## Pushing changes to your branch

To push your changes to your branch, run the following command in your terminal:

```bash
git push origin your_name
```

This will push your changes to your branch on GitHub.

## Updating your branch with the latest changes from the main branch

If you want to update your branch with the latest changes from the main branch, you can do so pulling the changes from it.

For that, run the following command in your terminal:

```bash
git pull origin main
```

This will update your branch with the latest changes from the main branch.

## If pull fails:

If you get an error message, make sure to commit your changes before pulling the changes from the main branch.

You may also need to fetch the changes from the main branch and merge them into your branch.

For that, run the following commands in your terminal:

```bash
git fetch origin main
git merge origin/main
```

If you have any conflicts, you will need to resolve them before committing the changes.

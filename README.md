# Deep Learning (DL) with Pytorch


This repository contains a collection of exercises and practice materials for DL classes.

## Curricular Unit
Aprendizagem Profunda, Licenciatura em Ciência de Dados Aplicada, Universidade Católica Portuguesa, 2024-2025.

## Syllabus

| **Module** | **Topic**                                                                        | **Lecture**                             | **Exercises**                           |
|------------|----------------------------------------------------------------------------------|-----------------------------------------|-----------------------------------------|
| 1          | Course Introduction                                                              | [lecture](lectures/DL-Session01.pdf)    | -                                       |
| 2          | NumPy Fundamentals                                                               | [lecture](lectures/DL-Session02.pdf)    | [exercises](exercises/session02)        |
| 3          | The Perceptron                                                                   | [lecture](lectures/DL-Session03.pdf)    | [exercises](exercises/session03)        |
| 4          | PyTorch Introduction                                                             | [lecture](lectures/DL-Session04.pdf)    | [exercises](exercises/session04)        |
| 5          | Training Neural Networks                                                         | [lecture](lectures/DL-Session05.pdf)    | -                                       |
| 6          | Neural Networks with PyTorch                                                     | [lecture](lectures/DL-Session06.pdf)    | [exercises](exercises/session06-08)     |
| 7          | Model Selection and Hyperparameter Tuning                                        | [lecture](lectures/DL-Session07.pdf)    | -                                       |
| 8          | Neural Networks with PyTorch                                                     | [lecture](lectures/DL-Session08.pdf)    | [exercises](exercises/session06-08)     |
| 9          | Regularization                                                                   | [lecture](lectures/DL-Session09.pdf)    | -                                       |
| 10         | Convolutional Neural Networks                                                    | [lecture](lectures/DL-Session10-11.pdf) | -                                       |
| 11         | Convolutional Neural Networks - Hands-On                                         | [lecture](lectures/DL-Session10-11.pdf) | [exercises](exercises/session11-12)     |
| 12         | Convolutional Neural Networks - Hands-On                                         | [lecture](lectures/DL-Session12.pdf)    | [exercises](exercises/session11-12)     |
| 13         | Intro to Computer Vision and Image Classification                                | [lecture](lectures/DL-Session13.pdf)    |                                         |
| 14         | Recurrent Neural Networks                                                        | [lecture](lectures/DL-Session14.pdf)    | -                                       |
| 15         | Recurrent Neural Networks                                                        | [lecture](lectures/DL-Session15.pdf)    | [exercises](exercises/session15-16-17)  |
| 16         | Recurrent Neural Networks - Hands-On                                             | [lecture](lectures/DL-Session16.pdf)    | [exercises](exercises/session15-16-17)  |
| 17         | Recurrent Neural Networks - Hands-On                                             | [lecture](lectures/DL-Session17.pdf)    | [exercises](exercises/session15-16-17)  |
| 18         | Attention Mechanisms                                                             | [lecture](lectures/DL-Session18.pdf)    | -                                       |
| 19         | Attention Mechanisms - Hands-On                                                  | [lecture](lectures/DL-Session19.pdf)    | [exercises](exercises/session19-20)     |
| 20         | Attention Mechanisms - Hands-On                                                  | [lecture](lectures/DL-Session20.pdf)    | [exercises](exercises/session19-20)     |
| 21         | Exam                                                                             | [lecture](lectures/DL-Session21.pdf)    | -                                       |
| 22         | Transformers                                                                     | [lecture](lectures/DL-Session22.pdf)    | [exercises](exercises/session22-23-24)  |
| 23         | Transformers - Hands-On                                                          | [lecture](lectures/DL-Session23.pdf)    | [exercises](exercises/session22-23-24)  |
| 24         | Transformers - Hands-On                                                          | [lecture](lectures/DL-Session24.pdf)    | [exercises](exercises/session22-23-24)  |
| 25         | Work on Project                                                                  | [lecture](lectures/DL-Session25.pdf)    | -                                       |
| 26         | Multi-Topic Overview: Multimodal + Transfer + Efficient + Reinforcement Learning | [lecture](lectures/DL-Session26.pdf)    | -                                       |
| 27         | Project Presentation                                                             | [lecture](lectures/DL-Session27.pdf)    | -                                       |

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

You also need to install pytorch. For that follow the instructions on the [official website](https://pytorch.org/get-started/locally/).

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

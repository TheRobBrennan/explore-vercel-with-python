# Welcome

This project will explore how [Python](https://www.python.org) apps might be configured and set up for deployment to [Vercel](https://vercel.com).

## Getting started

To develop and run these projects locally, you'll want to make sure you have the [npm](https://www.npmjs.com) CLI installed on your development environment to install the [Vercel CLI](https://vercel.com/docs/cli) to develop and deploy your applications to [Vercel](https://vercel.com).

### Install the Vercel CLI

```sh
# Install the Vercel CLI 
% npm i -g vercel
```

Assuming you already have an account on [Vercel](https://vercel.com), follow the prompts to authenticate your account with the [Vercel CLI](https://vercel.com/docs/cli) or log in via the command line:

```sh
% vercel login myemail@mail.com
```

## Examples

### Hello, world!

The obligatory "Hello, world!" example is available [here](./hello-world/README.md).

### Dice Roll

This example was initially presented in the [Using Vercel to host a Python API.](https://www.frontend-devops.com/blog/python-on-vercel) blog post and is available [here](./dice-roll/README.md).

### Hello, Matplot

The example at [](./hello-matplot/README.md) demonstrates how [Matplot](https://matplotlib.org) ~~can~~ should be used to return an image from a [Python](https://www.python.org) API endpoint hosted on [Vercel](https://vercel.com).

(!) KNOWN ISSUE: While running this project on macOS using Python 3.11.1, this functions as expected with `vercel dev` but does **NOT** result in a successful deployment to Vercel with `vercel deploy` 🤔 (!)

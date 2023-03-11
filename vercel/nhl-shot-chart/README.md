# Welcome

This guide assumes you have configured the [Vercel CLI](https://vercel.com/docs/cli) and authenticated with an account on [Vercel](https://vercel.com).

If you need guidance in getting this set up, please review the [README](../README.md) in this project's `vercel` folder.

## Getting started

### Local development

With the [Vercel CLI](https://vercel.com/docs/cli) installed on your system, we can use the CLI to spin up our local environment with:

```sh
% vercel dev

```

You should be able to see a simple plot by opening [http://localhost:3000/](http://localhost:3000/) in your favorite browser. Note that we have defined a redirect rule in [](./vercel.json) so that any requests for the root URL are automatically redirected to [http://localhost:3000/api](http://localhost:3000/api).

After a request has been made, you can press `CTRL+C` to cancel the process, and you will see something like this:

```sh
% vercel dev

```

### Deploy to Vercel

When you are ready to deploy your project, you can use the [Vercel CLI](https://vercel.com/docs/cli) installed on your system:

```sh
% vercel deploy

```

In the example output above, going to []() should display a simple shot chart on Vercel.

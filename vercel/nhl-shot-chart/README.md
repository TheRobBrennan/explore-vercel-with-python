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

### Deploy to Vercel

When you are ready to deploy your project, you can use the [Vercel CLI](https://vercel.com/docs/cli) installed on your system:

```sh
% vercel deploy
Vercel CLI 28.16.15
🔍  Inspect: https://vercel.com/therobbrennan/nhl-shot-chart/A1zD7K1yXUCT4WWVFrQcRDEB2N1W [1s]
✅  Production: https://nhl-shot-chart.vercel.app [37s]
📝  Deployed to production. Run `vercel --prod` to overwrite later (https://vercel.link/2F).
💡  To change the domain or build command, go to https://vercel.com/therobbrennan/nhl-shot-chart/settings
```

In the example output above, going to [https://nhl-shot-chart.vercel.app/api](https://nhl-shot-chart.vercel.app) should display a simple shot chart on Vercel.

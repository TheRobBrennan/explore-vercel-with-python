# Welcome

This guide assumes you have configured the [Vercel CLI](https://vercel.com/docs/cli) and authenticated with an account on [Vercel](https://vercel.com).

If you need guidance in getting this set up, please review the [README](../README.md) in this project's `vercel` folder.

## Getting started

### Local development

With the [Vercel CLI](https://vercel.com/docs/cli) installed on your system, we can use the CLI to spin up our local environment with:

```sh
% vercel dev
Vercel CLI 28.16.2
? Set up and develop “~/repos/explore-nhl-api-with-r-and-python/vercel/hello-matplot”? [Y/n] y
? Which scope should contain your project? TheRobBrennan
? Link to existing project? [y/N] n
? What’s your project’s name? hello-matplot
? In which directory is your code located? ./
Local settings detected in vercel.json:
No framework detected. Default Project Settings:
- Build Command: `npm run vercel-build` or `npm run build`
- Development Command: None
- Install Command: `yarn install`, `pnpm install`, or `npm install`
- Output Directory: `public` if it exists, or `.`
? Want to modify these settings? [y/N] n
🔗  Linked to therobbrennan/hello-matplot (created .vercel)
> Ready! Available at http://localhost:3000
```

You should be able to see a simple plot by opening [http://localhost:3000/](http://localhost:3000/) in your favorite browser. Note that we have defined a redirect rule in [](./vercel.json) so that any requests for the root URL are automatically redirected to [http://localhost:3000/api](http://localhost:3000/api).

After a request has been made, you can press `CTRL+C` to cancel the process, and you will see something like this:

```sh
% vercel dev
Vercel CLI 28.16.2
> Ready! Available at http://localhost:3000
> Building @vercel/python@latest:api/index.py
Installing required dependencies...
> Built @vercel/python@latest:api/index.py [12s]
using HTTP Handler
127.0.0.1 - - [18/Feb/2023 10:28:07] "GET /api HTTP/1.1" 200 -
^C
```

### Deploy to Vercel

When you are ready to deploy your project, you can use the [Vercel CLI](https://vercel.com/docs/cli) installed on your system:

```sh
% vercel deploy
Vercel CLI 28.16.2
> Ready! Available at http://localhost:3000
> Building @vercel/python@latest:api/index.py
Installing required dependencies...
> Built @vercel/python@latest:api/index.py [12s]
using HTTP Handler
127.0.0.1 - - [18/Feb/2023 10:28:07] "GET /api HTTP/1.1" 200 -
^C
rob@prism hello-matplot % vercel deploy
Vercel CLI 28.16.12
🔍  Inspect: https://vercel.com/therobbrennan/hello-matplot/EMQtYxndKpzAx455UdQJvjB8Ucan [1s]
✅  Production: https://hello-matplot.vercel.app [32s]
📝  Deployed to production. Run `vercel --prod` to overwrite later (https://vercel.link/2F).
💡  To change the domain or build command, go to https://vercel.com/therobbrennan/hello-matplot/settings
```

In the example output above, going to [https://hello-matplot.vercel.app/api](https://hello-matplot.vercel.app/api) will display a simple line chart using matplot on Vercel.

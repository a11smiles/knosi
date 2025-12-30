# Knosi Marketing Website

This is the static marketing website for Knosi, designed to be hosted on GitHub Pages.

## Features

- Clean, modern design with Tailwind CSS
- Fully responsive layout
- Purple/blue color scheme
- Fast loading (single HTML file with CDN resources)
- SEO optimized

## Deployment to GitHub Pages

### Option 1: Deploy from root

1. Go to your GitHub repository settings
2. Navigate to **Pages** section
3. Under "Source", select **Deploy from a branch**
4. Select branch: `main`
5. Select folder: `/web`
6. Click **Save**

### Option 2: Deploy to gh-pages branch

```bash
# From project root
git subtree push --prefix web origin gh-pages
```

Then in GitHub settings:
- Source: **Deploy from a branch**
- Branch: `gh-pages`
- Folder: `/ (root)`

## Local Development

Simply open `index.html` in your browser. No build step required!

## Customization

The website uses Tailwind CSS via CDN. To customize:

1. **Colors**: Edit the `tailwind.config` in the `<script>` tag
2. **Content**: Edit the HTML directly
3. **Links**: Update GitHub links to point to your repository

## License

MIT License - Same as the Knosi project

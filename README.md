# DTEK Schedule Scraper

This repository contains a GitHub Actions workflow that scrapes the latest DTEK schedule data.

> **Note:** The scraper relies on the [**Browserless API**](https://www.browserless.io/). You’ll need a valid Browserless API key and must add it as a secret named `BROWSERLESS_TOKEN` in your repository settings.  
> Keep in mind that you may need to adjust the update frequency to stay within the free‑plan limits.

## 🕐 Latest Data

- [Kyiv Oblast](https://e1ectr0cut1e.github.io/dtek-parser/dtek-krem.json)
- [Odesa](https://e1ectr0cut1e.github.io/dtek-parser/dtek-oem.json)

*(The most recent data is automatically committed to the `data` branch.)*

## 📁 Historical Data

All previously collected snapshots are stored in the `data` branch. Feel free to explore the commit history for past records.

## 🙏 Acknowledgements

Thanks to [@lifearoundfreaks](https://github.com/lifearoundfreaks) for the brilliant and efficient initial implementation.

## ✳️ Adding More Sites

To scrape additional sites:

1. **Fork the repository.**
2. **Obtain a [Browserless](https://www.browserless.io/) API token.**
3. **Adjust the environment names** in [.github/workflows/dtek.yaml](.github/workflows/dtek.yaml).
4. **Create the corresponding environments** in your repository settings.
5. **Set the variables** for each environment:
   - `NAME` – used for naming the JSON file.
   - `SHUTDOWNS_URL` – the shutdowns page URL (e.g., `https://www.dtek‑X.com.ua/ua/shutdowns`).
6. **Set the secrets** for each environment:
   - `BROWSERLESS_TOKEN` – the Browserless API token.
   - `WEBHOOK_URL` – optional; if set, the latest JSON will be posted to this endpoint whenever the schedule changes.
7. **Adjust the update schedule** in [.github/workflows/dtek.yaml](.github/workflows/dtek.yaml) if you’d like to increase or decrease how often the scraper runs.
8. **Enable scheduled GitHub Actions** (the workflow is already configured to run on a cron schedule).
9. **You’re all set!** Commit your changes and push them to your fork; the workflow will start running on the defined schedule.
